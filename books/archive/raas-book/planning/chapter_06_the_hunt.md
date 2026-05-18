# Chapter 6: The Hunt

## Subtitle
Strategic Targeting and the Resilience Stack

## Core Question
Why are ransomware operators no longer simply locking files — why are they specifically targeting the systems that would allow a victim to recover, and who are the preferred victims in 2026?

## Purpose in the Book
Chapter 6 is the victimology and targeting strategy chapter. It answers the questions every reader is silently asking: "Could this happen to me? To my employer? To my hospital or city council?" The answer, supported by Unit 42's 2026 Global IR Report and the European Parliamentary Research Service data, is: almost certainly yes — and the attackers have specifically engineered their campaigns to ensure that when the blow lands, you cannot get back up without paying. This chapter introduces the "resilience stack" as the true target of modern ransomware: backups, identity services, SaaS platforms, and virtualization layers. It also profiles the primary victim demographics: manufacturing, healthcare, municipalities, and SMEs.

---

## Required Content

### Must Cover
- The strategic shift from endpoint disruption to resilience denial: ransomware operators now target systems that enable recovery — backup infrastructure, identity and access services, virtualization/management planes, SaaS repositories, third-party provider connections. If these systems fall, the victim cannot recover without paying regardless of how good their endpoint security is.
- The speed of modern attacks: Unit 42's 2026 dataset (750+ major incidents, 50+ countries): attacks are 4x faster than before; the fastest intrusions reached data exfiltration in as little as 1.2 hours. The implication: defenders who might have had days or hours to respond now have minutes or seconds. If identity abuse and automation are already in play, the opportunity for orderly triage is gone.
- Identity as the center of gravity: identity loopholes drove nearly 90% of Unit 42's investigated cases. Identity is the connective tissue that connects endpoints, cloud resources, backups, SaaS platforms, and admin consoles. Compromising identity = inheriting access to all of these simultaneously. RMM/MDM weaponization: privileged vendor tools pushed through trusted administrative channels for one-to-many command execution.
- SaaS and ICT supply chains as the new scale mechanism: 23% of Unit 42 cases involved SaaS application data. OAuth token and API key abuse blends into legitimate automation traffic. Software supply chain risk now includes transitive libraries — over 60% of cloud-native vulnerabilities reside in transitive dependencies that can execute malicious code during the build phase.
- Victimology — who is being targeted:
  - Manufacturing: most targeted sector across Germany, Spain, France, and Italy (EPRS); Unit 42 medical technology manufacturing case; GuidePoint lists manufacturing among the four most impacted industries. Why: high downtime cost, legacy OT/IT infrastructure, complex supplier dependencies.
  - Healthcare: postponed procedures and potential patient deaths (EPRS). Safety-critical operations, sensitive PHI, urgency to restore creates maximum coercive pressure.
  - Public administration/municipalities: frequent targets (EPRS). Example: Sanxenxo city council, Spain. Public pressure, citizen data, fragile local resilience.
  - SMEs: ~80% of German cyberattacks targeted SMEs in 2025 (EPRS). 28% of Irish SMEs risk shutting down after just one attack. SMEs are not soft targets — they are high-probability monetization targets with lower security maturity and stronger payment pressure.
  - Legal sector: 132% YoY increase from Report 4 (196 → 455 victims). Privileged communications + reporting obligations + client attrition risk = extreme coercion leverage.

### Should Include
- The "resilience sabotage" framing: ransomware in 2026 should be treated less as a malware problem and more as a deliberate sabotage of the victim's ability to recover independently. Defenders who focus on endpoint blocking while leaving identity, backup control planes, SaaS, and third-party trust insufficiently governed are defending the wrong layer.
- EU geographic concentration: Germany, Spain, France, Italy as the highest-victim EU countries. This correlates with GDP — attackers are economically rational, targeting large pools of digitized and monetizable organizations.
- EPRS ICT supply chain warning: compromising a single provider can yield simultaneous access to numerous integrated systems. Such attacks can have EU-wide repercussions.
- Why backup systems are specific targets: without immutable or isolated backups, encryption loses much of its coercive force. Attackers therefore target backup administrators, snapshot deletion, backup job tampering, and backup repository encryption. Backup systems are only as resilient as the identity fabric that administers them.

### Optional (if it fits naturally)
- A hypothetical vignette: a mid-sized manufacturing company. The attacker compromises the IT admin's RMM credentials. Within two hours, production lines stop, backup jobs have been corrupted, and the HR system is locked. The company has never had a ransomware drill. The operations director is calling the IT manager on his cell phone. No one knows what to do.

---

## Source Material Focus

Primary sources for this chapter:
- **Report 5 (Unit 42/EPRS Victimology):** All targeting strategy data, speed statistics, identity statistics, SaaS statistics, sector victimology, EU geographic data, SME risk data, RMM/MDM weaponization, ICT supply chain risk.
- **Report 4 (GuidePoint/Extortion Mechanics) — Secondary:** Legal sector 132% YoY increase; GuidePoint sector rankings.
- **Report 2 (Mandiant/Unit 42 HR) — Secondary:** The identity/IAB/credential theft pipeline from Ch 3 is the mechanism by which attackers access the resilience stack described in this chapter.

Key data points to incorporate:
- Unit 42 2026 Global IR Report: 750+ major incidents, 50+ countries, all major industries.
- Attacks 4x faster; fastest intrusions: exfiltration in 1.2 hours.
- Over 90% of breaches enabled by preventable exposure gaps.
- Identity loopholes drove nearly 90% of Unit 42 investigated cases.
- 23% of cases involved SaaS application data.
- Over 60% of cloud-native vulnerabilities in transitive libraries (supply chain).
- EPRS: manufacturing most targeted sector in Germany, Spain, France, Italy.
- Unit 42 case: global medical technology firm, SEO poisoning, manufacturing/distribution/shipping/order processing disrupted.
- EPRS: ~80% of German cyberattacks targeted SMEs in 2025.
- EPRS: 28% of Irish SMEs risk shutting down after one ransomware attack.
- EPRS: ICT supply chain attacks can have EU-wide repercussions.
- Sanxenxo city council, Spain — example municipality target.
- GuidePoint: manufacturing, retail/wholesale, healthcare, technology among four most impacted industries.
- Report 4: Legal sector 132% YoY increase (196 → 455 victims) — use here as one data point in the sector profile.

---

## Structural Requirements

### Opening
Open with a disorienting inversion: the attacker is not here for your files. They already have your files. What they want now is to make sure you cannot function without them — and without paying. Introduce the concept of the resilience stack as the real target.

### Body Flow
1. The strategy: from "lock your files" to "destroy your ability to recover." Explain the resilience stack (backups, identity, SaaS, virtualization) and why each layer is now a primary target.
2. The speed problem: 4x faster, 1.2 hours. When attackers already have identity access, the resilience stack can fall before a defender even knows the attacker is present.
3. Identity as the master key: 90% of cases. Walk through how identity compromise cascades — from one stolen credential or OAuth token to administrative access across the entire environment. RMM/MDM as force multipliers.
4. SaaS and supply chain: 23% of cases involve SaaS. OAuth tokens, API keys, transitive dependencies — the modern attack surface is not just your servers, it is every trusted integration.
5. The victim profiles: manufacturing, healthcare, municipalities, SMEs, legal sector. For each: why they are targeted (coercion economics), how they are compromised (sector-specific patterns), and what the human consequences look like.
6. The geographic pattern: EU concentration in Germany, Spain, France, Italy. The SME reality: most victims are not Fortune 500 companies.

### Closing
End by making the threat personal: "If you work for a small or mid-sized company, a hospital, a city council, or a law firm, you are not watching this from a distance. You are inside the target." Then forward-look: "Once the attacker has disabled your ability to recover independently, what happens next? The demand arrives. And it arrives through one of the most psychologically engineered pressure systems ever devised." Set up Chapter 7.

---

## Continuity Notes

### References to Other Chapters
- Build on: Ch 3's IAB/credential pipeline — identity loopholes in Ch 6 are fed by the infostealer ecosystem in Ch 3.
- Build on: Ch 4's AI acceleration — 4x faster attacks are enabled partly by AI-automated reconnaissance and privilege escalation.
- Build on: Ch 5's data-only extortion — the SaaS data in 23% of cases is the theft that powers non-encryption extortion.
- Foreshadow: Ch 7 (the psychological pressure that arrives after the resilience stack falls).
- Foreshadow: Ch 8 (the defensive response — identity, backup resilience, SaaS governance).

### Terms & Concepts to Use
- Resilience stack: introduce and define here — this is a new conceptual frame the reader carries into Ch 7 and Ch 8.
- Identity (the center of gravity): anchor this firmly — 90% of cases.
- RMM/MDM: define with "trusted master key for thousands of systems" metaphor.
- OAuth token / API key: define with "hotel keycard that never expires" metaphor.
- SaaS: define as "business software you access through a browser but don't actually control."
- ICT supply chain: connect to "one poisoned link that opens every door."

---

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Target length: 3,500–5,000 words.
- The SME data is the most democratizing insight in the book — it directly addresses the "this only happens to big companies" misconception. Give it appropriate weight and emotional resonance.
- Do not let the technical content of the resilience stack discussion overwhelm the human stakes. For every system, there is a person who depends on it: a patient waiting for surgery, a factory worker watching a line go silent, a city clerk unable to process any requests.
