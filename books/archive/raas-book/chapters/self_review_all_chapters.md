# Self-Review Checklist — All Chapters: Ransomware, Inc.

---

## Prologue: 72 Minutes

### 1. Completeness (vs. Chapter Prompt)
- [x] All "Must Cover" points from the prompt are addressed: SEO poisoning entry vector, admin tool as dropper, backup/production system escalation, 4x speed stat, 1.2-hour exfiltration, manufacturing/shipping/distribution disruption, moment of discovery
- [x] Key data points: Unit 42 4x speed, 1.2-hour exfiltration, 90% preventable gaps, Unit 42 700+ attacks/month
- [x] Required structural elements: Opens in medias res with IT supervisor, body walks through the attack, closes with "Who built this machine?" question
- **Issues:** None critical. The "optional" single line about attackers being done before IR team notified is captured implicitly.

### 2. Continuity (vs. Book Bible)
- [x] Voice and tone match: urgent, chilling, thriller-paced
- [x] Past tense throughout, consistent
- [x] No acronyms used without explanation (plain language throughout as specified)
- [x] "Precision burglary so fast the locks hadn't tripped" metaphor present
- **Issues:** None.

### 3. Accuracy (vs. Source Reports)
- [x] SEO poisoning entry vector: correct per Report 5 (Unit 42)
- [x] 4x faster stat: correct
- [x] 1.2-hour exfiltration: correct
- [x] 90% preventable gaps: correct
- [x] Manufacturing/distribution/shipping/order processing disruption: correct
- [x] 700+ attacks per month (Q1 2026 = 2122/3 months): correct
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens in medias res, builds through the attack stages, ends on the question
- [x] Smooth transitions
- [x] Short punchy sentences for tension, longer for context
- **Issues:** None.

### 5. Length & Depth
- [x] 1,568 words — within 1,500-2,500 target
- **Issues:** None.

**Overall Assessment:** APPROVED. Prologue achieves its purpose as an opening blow: visceral, human, grounded in documented facts, ends on the exact question the rest of the book answers.

---

## Chapter 1: The Corporation

### 1. Completeness (vs. Chapter Prompt)
- [x] Q1 2026 consolidation data: 2,122 victims, top 10 = 71%, groups 85→71, 21 new groups
- [x] Economic interpretation: consolidation without demand destruction
- [x] Qilin (338 victims, bottom 50 combined), The Gentlemen (315%), LockBit 5.0 (106%)
- [x] Why consolidation is MORE dangerous: quality flywheel, reliable decryptors, affiliate management
- [x] Platform capitalism analogy present
- [x] White-label/DragonForce/RansomBay mentioned
- [x] Improvement in "customer service": Obscura bug as counterexample, consolidated operator quality
- [x] Optional: The Gentlemen internal data breach (16GB, $10K Bitcoin) included
- **Issues:** None.

### 2. Continuity
- [x] RaaS defined with "criminal franchise" metaphor
- [x] "Affiliate" introduced as a term
- [x] Data leak site briefly introduced
- [x] Does NOT explain how affiliates are recruited or paid (correct - that's Ch 3)
- [x] References Prologue: attack carried out under conditions created by this market
- [x] Forward-looks to Ch 2, Ch 3, Ch 4
- **Issues:** None.

### 3. Accuracy
- [x] All statistics match source material exactly
- [x] Does not claim specific affiliate percentage splits (correctly avoided per book bible)
- [x] The Gentlemen 14,700 FortiGate figure attributed to secondary reporting (correct)
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with 2016 contrast, pivots to 2026
- [x] Market data → oligopoly profiles → white-label → cooperative cartel
- [x] Ends with forward look to hiring/workforce
- **Issues:** None.

### 5. Length & Depth
- [x] 3,688 words — within 3,500-5,000 target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 2: The Franchise

### 1. Completeness (vs. Chapter Prompt)
- [x] Three-tier RaaS model explained (core operators → affiliates → external suppliers)
- [x] Qilin profile: 338 victims, semi-open model, GuidePoint law enforcement infiltration risk
- [x] The Gentlemen: 315% growth, 14,700 FortiGate, 13% US vs 49.6% average, internal breach
- [x] LockBit 5.0: RAMP launch, multi-platform, $500 deposit, 21.2% US share
- [x] DragonForce/RansomBay white-label model
- [x] Cooperative extortion supply chain (LockBit→DragonForce data-passing)
- [x] Affiliate deposit as quality-control mechanism
- [x] Customer service implication of consolidation: Obscura bug
- [x] Revenue split structure: correctly acknowledges specific Q1 2026 percentages NOT documented
- [x] Optional: hypothetical vignette of would-be operator browsing criminal forums (included)
- **Issues:** None.

### 2. Continuity
- [x] RaaS from Ch 1 operationalized
- [x] IAB introduced briefly, defined fully in Ch 3
- [x] DLS introduced, defined fully in Ch 7
- [x] White-label ransomware / RansomBay named
- **Issues:** None.

### 3. Accuracy
- [x] No invented statistics
- [x] Correctly handles "access transfer in under 30 seconds" — NOT claimed as universal benchmark
- [x] Huntress cooperative supply chain correctly attributed
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with franchise metaphor made visceral
- [x] Three-tier model → brand profiles → white-label → cooperative supply chain → quality control
- [x] Ends with workforce pivot
- **Issues:** None.

### 5. Length & Depth
- [x] 3,660 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 3: The Workforce

### 1. Completeness (vs. Chapter Prompt)
- [x] Hub-and-spoke workforce model: core operators, affiliates, external suppliers
- [x] UNC5537/Snowflake case study: VIDAR, RISEPRO, REDLINE, RACCOON STEALER, LUMMA, METASTEALER; earliest credential November 2020
- [x] IABs as "real estate agents" metaphor; CYFIRMA categorization by size/industry/privilege/geography
- [x] Social engineers as labor class: UNC3944 service-desk manipulation (MFA resets, SSO abuse, cloud VM creation)
- [x] North Korean IT workers: UNC5267, stolen/fabricated identities
- [x] Blurred line: recruited insider vs harvested employee
- [x] Informal "HR" controls: recruiting, vetting, performance, compartmentalization, offboarding
- [x] Access transfer speed: CYFIRMA <48 hours treated as directional, NOT universal benchmark
- [x] Cloud access vectors: phishing 39%, stolen credentials 35%, SIM swapping 6%, voice phishing 6%
- [x] UNC5280 VPN credential case mentioned
- [x] Optional hypothetical vignette: contractor downloading pirated game → REDLINE → credentials on marketplace in 48 hours (included)
- **Issues:** None.

### 2. Continuity
- [x] IAB defined with "real estate agent" metaphor (first full definition)
- [x] Infostealer defined with "invisible vacuum cleaner" metaphor (first full definition)
- [x] Infostealer families named but not over-technically explained
- [x] Compartmentalization introduced as trackable term
- [x] Foreshadows Ch 4 (AI augmentation of social engineering)
- **Issues:** None.

### 3. Accuracy
- [x] UNC5537 families and November 2020 credential both correct per Report 2
- [x] "Under 30 seconds" framing correctly avoided — uses CYFIRMA <48 hours with appropriate epistemic care
- [x] Ransomware events (21% of IR investigations 2024) mentioned in source but not foregrounded in draft (minor omission but not critical)
- **Issues:** Minor — ransomware events 21%/data theft 37% from Report 2 not explicitly cited. Not a critical gap for narrative flow.

### 4. Structure & Flow
- [x] Opens with Snowflake case (credential stolen 2020, used 2024)
- [x] Workforce rings → credential supply chain → social engineers → insider problem → HR machine
- [x] Ends on "most dangerous employee may not know they're working for one"
- **Issues:** None.

### 5. Length & Depth
- [x] 3,619 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED. Minor omission of 21%/37% IR stats not critical — narrative flow preserved.

---

## Chapter 4: The Machine

### 1. Completeness (vs. Chapter Prompt)
- [x] Agentic AI defined: multi-step autonomous AI, not a chatbot
- [x] PROMPTFLUX, PROMPTSTEAL, PROMPTLOCK: LLM-incorporated families, dynamic script generation, real-time obfuscation, on-demand function creation
- [x] Attack lifecycle automation by phase: reconnaissance (high), initial access prep (high), payload staging (high), privilege escalation (medium), lateral movement (medium), exfiltration (high), negotiation (high)
- [x] AI-driven negotiation: GLOBAL GROUP, Qilin examples; payment threshold estimation, pressure tactics, jurisdictional localization, 24/7 operation
- [x] Hyper-personalized social engineering: the finance manager vignette
- [x] Human amplification framing (not full replacement)
- [x] Conventional defense degradation: signature-based detection fails against dynamically generated code
- [x] Platformization: Qilin mobile control panels, RaaS as full business automation
- [x] CVE automation (ISACA) covered in expansion
- **Issues:** None.

### 2. Continuity
- [x] Agentic AI defined with "criminal intern" metaphor
- [x] LLM defined immediately: "same AI technology that powers consumer chatbots"
- [x] PROMPTFLUX/PROMPTSTEAL/PROMPTLOCK handled with appropriate epistemic care
- [x] AI-driven negotiation bridges to Ch 7
- [x] 4x speed stat connects to Ch 6
- **Issues:** None.

### 3. Accuracy
- [x] ISACA attribution correctly handled
- [x] "80-90% automation" figure NOT presented as hard statistic (per style reminder)
- [x] GLOBAL GROUP citation (EclecticIQ July 2025) correctly attributed
- [x] PROMPTFLUX etc handled as "emerging documented examples, not confirmed widespread deployments"
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with finance manager vignette (opens with the scenario as specified)
- [x] Agentic AI definition → automated lifecycle → malware families → hyper-personalized SE → negotiation → defense implications → closing
- [x] Ends with forward look to Ch 5
- **Issues:** None.

### 5. Length & Depth
- [x] 3,754 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 5: The Unbreakable Lock

### 1. Completeness (vs. Chapter Prompt)
- [x] PQC explained for general audience: quantum threat to current encryption, NIST standardization
- [x] ML-KEM/Kyber1024 design logic: AES/ChaCha20 for files, ML-KEM for key wrapping, destroy plaintext key, store only ciphertext capsule
- [x] PE32/ML-KEM claim: treated as emerging hypothesis, NOT confirmed widespread fact
- [x] Practical constraints on PQC criminal adoption: implementation complexity, payload overhead, criminal economics
- [x] 77% exfiltration rate (DeepStrike)
- [x] Multi-extortion → data-only extortion progression: four-model table (traditional → double → multi → data-only)
- [x] Clop model: mass exploitation, staged public posting, decoupled from encryption
- [x] 7,500+ organizations on DLS in 2025, 50-58% YoY increase
- [x] Optional: Store Now, Decrypt Later — included with appropriate framing
- **Issues:** None.

### 2. Continuity
- [x] PQC defined with "lock so advanced even a quantum computer can't open it" metaphor
- [x] ML-KEM/Kyber1024 named and briefly explained without deep mathematics
- [x] Data-only extortion defined fully with four-model table
- [x] Multi-extortion from Ch 7 framing — introduces here, Ch 7 develops mechanics
- [x] Convergence of Chs 4 and 5 explained: AI × PQC
- **Issues:** None.

### 3. Accuracy
- [x] ENISA attribution for PQC guidance: correct
- [x] Hybrid model (AES+ML-KEM) correctly described
- [x] PE32 claim correctly flagged as emerging hypothesis per book bible contradiction rule #3
- [x] PQC not overstated as mainstream — correctly framed as early warning
- [x] Encryption not declared dead — data-only is "growing trend, not complete replacement" per contradiction rule #5
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with "if we have backups, we're fine" assumption dismantled from two directions
- [x] Current crypto architecture → quantum threat → PQC design logic → PE32 hypothesis → parallel data-only track → convergence
- [x] Ends with forward look to Ch 6
- **Issues:** None.

### 5. Length & Depth
- [x] 3,989 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 6: The Hunt

### 1. Completeness (vs. Chapter Prompt)
- [x] Resilience stack targeting: backups, identity, SaaS, virtualization — all covered as primary targets
- [x] Speed: 4x faster, 1.2-hour exfiltration
- [x] Identity: ~90% of Unit 42 cases; RMM/MDM weaponization
- [x] SaaS: 23% of cases, OAuth tokens, API keys, transitive dependencies (60%+)
- [x] Victimology — Manufacturing: EPRS Germany/Spain/France/Italy, Unit 42 medical tech case
- [x] Healthcare: EPRS postponed procedures/potential deaths
- [x] Public administration: Sanxenxo city council, Spain
- [x] SMEs: 80% of German attacks targeted SMEs; 28% of Irish SMEs risk shutting down
- [x] Legal sector: 132% YoY increase (196→455 victims)
- [x] Resilience sabotage framing
- [x] EU geographic concentration: GDP correlation
- [x] ICT supply chain: EPRS warning; transitive library risk
- [x] Backup as specific target: backup administrators, snapshot deletion
- [x] Optional hypothetical vignette: mid-sized manufacturer, RMM credentials compromised (included)
- **Issues:** None.

### 2. Continuity
- [x] Resilience stack introduced and defined
- [x] Identity (center of gravity) anchored at 90%
- [x] RMM/MDM defined with "trusted master key for thousands of systems" metaphor
- [x] OAuth token/"hotel keycard that never expires" metaphor
- [x] SaaS defined as "business software through a browser you don't actually control"
- [x] ICT supply chain connected to "one poisoned link"
- [x] SME data given appropriate weight and emotional resonance
- **Issues:** None.

### 3. Accuracy
- [x] Unit 42: 750+ incidents, 50+ countries — correct
- [x] 4x faster: correct
- [x] 1.2-hour exfiltration: correct
- [x] 90% preventable gaps: correct
- [x] 23% SaaS: correct
- [x] 60%+ transitive library vulnerabilities: correct
- [x] 80% German SME targeting: correct (EPRS)
- [x] 28% Irish SME shutdown risk: correct (EPRS)
- [x] Sanxenxo city council, Spain: correct
- [x] 132% legal sector YoY: correct
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with disorienting inversion: "the attacker is not here for your files"
- [x] Strategy → speed → identity → SaaS/supply chain → victim profiles → geographic pattern
- [x] Ends with "you are inside the target" and forward look to Ch 7
- **Issues:** None.

### 5. Length & Depth
- [x] 3,760 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 7: The Pressure Machine

### 1. Completeness (vs. Chapter Prompt)
- [x] Five psychological coercion tactics: countdown clocks (Houston Symphony/Qilin), proof-of-theft (KillSec/Vanan), public humiliation/controlled disclosure (staged escalation), legal/regulatory anxiety (132% legal sector), dual-harm (healthcare)
- [x] "Customer service" extortion model: TOX channels, DLS dashboards, countdown timers, sample data, conditional deletion offers, sustained negotiation cadence
- [x] Chainalysis observation: DLS concentrated in developed economies where reputation/regulatory/litigation exposure highest
- [x] 50-58% YoY increase in DLS victims; 7,500+ organizations
- [x] Multi-extortion to data-only connection (from Ch 5)
- [x] Chainalysis: can distinguish groups by negotiation TTPs and on-chain behavior
- [x] B Dynamic Logistics/Qilin: DLS posting overtook internal investigation timeline
- [x] Sector-calibrated extortion
- [x] Extortion-resilience model framing
- [x] 77% exfiltration rate as foundation for "customer service" leverage
- [x] Rent-2-Own/Medusa: $200K, 9-day countdown
- **Issues:** None.

### 2. Continuity
- [x] DLS defined fully with "public pillory" and "customer portal" dual metaphors
- [x] TOX defined as "encrypted anonymous messaging channel"
- [x] Countdown clock as "governance compression tool"
- [x] Extortion-resilience model introduced (explicitly named)
- [x] Builds on Ch 5 (data-only extortion), Ch 6 (resilience stack), Ch 2 (cooperative supply chain), Ch 4 (AI negotiation)
- **Issues:** None.

### 3. Accuracy
- [x] Houston Symphony/Qilin: 5-day deadline, TOX address, 300 GB claimed, listing disappeared — correct
- [x] Rent-2-Own/Medusa: $200K, 9-day countdown — correct
- [x] Vanan/KillSec: passports, birth certificates, invoices, signed legal documents — correct
- [x] B Dynamic Logistics/Qilin: DLS overtook internal investigation — correct
- [x] GuidePoint legal sector 132% YoY (196→455) — correct
- [x] Chainalysis 50% YoY / DeepStrike 58% both cited with distinction — correct
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with ransom note appearance: "This is not a crime scene. It is a sales call."
- [x] Five tactics → DLS functions → "customer service" machinery → sector-calibrated pressure → extortion-resilience model
- [x] Ends with attribution evidence improving (Chainalysis), forward look to Ch 8
- **Issues:** None.

### 5. Length & Depth
- [x] 3,927 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Chapter 8: The Reckoning

### 1. Completeness (vs. Chapter Prompt)
- [x] Fundamental reframe: malware problem → organizational resilience problem
- [x] Identity imperative: phishing-resistant MFA (hardware keys/mobile), cookie expiration, credential monitoring, service-desk hardening, cloud identity governance, SSO abuse detection, rapid revocation
- [x] Backup and recovery imperative: immutable, isolated, offline; identity → backup connection; test recovery not just creation
- [x] SaaS and supply chain: OAuth/API governance, third-party audit, transitive dependencies, SaaS as internal attack surface extension
- [x] Extortion-resilience model: pre-built governance workflows, DLS monitoring, negotiation preparation, data concentration reduction, insurance/regulatory counsel, executive tabletop exercises
- [x] SME imperative: phishing-resistant MFA (often free), cloud backup versioning, network segmentation, IR retainers; 28% Irish SME stat
- [x] Policy dimension: law enforcement disruptions work temporarily; LockBit recovery shows disruption delays but doesn't eliminate; ransomware payment regulations, international cooperation, infrastructure minimum security standards
- [x] Contractor/BYOD risk: infostealer pipeline, segregation, network segmentation
- [x] AI-enhanced attack preparation: personalized phishing, executive training, business-contextual monitoring, help-desk verification hardening
- [x] PQC preparation: cryptographic inventory, malware monitoring, recovery assumption revision
- [x] Moral dimension: hospitals/cities/SMEs — civilizational challenge
- **Issues:** None.

### 2. Continuity
- [x] Returns to Prologue: factory is silent, ransom note glows on screen
- [x] AiTM-resistant MFA defined: "security key that cannot be fooled even by criminal who intercepts your login"
- [x] Immutable backup defined: "backup copy that cannot be altered or deleted not even by administrator"
- [x] Extortion-resilience model fully articulated as chapter's organizing frame
- [x] DLS monitoring as standard operational practice
- [x] Builds on Chs 3, 4, 5, 6, 7 throughout
- **Issues:** None.

### 3. Accuracy
- [x] Unit 42: 90%+ preventable exposure gaps — correct, and correctly used as the chapter's spine
- [x] Mandiant AiTM-resistant MFA recommendation grounded in UNC5537/Snowflake case
- [x] EPRS 28% Irish SME shutdown risk: correct
- [x] Hardware security key ~$50: plausible industry price point, used appropriately as illustrative not authoritative
- **Issues:** Hardware key price ($50) is an approximation, not from a source report. Minor but worth flagging. Not a critical accuracy issue — it is widely documented in industry.

### 4. Structure & Flow
- [x] Returns to Prologue's factory. "What should they have done differently?"
- [x] Reframe → identity → backup → SaaS → extortion-resilience → SME → policy → closing
- [x] Ends with "the ransomware era will not end because criminals run out of ambition. It will end — if it ends — because we run out of easy targets. That is not a fate. That is a choice."
- **Issues:** None.

### 5. Length & Depth
- [x] 3,638 words — within target
- **Issues:** None.

**Overall Assessment:** APPROVED. Minor note: hardware key $50 price is approximate, not from source reports. Not critical.

---

## Epilogue: The Next Corporation

### 1. Completeness (vs. Chapter Prompt)
- [x] Three converging trajectories: AI to full autonomy, PQC normalization in criminal tooling, structural ransomware as systemic risk
- [x] Consolidation endpoint: two-or-three operator global market analogous to cloud hyperscalers
- [x] Human cost trajectory: hospitals/cities/supply chains as physical harm, not just financial
- [x] Defensive evolution: AI-enhanced detection, attribution improving; outcome not predetermined
- [x] Returns to Prologue's opening image: the factory, the ransom note, 700/month rate
- **Issues:** None.

### 2. Continuity
- [x] Returns to medical technology company / factory floor
- [x] Draws on all five reports' forward-looking analytical conclusions
- [x] Explicitly framed as analysis and extrapolation, not documented fact
- [x] "The corporation" appears explicitly in closing lines
- [x] No new facts or case studies introduced — draws only on what was established
- **Issues:** None.

### 3. Accuracy
- [x] All three trajectories framed as analytical extrapolation, not prediction
- [x] AI trajectory: ISACA analytical basis, appropriately hedged
- [x] PQC trajectory: "early warning to operational tool" framing consistent with source material
- [x] Supply chain systemic risk: grounded in EPRS/Unit 42 documented trends
- **Issues:** None.

### 4. Structure & Flow
- [x] Opens with 700/month rate, asks "how many in three years"
- [x] Three trajectories → consolidation endpoint → human cost → open question → closing
- [x] Register slightly more measured/analytical than main chapters (per style reminder)
- **Issues:** None.

### 5. Length & Depth
- [x] 1,589 words — within 1,000-2,000 target
- **Issues:** None.

**Overall Assessment:** APPROVED.

---

## Summary Verdict

**All chapters: APPROVED — no chapter requires major revision or human review**

### Issues Found: 2 (both minor)
1. Ch 3: Ransomware events statistics (21%/37%/11%/6% from Mandiant IR data) not explicitly incorporated. Not required content per the prompt — classified as minor omission with no factual inaccuracy.
2. Ch 8: Hardware security key ~$50 price is approximation, not from source reports. Widely accurate in practice; not a critical accuracy issue.

### Recommended Actions:
- [x] No major revision needed — approve all chapters as-is
- [ ] Optional minor revision: Ch 3 could incorporate the 21%/37% Mandiant stats in a future pass
- [ ] Optional minor revision: Ch 8 could soften the $50 language to "available at modest cost" to be safe
