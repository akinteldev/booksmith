# Source Use — Chapter 6: The Agent in the Loop

## Files read
- books/ransomware-inc/reports/task_1779010243_15a209c49d.md (Report #3)

## Main facts used (Report #3)
- AI-assisted vs. agentic distinction: current evidence supports LLM use for phishing, translation, malware-development assistance, reconnaissance summarization, scripting, social-engineering personalization. 2026 forecasts extend toward multi-agent chaining across reconnaissance, vulnerability discovery, credential attacks, payload adaptation, lateral movement, exfiltration — explicitly framed as forecast, not confirmed current state.
- Modular extortion architecture: encryption, exfiltration, identity abuse, disruption as composable components rather than single "encrypt everything" payload.
- Operator-time compression as central operational consequence.
- FinCEN: U.S. ransomware payments ~$2.1 billion across 2022-2024; payments declined from 2023 peak but pool sustains automation investment.
- Trend Micro 2026 outlook: faster and more persistent automated ransomware.
- ITBrief 2026 forecast: fully automated cybercrime.
- Zscaler ThreatLabz 2026 forecasts: AI-managed victim identification, automated exploit selection, AI-assisted negotiation; voice-based social engineering as parallel major vector.
- The careful framing throughout: AI as augmentation, not substitution; agentic-chaining as forecast, not universal current state.

## Reports NOT used
- Reports #1, #2, #4, #5 — not invoked. Mid-draft contained two cross-Report leaks (Cisco Talos 50%→18% pre-ransomware stat from Report #2 and Anubis investigative-article reference from Report #1); both removed in the revision pass.

## Hypothetical Vignette
- Opening: an affiliate running seven concurrent intrusions with an AI chat-window assistant for target prioritization, data-triage, exploit selection, and regulatory-leverage analysis. Closes with the same character at end of Tuesday having advanced 4/7 intrusions and processed 40TB of exfiltrated data with model assistance. Illustrates only documented mechanics from Report #3: AI-assisted reconnaissance, data triage, exfiltration prioritization, negotiation-message drafting. No invented capabilities, no specific company named.
- The affiliate's use of a "model" is presented as augmentation throughout; the model is not portrayed as autonomously executing the intrusion.

## Cross-chapter references
- ONE explicit reference: closing paragraph naming "The next chapter" pointing to Ch 7 (voice/social-engineering AI). Within the one-explicit-reference cap.
- All other inter-chapter resonance handled thematically without pointer text. The hospital/manufacturer/backup-admin vignettes from earlier chapters are referenced implicitly as "Most ransomware stories describe consequences that an ordinary person can see" — meta-framing about ransomware coverage in general, not chapter-pointer text.

## Source-routing fixes during revision
- Removed Cisco Talos 50%→18% pre-ransomware figure (originates from Report #2 via Lyrie; used in Ch 3). Replaced with general framing about pre-ransomware detection shrinking across recent incident-response reporting.
- Removed Anubis "investigative-article" comparison (originates from Report #1; used in Ch 2). Replaced with a non-attributed reference to platforms investing in automated data-triage services.

## Calibration discipline
- The chapter explicitly states the augmentation-vs-autonomy distinction multiple times.
- Forecasts (Trend Micro, ITBrief, Zscaler ThreatLabz) are framed as forecasts, not as current confirmed state.
- The "fully autonomous attack agents" framing is explicitly identified as one of two errors the chapter is calibrating against.
