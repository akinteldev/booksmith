# Chapter 3: White-Label Crime

## Core Question

How did white-label ransomware democratize cybercrime — and what happens when anyone can operate a ransomware brand without building any of the underlying technology?

## Purpose in the Book

This chapter deepens the platform economy argument by exploring its most extreme expression: white-label ransomware. If Chapter 1 explained how RaaS separates development from execution, Chapter 3 explains the next logical step — separating branding from infrastructure entirely. The result is a criminal franchise model so scalable that non-technical operators can run what looks like an independent ransomware group while relying entirely on someone else's tooling. The chapter also introduces the concept of cartel-as-platform: the infrastructure provider who doesn't care what brand their clients use, only that they take their cut of every payment.

## Required Content

### Must Cover

- The white-label ransomware model: how it works, who offers it (DragonForce as primary example), what it means for the criminal ecosystem
- DragonForce's cartel model in detail: offering backend services (admin panels, leak sites, tooling, negotiation infrastructure) while affiliates operate under separate brand names
- How this lowers the barrier to entry: the "non-technical criminal" who can now operate a ransomware brand by subscribing to DragonForce's platform
- The service bundle: what you get when you subscribe to white-label ransomware infrastructure

### Should Include

- Revenue sharing mechanics: DragonForce's 80% affiliate share; RansomHub's historical 90% — the criminal franchising economics
- The attribution distortion effect: because affiliates can operate under any brand name, identifying the real infrastructure provider becomes nearly impossible
- What "white-label" means for law enforcement: even if you disrupt the visible brand, the underlying infrastructure (and its operator) may survive
- The analogy to legitimate white-label SaaS: how this mirrors cloud services that power many competing consumer brands from a single backend

### Optional (if it fits naturally)

- Brief mention of the "Ransom Bay" white-label service as an example of explicit criminal infrastructure-as-a-service marketing

## Source Material Focus

Primary sources for this chapter:
- **Report 1:** DragonForce cartel model, white-label service details, profit-sharing terms, attribution distortion, criminal franchising mechanics
- **Report 2:** Platform-like onboarding, IAB/affiliate ecosystem integration, criminal managed-service-provider framing

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779005211_949b8650bc.md`
- `books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points to incorporate:
- DragonForce: 80% profit share for affiliates; operates as cartel providing backend; permits affiliates to use own brand names
- RansomHub: 90% profit share (historical, before shutdown) — highest in ecosystem
- White-label model allows non-technical criminals to operate ransomware campaigns using shared infrastructure
- Attribution distortion: incident attributed to visible brand may have been powered by different infrastructure entirely
- DragonForce reportedly targeted and absorbed infrastructure/affiliates from competitors including Mamona and BlackLock

## Structural Requirements

### Opening

Hypothetical vignette: a criminal entrepreneur with no technical skills reads a forum post advertising DragonForce's affiliate program. Within a week, they are operating under their own brand name, with a functioning leak site, negotiation portal, and ransomware payload — none of which they built. Walk through what they are actually getting for their percentage cut.

### Body Flow

1. The white-label model explained: what it is, how it differs from traditional RaaS, why it matters
2. DragonForce's cartel structure: the visible/invisible split between brands and infrastructure
3. The implications: attribution becomes harder, infrastructure survives brand disruption, barriers to entry fall to near zero

### Closing

End on the revelation: the criminal economy has achieved something that legitimate tech companies spent billions building — a platform model where anyone can launch a product without owning any infrastructure. The real power in the ransomware economy is not in the brand names we see on leak sites. It is in the invisible infrastructure beneath them.

## Continuity Notes

### Thematic Links (use sparingly)

- The infrastructure/brand separation theme here is the technical foundation for Chapter 9's argument that targeting infrastructure (not brands) is the only effective defensive posture

## Style Reminders

- Follow the book bible's voice guidelines exactly
- Target length: 3,500 — 5,000 words
- Maintain consistent POV and tense throughout
- No chapter subheadings — flowing prose only
