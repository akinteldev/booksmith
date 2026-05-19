# Chapter 3 Source Use

## Files Read
- books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md (Report #2)

## Main Facts Used
- Infostealer delivery channels: cracked software, phishing pages, public code repositories, fake CAPTCHA pages (ENISA via Report #2).
- Mandiant 2025 IR: exploitation, stolen credentials, email phishing as leading initial vectors; "log in" rather than break in.
- Cisco Talos Q1 2026: phishing top initial-access vector in >1/3 of engagements; pre-ransomware engagements 50% → 18% (defenders catching activity earlier).
- Pricing: $20 low-privilege → $10,000+ domain-admin with persistence (Lyrie Research / Flare).
- 16% of infostealer-infected endpoints expose enterprise SSO credentials (up from 6% in 2024).
- 79% of logs contain Microsoft Entra ID credentials.
- 1.17M logs contain credentials + session cookies enabling MFA bypass.
- Kill-chain compression: access purchase → ransomware deployment in under 48 hours.
- Tiered ecosystem: infostealer operators → validators → IABs → affiliates → core operators.
- Change Healthcare: compromised Citrix account without MFA, infostealer-infected employee, $22M ransom (Hudson Rock via InfoStealers).
- IABs as "invisible toll booth" between phishing and ransomware.
- BreachSense framing of defensive window between credential theft and deployment.
- NCC Group: insider recruitment growing; gig-worker exploitation.
- Affiliate migration after RansomHub collapse toward DragonForce / LockBit (Rapid7, ENISA).
