# Source Use — Chapter 3: The Wholesalers

## Files read
- books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md (Report #2)

## Main facts used (Report #2)
- Infostealer → IAB → affiliate supply chain; infostealer distribution channels (cracked software, phishing pages, public code repositories, fake CAPTCHA pages).
- IAB validation, enrichment, resale function; brokers as quality-assurance + sales-engineering + risk-underwriting layer.
- IAB price stratification: ~$20 low-privilege credentials to $10,000+ domain-admin access with persistence (Lyrie 2026 defensive playbook).
- Flare (via Lyrie): 16% of infostealer-infected endpoints expose enterprise SSO credentials (up from 6% in 2024); 79% of logs contain Microsoft Entra ID credentials; ~1.17 million logs include credentials + session cookies enabling MFA bypass.
- Cisco Talos Q1 2026 (via Lyrie): phishing reemerged as top initial-access vector in >1/3 of engagements; pre-ransomware engagement share dropped from 50% (Q1 2025) to 18% (Q1 2026) due to earlier defender disruption / kill-chain compression.
- Mandiant 2025 incident-response dataset: exploitation, stolen credentials, and email phishing as leading initial infection vectors; "log in" framing rather than "break in."
- Access-purchase-to-deployment intervals: days to weeks, sometimes under 48 hours.
- NCC Group (January 2026): structured insider recruitment with commission tiers, anonymity guarantees, targeting IT, cloud, identity, and security roles.
- Recorded Future 2026: contractor/gig-worker/MSP-employee recruitment targeting; insider as multi-victim leverage source.
- Rapid7: affiliate drift between RaaS programs as structural feature, not anomaly.
- Credential vintage / freshness as price driver.
- Validator's role in pricing stale vs. fresh access.

## Reports NOT used
- Reports #1, #3, #4, #5 — not invoked.

## Hypothetical Vignette
- Opening: an affiliate scrolling a credential marketplace, comparing listings (low-priced fresh consumer-retailer session vs. high-priced validated regional-bank domain-admin access), opening chat with the seller, getting validation evidence, completing escrow. All mechanics are documented in Report #2: marketplace UX with seller reputation/escrow, freshness/age as pricing factor, validation evidence as quality assurance, deployment within days-to-72-hours window. No invented capabilities or specific actors.

## Cross-chapter references
- ZERO explicit cross-chapter pointer text used. Thematic resonance handled implicitly (the platform/franchise architecture from Ch 1-2 is referenced as "the operator's platform" and "the previous chapter" once in the affiliate-drift paragraph). One explicit reference to "the previous chapter" used; within the one-explicit-reference cap.
