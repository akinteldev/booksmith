# Chapter 3: The Wholesalers

## Core Question
Who are the people quietly selling the keys to your company — and how does a $20 credential become a multi-million-dollar ransom?

## Purpose in the Book
This chapter introduces the access economy: infostealers, Initial Access Brokers, and the labor market that supplies the franchises in Chapter 2. The reader should leave understanding that ransomware is downstream of an entire supply chain — that the moment of compromise often happens months before the encryption, in the form of a single stolen browser session that nobody noticed.

## Required Content

### Must Cover
- The pipeline: infostealer malware harvests credentials, session cookies, SSO tokens, and cloud credentials → IABs validate, enrich, and resell that access → affiliates buy it and use it to ransom companies.
- How infostealers are delivered: cracked software, phishing pages, public code repositories, fake CAPTCHA pages, other social-engineering channels.
- The economic structure: low-privilege credentials may sell for as little as $20; domain-admin access with persistence can exceed $10,000.
- The scale of identity exposure: 16% of infostealer-infected endpoints expose enterprise SSO credentials; 79% of logs contain Microsoft Entra ID credentials; 1.17 million logs include credentials plus session cookies that may enable MFA bypass.
- The shift in initial access: Mandiant identified exploitation, stolen credentials, and email phishing as leading vectors; Cisco Talos found phishing reemerging as the top vector in more than one-third of Q1 2026 engagements; pre-ransomware engagement detection declined to 18% from 50% in Q1 2025 because defenders disrupted activity earlier.
- The labor specialization angle: "attackers increasingly log in with valid credentials rather than deploy noisy malware at the outset." Frame this as why the access economy matters so much.
- The compression of the kill chain: access purchase, validation, lateral movement, data theft, and deployment may occur in under 48 hours.

### Should Include
- A grounded opening: a vignette of an end-user installing a cracked productivity application, or interacting with a fake CAPTCHA page, and unknowingly handing over their browser session. The character can also be a salesperson whose Entra ID token is captured during routine browsing. Use only mechanics described in Report #2.
- A second vignette inside the IAB market: a broker validating an access listing before reselling.
- The defensive window framing: BreachSense's observation that the gap between theft and ransomware deployment is often days to weeks, creating a defensive intervention window.
- The metaphor work: position infostealer logs as "a stolen wallet full of credit cards, ID badges, and keys to every door the victim has ever walked through"; position IABs as wholesalers.

### Optional (if it fits naturally)
- ENISA's framing of ransomware as one of the most directly disruptive cybercrime threats in EU organizations.
- The Rapid7 / ENISA observation that RansomHub's disappearance pushed affiliates toward DragonForce and LockBit — a callback to the franchise dynamics in Chapter 2 without explicitly signposting them.

## Source Material Focus

Primary sources for this chapter:
- **Report #2:** Infostealer-to-IAB-to-affiliate pipeline; SSO/Entra ID exposure statistics; pricing tiers; Mandiant/Cisco Talos initial-access findings; kill-chain compression; access economy specialization.

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points, quotes, or findings to incorporate:
- Pricing: low-privilege credentials ~$20; domain-admin access with persistence may exceed $10,000.
- 16% of infostealer-infected endpoints expose enterprise SSO credentials.
- 79% of logs contain Microsoft Entra ID credentials.
- 1.17 million logs include credentials plus session cookies enabling MFA bypass.
- Mandiant 2025 IR dataset: exploitation, stolen credentials, and email phishing as leading initial infection vectors.
- Cisco Talos Q1 2026: phishing top initial-access vector in over one-third of engagements.
- Pre-ransomware engagements: 50% (Q1 2025) → 18% (Q1 2026) — defenders are catching activity earlier.
- Kill-chain compression: access purchase → deployment in under 48 hours.
- Affiliate migration after RansomHub's collapse toward DragonForce and LockBit.

## Structural Requirements

### Opening
Open inside a moment of compromise that is small enough to feel banal: an end-user clicks something, types something, or installs something. Then widen to show that this single mundane action just produced an artifact that will be sold three or four times before it reaches the attacker who will use it.

### Body Flow
1. The opening compromise scene → widen into the infostealer layer of the economy.
2. The IAB layer: validation, enrichment, resale; the pricing structure. → transition into who buys.
3. The affiliate layer: how the purchased access turns into intrusion; the kill-chain compression.
4. The strategic frame: this is a wholesale supply chain. Ransomware operators no longer hack their way in; they buy in.

### Closing
End on the unsettling realization that by the time a ransomware operator names a company on a leak site, the original act of compromise may have happened months earlier and may have been a single distracted click by a single employee. Set up Chapter 4, which moves from how attackers get in to which organizations they choose to hit and why.

## Continuity Notes

### Thematic Links (use sparingly)
- This chapter reinforces the affiliate-economy framing from Chapter 2 without quoting it. Let the resonance be implicit.
- Concepts that may naturally recur: identity compromise, SSO/Entra ID, MFA bypass via session cookies (all return in Chapters 5 and 7).

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Aim for about 5,000 words.
- Maintain consistent POV and tense throughout.
- ONLY `# Chapter 3: The Wholesalers` as the heading — no subheadings inside the chapter body.
- No horizontal rules, no italic subtitle line, no bracketed citations.
