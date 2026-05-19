# Self-Review Checklist — Chapter 7: The Voice on the Phone

## Review Criteria

### 1. Completeness vs. Chapter Prompt
- [x] All "Must Cover" points addressed: persona-simulation pipeline (public-data + breach + internal data synthesis), voice/video AI vishing and deepfake help-desk fraud, conversational extortion bots, Zscaler ThreatLabz voice-based social engineering forecast, connection to access economy (session cookies / Entra ID / SSO tokens), MFA-bypass-via-exception-channel logic.
- [x] Key data points incorporated: Zscaler ThreatLabz 2026 voice-based social engineering forecast; Trend Micro 2026 extortion-bot forecast; hyper-personalization as fusion of public + stolen + internal data; access-economy supply chain.
- [x] Required opening (help-desk technician on Tuesday morning receiving cloned-voice call from executive seeking MFA reset), body flow (scene → persona-simulation pipeline → voice/video & shrinking skill barrier → conversational bots → access-economy connection → defensive shift), and closing (training-as-category-error revelation, set-up for Ch 8 negotiation desk) all present.
- [x] Does not poach Ch 8 (negotiation desk operational detail) or Ch 9 (cryptographic wall); stops at the social-engineering/identity surface.
- **Issues:** none.

### 2. Continuity vs. Book Bible
- [x] Voice: veteran investigative journalist; calm alarm; translation over sensationalism. The chapter resists the "AI = autonomous attacker" hype trap by framing voice cloning and extortion bots as operator-augmentation tools that exploit a specific human-exception-channel failure mode.
- [x] Narrator stays as lens; no first-person memoir framing.
- [x] POV (third-person observer), tense (past for vignette, present for analysis), and register (analytical with vignette grounding) consistent throughout.
- [x] Concepts used correctly: hyper-personalization, voice cloning, conversational extortion bots, identity compromise, session-cookie theft, MFA bypass via exception channel.
- [x] One explicit cross-chapter pointer ("The next chapter takes this layer's logic into the post-compromise phase…") in the closing — within the cap. Verified by regex scan.
- [x] Prior-chapter resonance (access economy, AI thread, operator-time compression) handled thematically without pointer text.
- **Issues:** none.

### 3. Accuracy vs. Source Reports
- [x] Every factual claim aligns with Report #2 or Report #3.
- [x] No hallucinated statistics: the chapter does not invent percentages or dollar figures. Zscaler ThreatLabz, Trend Micro forecasts are correctly framed as forecasts.
- [x] No invented threat actors. No named real victim company.
- [x] Vignette uses only documented mechanics: voice cloning from public audio (Report #3), infostealer-log-derived verification data (Report #2), MFA reset via help-desk exception channel (Report #3 deepfake-enabled help-desk fraud).
- [x] The "executive's household device" expansion of the infostealer harvest path is grounded in Report #2's broad-spectrum infostealer-distribution framing ("cracked software, phishing pages, public code repositories, fake CAPTCHA pages") and the general logic of how household credentials reach corporate identity systems.
- [x] The "cloned-voice executive call during negotiation" detail is grounded in the report's combined description of voice cloning and AI-managed negotiation as parts of the same operational pipeline.
- **Issues:** none.

### 4. Source Routing Check
- [x] Chapter prompt listed exactly two required files: Report #3 and Report #2. Both were read before drafting.
- [x] No unlisted report (Reports #1, #4, #5) is invoked. No data points, named actors, or capabilities from those reports appear.
- [x] Factual claims traceable to Report #2 or Report #3.
- [x] Source-use sidecar saved at `chapter_07_sources.md` listing files read and main facts used.
- **Issues:** none.

### 5. Production Formatting Rules
- [x] One heading only: `# Chapter 7: The Voice on the Phone`.
- [x] No `##` or `###` subheadings in the body. (Verified: 0 matches.)
- [x] No horizontal rules. (0 matches.)
- [x] No italic subtitle line.
- [x] No citation markers. (0 matches.)
- [x] No bold body prose. (0 matches.)
- [x] No italics in body prose. (0 matches.)
- [x] Paragraph spacing clean: no triple blank lines, no decorative separators.
- **Issues:** none.

### 6. Structure, Flow, and Style
- [x] Logical progression from the help-desk vignette through the persona-simulation pipeline, voice/video layer, deepfake help-desk fraud, access-economy connection, extortion bots, defensive-shift argument, and the personal-life angle.
- [x] Transitions organic, not labeled.
- [x] Opening (help-desk technician on Tuesday morning) is earned, tactile, and consequential.
- [x] Closing bookend (the help-desk technician's post-incident interview) provides closure; final paragraph pivots cleanly to Ch 8's negotiation-desk subject.
- [x] Paragraph and sentence variety: some short punchy lines ("The voice on the phone is the application of that read."), some long analytical paragraphs. No monotonous rhythm.
- [x] Technical concepts (voice cloning, session cookie binding, conditional access, continuous access evaluation) explained through operational context rather than metaphor stacking.
- [x] Avoids cyber-war clichés, moral grandstanding, melodrama. The "voice on the phone is the front door of the access economy" framing is the chapter's central translation device and is used precisely.
- **Issues:** none.

### 7. Depth and Proportion
- [x] Chapter covers required material with depth appropriate to its role as the social-engineering narrowing of the AI thread.
- [x] No section feels thin or padded. The personal-life paragraph (extending the threat to readers' parents, children, professional inboxes) lands the "so what?" without sensationalism.
- [x] Stops at a natural editorial endpoint with a clean handoff to Ch 8.
- [x] Word count is approximately 4,010, below the ~5,000 target. The chapter exhausts the source material's voice-and-social-engineering content from Reports #2 and #3 without padding. Adding 1,000 words to hit the target would either dilute the argument or drift into Ch 8 territory (negotiation desk specifics). Holding at present length per the self-review template's explicit guidance that word count itself is not an issue if depth and proportion are sound.
- **Issues:** none.

## Revision Pass

One automatic revision pass was performed mid-self-review: six explicit cross-chapter pointer references in the first draft ("the previous chapter," "the wholesalers' chapter") were rewritten as thematic recurrence without pointer text. The final draft contains exactly one explicit cross-chapter pointer ("The next chapter") at the closing, within the chapter prompt's "maximum one explicit reference" cap.

## Verdict

**Overall Assessment:** Chapter 7 is production-ready. It hits every "Must Cover" point, narrows Chapter 6's AI thread cleanly onto the identity-and-trust surface, anchors itself in a tangible help-desk vignette built only from Report #2 and Report #3 mechanics, calibrates the AI augmentation claim conservatively, lands the access-economy connection as a complementary-rather-than-replacement path, and closes on the strongest claim of the chapter — that traditional user-awareness training has become a category error against AI-augmented social engineering — without overreaching the source evidence. Formatting is clean. Source routing is disciplined.

### Issues Found: 0

### Recommended Action
- [x] Approve after automatic revision.
- [ ] Minor unresolved issue — note but do not block.
- [ ] Major unresolved issue — block for human review with exact problem summary.
