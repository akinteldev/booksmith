#!/usr/bin/env python3
"""
Booksmith Pipeline Orchestrator
Manages the end-to-end book creation pipeline: planning → drafting → review → logues → finalizing.
Reads config, manages git operations, handles human gate timeout, and logs execution.
"""

import os
import sys
import yaml
import json
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


class BooksmithPipeline:
    def __init__(self, book_name: str):
        self.project_root = Path(__file__).parent.parent.resolve()
        self.config_path = self.project_root / "config.yaml"
        self.book_dir = self.project_root / "books" / book_name
        
        # Load configuration
        with open(self.config_path) as f:
            self.config = yaml.safe_load(f)
        
        # Setup paths
        self.books_dir = self.project_root / self.config["paths"]["books_dir"]
        self.logs_dir = self.project_root / self.config["paths"]["logs_dir"]
        self.pipeline_dir = self.project_root / "pipeline"
        self.templates_dir = self.pipeline_dir / "templates"
        
        # Logging
        self.log_file = None
        self._init_logging()
    
    def _log(self, message: str, level: str = "INFO"):
        """Write log entry to file and stdout."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(entry + "\n")
        
        print(entry)
    
    def _init_logging(self):
        """Initialize log file for this run."""
        os.makedirs(self.logs_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.logs_dir / f"booksmith_{timestamp}.log"
        self._log(f"=== Booksmith Pipeline Started ===")
        self._log(f"Book: {self.book_dir.name}")
    
    def _run_git(self, *args) -> subprocess.CompletedProcess:
        """Run a git command in the project root."""
        cmd = ["git", "-C", str(self.project_root)] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            self._log(f"Git error: {result.stderr}", "ERROR")
        
        return result
    
    def git_pull(self):
        """Pull latest changes from remote."""
        self._log("Pulling latest changes...")
        result = self._run_git("pull", "origin", self.config["github"]["branch"])
        if result.returncode == 0:
            self._log(f"Pull successful: {result.stdout.strip()[:100]}")
        else:
            # If repo is empty/new, this is expected - continue
            self._log("Git pull failed (may be new repo), continuing...", "WARN")
    
    def git_push(self, message: str):
        """Push changes to remote."""
        self._log(f"Committing and pushing: {message}")
        
        # Add all changes
        self._run_git("add", "-A")
        
        # Check if there are changes
        status = self._run_git("status", "--porcelain")
        if not status.stdout.strip():
            self._log("No changes to commit.")
            return
        
        # Commit
        self._run_git("commit", "-m", message)
        
        # Push
        result = self._run_git("push", "origin", self.config["github"]["branch"])
        if result.returncode == 0:
            self._log(f"Push successful.")
        else:
            self._log(f"Push failed: {result.stderr}", "ERROR")
    
    def git_commit(self, message: str):
        """Commit changes without pushing (for intermediate steps)."""
        result = self._run_git("add", "-A")
        status = self._run_git("status", "--porcelain")
        
        if not status.stdout.strip():
            return
        
        self._run_git("commit", "-m", message)
        self._log(f"Committed: {message}")
    
    def initialize_book(self):
        """Create book directory structure."""
        self._log(f"Initializing book directory: {self.book_dir.name}")
        
        # Create all subdirectories
        for subdir in ["planning", "chapters", "review", "logues", "manuscript"]:
            (self.book_dir / subdir).mkdir(parents=True, exist_ok=True)
        
        self._log("Directory structure created.")
    
    def read_file(self, path: Path) -> str:
        """Read a file and return its content."""
        with open(path) as f:
            return f.read()
    
    def write_file(self, path: Path, content: str):
        """Write content to a file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        self._log(f"Written: {path.relative_to(self.project_root)}")
    
    def list_files(self, directory: Path, extension: str = None) -> list:
        """List files in a directory."""
        if not directory.exists():
            return []
        
        files = list(directory.iterdir())
        if extension:
            files = [f for f in files if f.suffix == extension]
        
        return sorted(files)
    
    def phase1_planning(self, reports_dir: Path):
        """Phase 1: Generate book bible and chapter prompts."""
        self._log("=" * 60)
        self._log("PHASE 1: PLANNING")
        self._log("=" * 60)
        
        # Read all report files
        reports = {}
        for i, report_file in enumerate(self.list_files(reports_dir, ".md"), 1):
            reports[f"Report #{i}"] = {
                "path": report_file,
                "content": self.read_file(report_file)
            }
        
        # Output paths
        bible_path = self.book_dir / "planning" / "book_bible.md"
        prompts_dir = self.book_dir / "planning" / "chapter_prompts"
        prompts_dir.mkdir(exist_ok=True)
        
        # Return data for LLM processing
        return {
            "reports": reports,
            "bible_path": bible_path,
            "prompts_dir": prompts_dir,
            "template_bible": self.read_file(self.templates_dir / "book_bible_template.md"),
            "template_prompt": self.read_file(self.templates_dir / "chapter_prompt_template.md")
        }
    
    def phase2_drafting(self, chapter_data: dict):
        """Phase 2: Draft chapters with self-review."""
        self._log("=" * 60)
        self._log("PHASE 2: DRAFTING (Serial)")
        self._log("=" * 60)
        
        results = []
        total_chapters = len(chapter_data["prompts"])
        
        for i, chapter in enumerate(chapter_data["prompts"], 1):
            self._log(f"\n--- Drafting Chapter {i}/{total_chapters}: {chapter['title']} ---")
            
            # This is where the LLM would be called to draft the chapter
            # For now, return structure for agent execution
            
            results.append({
                "number": i,
                "title": chapter["title"],
                "subtitle": chapter.get("subtitle", ""),
                "status": "pending"  # Will be updated after drafting
            })
        
        return {
            "results": results,
            "chapters_dir": self.book_dir / "chapters"
        }
    
    def phase2b_review_gate(self, draft_results: list) -> dict:
        """Phase 2b: Human review gate."""
        self._log("=" * 60)
        self._log("PHASE 2B: REVIEW GATE")
        self._log("=" * 60)
        
        # Compile flagged chapters
        flagged = [r for r in draft_results if r.get("status") == "needs_review"]
        
        report = {
            "total_chapters": len(draft_results),
            "approved": len([r for r in draft_results if r["status"] == "approved"]),
            "flagged": flagged,
            "timeout_days": self.config["pipeline"]["human_gate_timeout_days"],
            "auto_fix_on_timeout": True
        }
        
        self._log(f"Review Report: {report['approved']} approved, {len(flagged)} flagged")
        
        return report
    
    def phase3_manuscript_review(self):
        """Phase 3: Full manuscript review."""
        self._log("=" * 60)
        self._log("PHASE 3: MANUSCRIPT REVIEW")
        self._log("=" * 60)
        
        # Read all chapters
        chapters_dir = self.book_dir / "chapters"
        chapters = self.list_files(chapters_dir, ".md")
        
        if not chapters:
            self._log("No chapters found for review.", "ERROR")
            return None
        
        chapter_contents = []
        for ch in chapters:
            chapter_contents.append({
                "file": ch.name,
                "content": self.read_file(ch)
            })
        
        # Read book bible for context
        bible_path = self.book_dir / "planning" / "book_bible.md"
        if bible_path.exists():
            bible_content = self.read_file(bible_path)
        else:
            bible_content = ""
        
        return {
            "chapters": chapter_contents,
            "bible": bible_content,
            "review_template": self.read_file(self.templates_dir / "manuscript_review_template.md")
        }
    
    def phase4_logues(self):
        """Phase 4: Write supplementary material."""
        self._log("=" * 60)
        self._log("PHASE 4: LOGUES WRITING")
        self._log("=" * 60)
        
        logues_config = self.config["pipeline"]["logues_included"]
        logues_dir = self.book_dir / "logues"
        logues_dir.mkdir(exist_ok=True)
        
        available_logues = {k: v for k, v in logues_config.items() if v}
        
        return {
            "logue_types": list(available_logues.keys()),
            "logue_template": self.read_file(self.templates_dir / "logues_template.md")
        }
    
    def phase5_finalizing(self):
        """Phase 5: Stitch all parts into final manuscript."""
        self._log("=" * 60)
        self._log("PHASE 5: FINALIZING")
        self._log("=" * 60)
        
        manuscript_dir = self.book_dir / "manuscript"
        manuscript_dir.mkdir(exist_ok=True)
        final_path = manuscript_dir / "final_manuscript.md"
        
        # Define the order of sections
        sections_order = [
            ("planning", "book_bible.md"),  # Optional: include bible as appendix or skip
            ("logues", None),                # All logue files in alphabetical order
            ("chapters", None),              # All chapter files in numerical order
        ]
        
        parts = []
        
        # Add logues first (foreword, intro, prologue)
        logues_dir = self.book_dir / "logues"
        if logues_dir.exists():
            for logue_file in sorted(self.list_files(logues_dir, ".md")):
                parts.append(f"\n\n{'='*60}\n\n{self.read_file(logue_file)}")
        
        # Add chapters in order
        chapters_dir = self.book_dir / "chapters"
        if chapters_dir.exists():
            for ch_file in sorted(self.list_files(chapters_dir, ".md")):
                parts.append(f"\n\n{'='*60}\n\n{self.read_file(ch_file)}")
        
        # Combine with title page and TOC placeholder
        final_content = f"""# {{book_title}}

## Copyright Notice

© {datetime.now().year} {{author_name}}. All rights reserved.

## Table of Contents

{{toc_placeholder}}

---
""" + "".join(parts)
        
        return {
            "final_path": final_path,
            "template": final_content
        }
    
    def run(self):
        """Execute the full pipeline."""
        self._log(f"Starting Booksmith Pipeline for: {self.book_dir.name}")
        
        try:
            # Initialize book structure
            self.initialize_book()
            
            # Phase 1: Planning
            reports_dir = self.book_dir / "reports"
            if not reports_dir.exists():
                self._log(f"Reports directory not found: {reports_dir}", "ERROR")
                return False
            
            phase1_data = self.phase1_planning(reports_dir)
            
            # Phase 2: Drafting (would be called by agent with LLM)
            # This is where the actual LLM calls happen in conversation
            
            self._log("\nPipeline structure ready. Ready for agent execution.")
            return True
            
        except Exception as e:
            self._log(f"Pipeline error: {str(e)}", "ERROR")
            import traceback
            self._log(traceback.format_exc(), "ERROR")
            return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python booksmith_pipeline.py <book_name>")
        sys.exit(1)
    
    book_name = sys.argv[1]
    pipeline = BooksmithPipeline(book_name)
    success = pipeline.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
