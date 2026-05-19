# Source Use — Chapter 8: The Negotiation Desk

## Files read
- books/ransomware-inc/reports/task_1779012482_285007975a.md (Report #4)

## Main facts used (Report #4)
- 7,960 ransomware-victim leak-site listings in 2025; +53% YoY (Check Point).
- 2,122 Q1 2026 leak-site posts; second-highest first-quarter total on record.
- Top 10 syndicates = 71% of global victims in Q1 2026 (CyberPress).
- Late-2025 consolidation: active leak sites fell from 84 to 77 while claimed victims rose 50% QoQ and 40% YoY (ReliaQuest).
- NordStellar transcript analysis: 256 negotiations, 11,599 individual messages, avg 47 messages per negotiation, 2020–2026 dataset.
- 25.6% of negotiations ended in payment; median 57% discount among paid victims; max single discount 96.2%.
- Discount phases: 25%–70% reductions for early engagement; upsell catalog (decryption, data deletion, proof-of-deletion, post-incident "security advice").
- $5.2M average ransom demand in H1 2024 (Dark Reading).
- $100M India Regional Cancer Center demand; $50M Synnovis demand; $25M London Drugs demand.
- Change Healthcare reported ~$22M+ payment; cascading downstream effect on US healthcare claims processing.
- $150K → $120K leaked-transcript case with law-enforcement mention (NordStellar) — used as the anchoring case study illustrating that threats and discounts run in parallel.
- Multi-extortion architecture: double (encryption + data theft), triple (customer/partner/media), quadruple (regulatory/SEC/litigation).
- SEC 2023 cybersecurity disclosure rule (Form 8-K materiality framework); ALPHV/BlackCat MeridianLink SEC complaint as the weaponization precedent.
- Harassment in 10% of Unit 42 2025 cases; selective deployment against stalled negotiations.
- BlackFog Q1 2026: data exfiltration in 96% of tracked ransomware incidents; only 1 in 9 ransomware attacks became public.
- Operation Secure (2025): 26 countries, >20,000 malicious IPs/domains, 69 infostealer variants; produced the unintended consequence of accelerating the shift toward encryptionless data-only extortion.
- Encryptionless extortion as the operationally rational post-Operation-Secure model (Broadcom/Symantec, Snakefly/Cl0p pivot).

## Reports NOT used
- Reports #1, #2, #3, #5 — not invoked. The chapter draws exclusively from Report #4 as the prompt specified.

## Hypothetical Vignette
- Opening + closing bookend: a finance director at a regional industrial manufacturer in front of a chat window with a countdown timer, sample stolen data on a leak-site preview page, an opening $7M demand reduced to $5M after three days, a "support agent" offering an additional discount for early engagement. By the end of the chapter the company pays $1.8M, declines the "data deletion proof" and "post-incident security advice" upsells, restores systems, files regulatory disclosure, never appears on the public leak site.
- The vignette uses only mechanics documented in Report #4: victim portal, countdown timer, leak-site preview, partial data sample, discount phases, customer-service tone, upsell catalog (decryption / data deletion / proof-of-deletion / security advice), regulatory disclosure dimension, the one-in-nine non-public outcome.
- No real victim company, named threat actor, or specific incident is invented for the vignette. Real cases (Change Healthcare, Synnovis, London Drugs, India Regional Cancer Center, ALPHV/BlackCat vs. MeridianLink) are cited only where they appear in Report #4.
- The harassment moment — text message containing teenage son's class schedule — illustrates Report #4's documented harassment mechanic (executive/family targeting after stalled negotiation) without inventing a specific real-world incident.

## Cross-chapter references
- ONE explicit pointer reference: closing paragraph naming "The next chapter" pointing to Ch 9 (post-quantum cryptographic frontier). Within the one-explicit-reference cap.
- All other inter-chapter resonance (platform economy, labor market, wholesalers' supply chain, recovery-trap, AI integration) is referenced thematically — "every prior phase of the operation," "the asymmetry that has run through every prior layer of the operators' machinery" — without chapter-number callouts.
- "Part III opens here" is structural framing (the Book Bible has the book in three parts: Industry / Operation / Squeeze; Ch 8 opens Part III), not a chapter pointer.

## Calibration discipline
- The chapter does NOT overstate the BlackFog one-in-nine figure or treat it as definitive; the text presents it as "BlackFog's analysis estimates" and contextualizes the working multiplier as the threat-intelligence community's estimate.
- Dollar figures ($5.2M average, $100M / $50M / $25M extremes, $22M+ Change Healthcare payment) are sourced directly to Report #4's citations.
- The NordStellar transcript statistics are presented exactly as the report frames them: 256 negotiations, 11,599 messages, avg 47, 25.6% paying, median 57% discount, max 96.2% reduction.
- The ALPHV/BlackCat SEC complaint case is framed as a precedent demonstration, not as a sustained pattern; the chapter does not claim that ransomware operators routinely file SEC complaints.
- The Operation-Secure-as-accelerator framing is grounded in Report #4's explicit observation that displaced affiliates shifted toward faster data-only extortion models requiring less operational dwell time.
