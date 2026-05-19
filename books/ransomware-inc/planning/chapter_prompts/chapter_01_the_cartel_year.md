# Chapter 1: The Cartel Year

## Core Question
What does it mean that 71% of global ransomware victims now come from ten companies that don't legally exist?

## Purpose in the Book
This is the opening chapter. It sets the central frame of the book: ransomware in 2026 is no longer a chaotic gang phenomenon — it is a consolidating industry. The chapter must convince the reader that the right mental model is a market, not a malware family, and must seed the platform/affiliate vocabulary the rest of the book builds on. It introduces the reader to the dominant brands of 2026 (Qilin, Akira, LockBit 5.0, The Gentlemen, DragonForce) as competing platforms, not as cartoon villains.

## Required Content

### Must Cover
- The Q1 2026 concentration shot: 2,122 organizations posted to leak sites, top 10 groups accounting for ~71% of victims, the top four (Qilin, Akira, The Gentlemen, LockBit) representing 41%. Translate these numbers so the reader feels what concentration looks like.
- Qilin's position as the most active operation for the third consecutive quarter with 338 posted victims — and the framing that Qilin alone outpaced the combined output of the bottom 50 groups.
- The Gentlemen's breakout: from 40 posted victims in Q4 2025 to 166 in Q1 2026.
- LockBit's return: post-Operation Cronos disruption, the September 2025 LockBit 5.0 relaunch, 163 Q1 2026 victims.
- The "creative destruction" pattern: disruption removes brands but rarely removes capacity, because affiliates, infrastructure, and access supply reaggregate around surviving operators. Use the RansomHub collapse → migration to other RaaS offerings as the worked example.
- The strategic argument that ransomware should now be understood as a platform economy: brands, payments, infrastructure, affiliate governance — not a malware category.

### Should Include
- A grounded opening vignette — e.g., an IT director at a mid-sized manufacturer watching their company's name appear on a leak site countdown clock. Use only attack mechanics described in Report #1 or Report #4.
- The high-level "encryption is one option among many" data: encryption present in 78% of 2025 cases (down from 92% in 2024, 96% in 2021), data theft in 57%, harassment in 10%. This seeds the multi-extortion theme that returns in Chapter 8.
- A note on the volume convergence across vendors (Check Point, Broadcom/Symantec, Cyble, GuidePoint) so the reader trusts the numbers.
- The handful of cautions: leak-site victim counts are not a complete incident census; high victim volume does not always mean high revenue (GuidePoint observation about Qilin's payment rates).

### Optional (if it fits naturally)
- A brief, sober mention of the 21 new groups that emerged in Q1 2026 but mostly posted fewer than 10 victims — the long tail that never breaks through.

## Source Material Focus

Primary sources for this chapter:
- **Report #1:** Q1 2026 RaaS market structure, concentration metrics, dominant operator victim counts, affiliate migration after disruption.
- **Report #4:** Volume convergence (7,960 leak-site listings in 2025, +53% YoY); confirmation of 2,122 Q1 2026 figure; Unit 42 78%/57%/10% encryption/theft/harassment breakdown.

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779005211_949b8650bc.md`
- `books/ransomware-inc/reports/task_1779012482_285007975a.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points, quotes, or findings to incorporate:
- 2,122 organizations listed on leak sites in Q1 2026; second-highest Q1 on record.
- Top 10 groups: 71% of victims (up from 57% in Q3 2025).
- Qilin, Akira, The Gentlemen, LockBit collectively: 41%.
- Qilin: 338 Q1 2026 victims; "outpaced the combined output of the bottom 50 groups."
- The Gentlemen: 40 → 166 victims quarter over quarter.
- LockBit: 163 Q1 2026 victims under LockBit 5.0; post-Operation Cronos recovery.
- Broadcom/Symantec: 6,182 extortion attacks in 2025, +23% over 2024.
- Cyble: ~6,500 incidents in 2025; identity compromise overtook vulnerability exploitation as dominant initial-access route.
- Unit 42: encryption in 78% of 2025 cases (vs. 92% in 2024, 96% in 2021); data theft 57%; harassment 10%; 86% of incidents involved business disruption.

## Structural Requirements

### Opening
Open with a grounded human scene: a single victim discovering they have been posted to a leak site. Establish the moment, then immediately widen out to show that this is one event in a market that posted more than 2,000 such organizations in three months.

### Body Flow
1. The opening scene and the immediate "this is happening in volume" reveal → transition into the structural picture.
2. The concentration story (top 10 = 71%; top 4 = 41%; Qilin's individual dominance) → transition into how this market got concentrated.
3. The creative-destruction dynamic: RansomHub collapse, affiliate migration, LockBit 5.0 return, The Gentlemen's breakout → transition into the strategic framing.
4. The strategic frame: ransomware as a platform economy, not a malware category. Plant the language ("platform," "affiliates," "brand," "service") the rest of the book will build on.

### Closing
End with revelation: the reader should now understand that takedowns alone do not reduce systemic risk, because the capability is not the brand. The capability is the labor market, the access market, and the infrastructure underneath. Set up Chapter 2's deeper dive into how those platforms operate as franchises.

## Continuity Notes

### Thematic Links (use sparingly)
- This chapter introduces the platform/affiliate concept that recurs throughout. Do not write "as later chapters will show" — let the recurrence be felt, not signposted.
- Concepts that may naturally recur: platformization, RaaS, affiliate migration, multi-extortion.

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Expected length: write to editorial completeness. Most chapters likely fall around 4,000–6,500 words, but do not pad to reach a number. If the assigned story is complete and source coverage is sufficient, concise is preferred.
- Maintain consistent POV and tense throughout.
- ONLY `# Chapter 1: The Cartel Year` as the heading — no subheadings inside the chapter body.
- No horizontal rules, no italic subtitle line, no bracketed citations.
