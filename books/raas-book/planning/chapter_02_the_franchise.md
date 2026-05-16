# Chapter 2: The Franchise

## Subtitle
Inside the RaaS Economy

## Core Question
How does the ransomware-as-a-service franchise model actually work — what do the dominant brands offer, how do affiliates operate, and what does it mean that criminals can now buy a "ready-to-run" extortion business?

## Purpose in the Book
Chapter 2 is the structural deep dive into the RaaS business model. Where Chapter 1 established the macro-economics (an industry consolidating around dominant platforms), Chapter 2 reveals the mechanics of those platforms: what the top groups actually offer, how affiliate relationships work, and how white-label ransomware is lowering barriers even further. This chapter makes the "criminal franchise" metaphor fully concrete. By the end, readers understand exactly how someone with minimal technical skill can become a ransomware operator by buying into the right platform.

---

## Required Content

### Must Cover
- The three-tier RaaS model: core operators (provide malware, infrastructure, leak sites, negotiation support, revenue processing) → affiliates (conduct intrusions, pay a percentage to operators) → external suppliers (IABs, infostealer operators, social engineers — covered more fully in Ch 3).
- Deep profiles of the three dominant brands, each illustrating a different strategic model:
  - Qilin: Volume leader. 338 victims in Q1 2026. Semi-open affiliate model. What does "openness" in an affiliate program look like and why does it matter?
  - The Gentlemen: Access-inventory model. 315% quarterly growth. Stockpile of roughly 14,700 compromised FortiGate devices. Geographic anomaly (only 13% US victims vs. 49.6% ecosystem average — followed access availability, not target prestige). The internal data breach (16+ GB, $10,000 Bitcoin listing) as evidence of organizational maturity.
  - LockBit 5.0: Brand recovery after law enforcement disruption. Multi-platform support (Windows/Linux/ESXi). Affiliate governance: ~$500 Bitcoin deposit requirement (screening + anti-fraud mechanism). Geographic diversification (US share fell from 50%+ historical to 21.2%).
- The DragonForce/RansomBay white-label model: a non-technical criminal buys fully-managed ransomware infrastructure, just as a business owner buys a franchise. The backend (malware, leak site, negotiation, revenue processing) is centralized; the brand may vary.

### Should Include
- The cooperative extortion supply chain: Huntress reporting on partnerships between LockBit, Qilin, and DragonForce — if a victim refuses to pay LockBit, stolen data may be passed to DragonForce for publication. Extortion is now a collaborative supply chain, not isolated gang activity.
- The affiliate deposit as a quality-control mechanism: LockBit's ~$500 Bitcoin entry requirement is analogous to a franchise fee. It screens for commitment, reduces opportunistic abuse, and signals governance maturity.
- The "customer service" implication of consolidation: larger brands need functional decryptors to maintain payment propensity. The Obscura bug (files over 1 GB unrecoverable) is an example of the quality problem in smaller operators that consolidated brands solve.
- Revenue split structure: acknowledge clearly that specific Q1 2026 affiliate percentage splits are not documented in authoritative sources. Describe the structure (operator takes a cut; affiliate keeps the rest) without inventing numbers.

### Optional (if it fits naturally)
- A hypothetical vignette: a would-be ransomware operator browsing a criminal forum, selecting a RaaS program the way a business owner browses franchise opportunities.

---

## Source Material Focus

Primary sources for this chapter:
- **Report 1 (Check Point Q1 2026):** All data on the three dominant groups, white-label model, cooperative extortion chains, affiliate deposit mechanism, Obscura quality bug.
- **Report 2 (Mandiant/Unit 42 HR) — Secondary:** Use to briefly establish the affiliate role (developed fully in Ch 3).

Key data points to incorporate:
- The Gentlemen: Q4 2025 = 40 victims → Q1 2026 = 166 victims (315% growth). 332 total organizations in first five months of 2026. Roughly 14,700 compromised FortiGate devices (pre-positioned access inventory). Only 13% US victims vs. 49.6% ecosystem average.
- The Gentlemen internal breach: 16+ GB of internal data, offered for $10,000 Bitcoin. Internal discussions of rival groups and interest in code signing.
- LockBit 5.0: launched on RAMP forum September 2025. Multi-platform (Windows/Linux/ESXi). Enhanced evasion/anti-analysis. Faster encryption. Randomized 16-character file extensions. ~$500 Bitcoin affiliate deposit. US share: from 50%+ historical to 21.2%.
- Qilin: 338 victims Q1 2026, most active group three consecutive quarters. Semi-open affiliate model flagged by GuidePoint as a law-enforcement infiltration risk.
- Akira: part of the 41% combined with Qilin/Gentlemen/LockBit.
- Cooperative supply chain: LockBit → DragonForce data-passing for victims who refuse LockBit.
- White-label model: three-step (develop → lease → take a cut); white-label pushes abstraction further (buyer needs no technical skill).

---

## Structural Requirements

### Opening
Open with the franchise metaphor made visceral. Something like: "To open a McDonald's, you pay a fee, sign a contract, and follow a manual. The food, the logo, the fryer — it all comes from headquarters. You just run the location. In 2026, ransomware works the same way." Then immediately ground it with data.

### Body Flow
1. The three-tier model: lay out the structural blueprint of a RaaS operation. Use the franchise analogy consistently. Make clear who does what and who gets paid for what.
2. Three brands, three strategies: Qilin (volume), The Gentlemen (access inventory), LockBit 5.0 (brand recovery). Use these as case studies showing that multiple viable business models exist inside the same criminal economy.
3. The white-label frontier: DragonForce/RansomBay. What it means that the technical barrier is now approaching zero. Connect back to Chapter 1's consolidation theme: more brands, fewer real operators.
4. The cooperative extortion supply chain: ransomware groups sharing victims, pooling infrastructure, passing data between platforms. This is cartelization.
5. The quality-control revelation: why consolidated brands are more dangerous because they deliver better "service" — more reliable decryptors, more consistent negotiation, higher payment conversion.

### Closing
End with a pivot toward the human layer beneath the brand: "Behind every ransomware brand is a workforce — hackers, social engineers, data brokers, and sometimes ordinary employees who don't know they're involved. Chapter 3 will introduce you to them." Set up the workforce chapter with a sense of impending revelation.

---

## Continuity Notes

### References to Other Chapters
- Build on: Ch 1's macro-economics and consolidation framing.
- Foreshadow: Ch 3 (The Workforce) — the affiliates and suppliers mentioned here get their full backstory there.
- Foreshadow: Ch 7 (The Pressure Machine) — the leak sites introduced here get their full treatment there.
- The cooperative extortion supply chain should be briefly mentioned here and paid off more fully in Ch 7.

### Terms & Concepts to Use
- RaaS (defined in Ch 1, operationalized here)
- Affiliate (defined in Ch 1, detailed here)
- Initial Access Broker (IAB) — introduce briefly, defined fully in Ch 3
- Data Leak Site (DLS) — introduced here, defined fully in Ch 7
- White-label ransomware / RansomBay model

---

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Target length: 3,500–5,000 words.
- The franchise metaphor is this chapter's load-bearing structural element — use it consistently but don't overwork it. Vary the framing: sometimes it's a franchise, sometimes a platform, sometimes a cartel. All are accurate.
- The Gentlemen's internal data breach is a great narrative moment — a criminal empire that got hacked. Use it to humanize and add irony without losing urgency.
