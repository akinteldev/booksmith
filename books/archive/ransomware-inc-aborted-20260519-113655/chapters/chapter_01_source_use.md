# Source Use — Chapter 1: The Cartel Year

## Files read before drafting
- books/ransomware-inc/reports/task_1779005211_949b8650bc.md (Report #1: Check Point, Broadcom/Symantec, AhnLab, Brandefense, GuidePoint, Secure Blink, Industrial Cyber, ZeroFox, Dark Reading/ReliaQuest)
- books/ransomware-inc/reports/task_1779012482_285007975a.md (Report #4: Check Point, Unit 42, GRIT/GuidePoint, Coveware, Huntress)

## Main facts used

### From Report #1
- 2,122 leak-site victims, Q1 2026 (Check Point Research; second-highest Q1 on record).
- Top 10 brands: ~71% of Q1 2026 victims, up from 57% in Q3 2025.
- Top 4 (Qilin, Akira, The Gentlemen, LockBit) = 41% combined.
- Qilin: 338 Q1 2026 victims; first place for third consecutive quarter; "outpaced combined output of bottom 50 groups."
- Qilin 2025 monthly trajectory: ~35/mo Q1 → 150+/mo Q4; >1,000 published victims in 2025.
- The Gentlemen: 40 → 166 victims Q4 2025 → Q1 2026; ~14,700 pre-staged FortiGate devices.
- LockBit 5.0: 163 Q1 2026 victims; relaunched September 2025; cross-platform (Windows/Linux/ESXi); randomized file extensions; ~$500 BTC affiliate deposit.
- Operation Cronos disrupted LockBit in 2024; AhnLab notes LockBit fell out of top 30 in 2025 before relaunch.
- Akira: ~$244M total proceeds (Industrial Cyber); consumer goods & industrial manufacturing focus.
- Qilin affiliate split: 80% (payments ≤ $3M); 85% (>$3M).
- DragonForce: white-label model, 80% affiliate share (AhnLab; Dark Reading citing ReliaQuest).
- RansomHub: collapsed April 2025; >760 victims before disappearance; up to 90% affiliate share previously; affiliates migrated to Qilin/DragonForce/Lynx (AhnLab).
- DragonForce/LockBit/Qilin attempted cartel coalition ("equal competition conditions," "dictate market conditions") (Secure Blink); ZeroFox assessed no verifiable coordination produced yet.
- Brandefense Q1 2026: 2,135 incidents; 68 active groups; 98 countries; 50% QoQ growth.
- Active groups: Q3 2025 peak = 85; Q1 2026 = 71.
- GuidePoint full-year 2025: 124 distinct brands (46% YoY increase); 58% YoY victim increase.
- 21 new ransomware groups emerged in Q1 2026, most posting <10 victims.
- Broadcom/Symantec 2025: 6,182 extortion attacks (+23% YoY); identifies former-RansomHub affiliate migration to Qilin/Akira/DragonForce; Qilin and Akira each ~16% of claimed attacks.
- Cyble 2025: ~6,500 incidents; identity compromise overtook vulnerability exploitation as dominant initial-access route.
- GuidePoint caution: high Qilin victim volume ≠ high revenue; rigid communications/inflexible negotiations; lower payment conversion than tempo would suggest.
- Coveware (cited via GuidePoint): payment rates fell to ~23% in Q3 2025.

### From Report #4
- 7,960 leak-site listings in 2025 (+53% YoY) — Check Point.
- 2,122 Q1 2026 corroborated.
- Unit 42 longitudinal: encryption in 78% of 2025 cases (down from 92% 2024, 96% 2021); data theft in 57%; harassment in 10% (down from 13% in 2024, up from 5% in 2021); 86% of incidents involved business disruption.
- Multi-extortion / modular extortion framing (double, triple, quadruple) — used as the basis for the "pressure dials" passage.
- Modern extortion as a coercive business process; encryption as one optional lever; data exposure as stable coercive pillar.

## Reports NOT used
- Report #2 (labor market / IABs / infostealers) — reserved for Ch 3.
- Report #3 (AI / PQC / social engineering) — reserved for Ch 6, 7, 9.
- Report #5 (sectoral targeting, resilience denial) — reserved for Ch 4, 5.

## Vignette grounding
The IT director's vignette uses only Report #1 / #4 mechanics:
- leak-site posting with countdown clock (Report #1 / #4)
- pre-encryption data exfiltration as primary leverage (Report #4: 78%/57% encryption/data-theft split; modular extortion)
- multi-extortion threat to publish stolen documents (Report #4)
- SaaS-like leak-site presentation, "client" lists, discount tiers (Report #4 leak-site theater framing — deepened in Ch 8)
- Coveware ~23% payment rate as backdrop to the "she paid" outcome (Report #1 via GuidePoint)

No invented capabilities or numeric claims. The 32 GB exfiltration figure is illustrative of typical Unit 42-described case scope and is presented as scene detail, not as a source-level statistic.
