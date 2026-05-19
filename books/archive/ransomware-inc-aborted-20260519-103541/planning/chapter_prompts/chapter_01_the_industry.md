# Chapter 1: The Industry

## Core Question
What does it mean that a handful of criminal platforms now control most of the world's ransomware activity, and how did consolidation replace chaos?

## Purpose in the Book
This is the establishing chapter. It reframes ransomware from a malware story into a market story. The reader meets the industry the way a business journalist meets a sector: as a collection of dominant operators, competitive positions, supply dynamics, and price signals. By the end, the reader should understand that "ransomware" in 2026 names a consolidated criminal services market, not a swarm of independent gangs.

## Required Content

### Must Cover
- The Q1 2026 concentration signature: 2,122 victims tracked across 70+ leak sites, top 10 groups accounting for ~71% of victims, Qilin/Akira/The Gentlemen/LockBit together representing 41%.
- The specific dominant operators and their distinguishing positions: Qilin (338 Q1 2026 victims, third consecutive quarter as most active), LockBit 5.0 (163 victims after September 2025 relaunch with multi-platform Windows/Linux/ESXi targeting, randomized extensions, ~$500 BTC affiliate deposit), Akira, The Gentlemen (breakout growth from 40 victims in Q4 2025 to 166 in Q1 2026), DragonForce as a white-label cartel.
- Platformization as the central thesis: core operators provide branding, malware development, leak-site infrastructure, negotiation workflows, payment handling, and affiliate governance; affiliates provide intrusion capability and execution.
- White-label ransomware (DragonForce 80% affiliate profit share; prior RansomHub at up to 90%) as criminal franchising.
- Cartel-style coordination: DragonForce's reported coalition overtures to LockBit and Qilin, "equal competition conditions," non-aggression rhetoric.
- The post-disruption pattern: takedowns (Operation Cronos against LockBit, the RansomHub collapse) redistribute affiliate labor rather than destroying it.

### Should Include
- The 21 new groups that emerged in Q1 2026 but mostly posted fewer than 10 victims each, demonstrating that brand creation did not offset mid-tier collapse.
- The vendor-data caveat: leak-site counts are a high-confidence proxy for visible extortion activity, not a complete incident census. GuidePoint's caution that victim volume does not equal revenue.
- The Brandefense cross-check (2,135 confirmed incidents, 68 active groups, activity across 98 countries, 50% QoQ growth).

### Optional (if it fits naturally)
- The Q3 2025 → Q1 2026 contrast (top 10 share moving from 57% to 71%) as a clean before/after of the consolidation cycle.

## Source Material Focus

Primary sources for this chapter:
- **Report #1:** Q1 2026 RaaS market structure, dominant operators, white-label/cartel partnerships, affiliate economics.

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779005211_949b8650bc.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points, quotes, or findings to incorporate:
- 2,122 organizations listed across 70+ leak sites in Q1 2026 (Check Point Research).
- Top 10 groups: 71% of listed victims; Qilin/Akira/The Gentlemen/LockBit: 41%.
- Qilin: 338 victims. LockBit 5.0: 163 victims. The Gentlemen: 166 (up from 40).
- LockBit 5.0 relaunched September 2025: Windows/Linux/ESXi, randomized extensions, ~$500 BTC affiliate deposit.
- DragonForce: 80% affiliate profit share, white-label model. RansomHub: up to 90% before shutdown.
- Brandefense Q1 2026: 2,135 confirmed incidents, 68 active groups, 98 countries, 50% QoQ growth.

## Structural Requirements

### Opening
Open with a Hypothetical Vignette that establishes the industrialized nature of the threat. Suggested: a CISO at a mid-market manufacturer in the Midwest opens a Monday morning incident-response call after a weekend intrusion, and finds that the responder on the line is not surprised, not alarmed, and has already opened the relevant ransomware group's leak site in another browser tab. The reader learns alongside the CISO that this is a routine event, handled by people whose job is now routine, attacking organizations through procedures that are routine. Then widen out into the market structure.

### Body Flow
1. The vignette and the immediate reframing: ransomware as routine industrial output → transition into the Q1 2026 concentration data.
2. The numbers that prove the market story: 2,122 victims, top 10 share, the dominant operators by name and volume → transition into how platforms differ from gangs.
3. Platformization: what a RaaS platform actually provides, white-label/franchise models, affiliate economics, the cartel coordination evidence → transition into the closing revelation.

### Closing
Close with the revelation that disruption no longer maps to deterrence. The reader expected law enforcement takedowns to mean fewer victims. The data shows the opposite: fewer brands, more concentrated capacity, more victims. End by establishing that the rest of the book will walk through this industry the way a journalist walks through a company.

## Continuity Notes

### Thematic Links (use sparingly)
- This is the establishing chapter; do not reach backward. Concepts that may naturally recur in later chapters: platformization, affiliate economics, profit-sharing splits, brand alliances, disruption-driven labor reallocation.

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Target length: 4,500–5,500 words.
- Maintain consistent POV and tense throughout (third-person observational, present tense for current state, past tense for documented events).
