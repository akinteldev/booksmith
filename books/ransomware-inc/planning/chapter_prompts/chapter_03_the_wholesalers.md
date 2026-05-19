# Chapter 3: The Wholesalers

## Core Question
Who are the people quietly selling the keys to your company, and how does a twenty-dollar credential become a multi-million-dollar ransom?

## Purpose in the Book
This chapter turns from the platforms to the labor market that supplies them. It introduces the reader to the access economy: infostealer crews who harvest credentials, Initial Access Brokers who validate and price those credentials, and ransomware affiliates who turn validated access into intrusions. The chapter must make this supply chain feel physical — a wholesale market that moves keys, badges, and session cookies the way commodity markets move grain — and it must show the speed and price ranges that make it work. It also introduces identity (SSO, Entra ID, session cookies) as the single most consequential credential class in 2026 ransomware, a theme that will recur in Chapters 5 and 7.

## Required Content

### Must Cover
- The pipeline as a chain: infostealer malware harvests credentials and session cookies; IABs validate and enrich access; ransomware affiliates buy it and operationalize it.
- Price stratification: low-privilege credentials can sell for as little as $20; domain-admin access with persistence can exceed $10,000. Make the spread tangible — a single stolen wallet vs. a master key.
- The scale of identity exposure: 16% of infostealer-infected endpoints expose enterprise SSO credentials; 79% of logs contain Microsoft Entra ID credentials; 1.17 million logs include credentials plus session cookies that may enable MFA bypass.
- Compression of the kill chain: Cisco Talos Q1 2026 reporting that phishing reemerged as the top initial access vector in more than one-third of engagements; pre-ransomware engagement share dropping from 50% to 18%; access-purchase-to-deployment intervals of days to weeks, sometimes under 48 hours.
- Labor partitioning as a logical consequence: phishers and stealer operators generate credentials; access validators test them; IABs package and resell; affiliates operationalize; core operators provide tooling, leak infrastructure, and negotiation. Each role is narrow and repeatable.
- The HR layer: RaaS programs compete for affiliate labor via revenue splits, reliability, tooling, and reputation; affiliate drift between brands is now a structural feature, not an anomaly.

### Should Include
- The rogue-insider angle: NCC Group reporting that ransomware gangs offer commissions and anonymity to employees with trusted access — IT, cloud, identity, security. Recorded Future's similar 2026 framing of insider recruitment.
- The "log-in not break-in" framing: Mandiant's identification of exploitation, stolen credentials, and email phishing as leading initial infection vectors in 2025.
- A grounded vignette: a mid-level help-desk technician whose stolen browser session is sold within a week to an affiliate who logs in as them. Use only mechanics described in Report #2.
- A brief mention that low-privilege credentials can still escalate via lateral movement — the $20 ticket is the entry, not the ceiling.

### Optional (if it fits naturally)
- The defensive intervention window: the gap between credential theft and ransomware deployment is often days to weeks, which is also the only realistic detection window for many defenders.

## Source Material Focus

Primary sources for this chapter:
- **Report #2:** Infostealer-to-IAB-to-affiliate pipeline; access pricing; identity exposure statistics; phishing reemergence; rogue-insider recruitment; affiliate drift dynamics.

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points, quotes, or findings to incorporate:
- Low-privilege credentials from as little as $20; domain-admin access with persistence exceeding $10,000.
- 16% of infostealer-infected endpoints expose enterprise SSO credentials.
- 79% of infostealer logs contain Microsoft Entra ID credentials.
- 1.17 million logs include credentials plus session cookies enabling MFA bypass.
- Cisco Talos Q1 2026: phishing reemerged as top initial access vector in more than one-third of engagements.
- Pre-ransomware engagements down from 50% (Q1 2025) to 18% (Q1 2026) because defenders disrupted activity earlier in the intrusion lifecycle.
- Mandiant 2025: exploitation, stolen credentials, and email phishing as leading initial infection vectors.
- NCC Group / Recorded Future 2026 reporting on insider recruitment, commissions, and gig-worker exploitation.
- The infostealer → dark-web / Telegram channel → broker validation → affiliate resale pipeline; days-to-weeks intervention window.

## Structural Requirements

### Opening
Open with a grounded scene: a stolen browser session changing hands in a dark-web marketplace. A user's saved logins and cookies are listed for sale, validated, repackaged, and resold within days. Make it feel like a commodity floor.

### Body Flow
1. The opening commodity-floor scene → transition into the pipeline that produces it.
2. The pipeline: infostealers → IAB validation → affiliate purchase, with the price ranges as the visible spine of the market.
3. The identity exposure picture (SSO, Entra ID, session cookies, MFA bypass) and what it means that browser cookies have become the new master keys → transition into compression.
4. Compression: phishing reemergence, defender disruption pushing pre-ransomware share down, sub-48-hour access-to-deployment cycles → transition into the HR layer.
5. The HR layer: affiliate competition, drift, insider recruitment — labor as the platform's most contested input.

### Closing
End on revelation: the reader has learned that there is a wholesale market for the keys to their employer, that it operates on commodity logic, and that the most consequential credentials in that market are the ones that prove identity, not just access a single device. Set up Chapter 4's pivot to which victims this supply chain ends up pointing at, and why.

## Continuity Notes

### Thematic Links (use sparingly)
- Chapter 1 and Chapter 2 have already introduced the platform/affiliate concept; this chapter shows who the affiliates buy from. Do not write "Chapter 2 explained..." — let the deepening speak for itself.
- Concepts that may naturally recur: IABs, infostealers, identity compromise (SSO/Entra ID), session-cookie theft, insider recruitment, affiliate drift.

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Aim for about 5,000 words.
- Maintain consistent POV and tense throughout.
- ONLY `# Chapter 3: The Wholesalers` as the heading — no subheadings inside the chapter body.
- No horizontal rules, no italic subtitle line, no bracketed citations.
