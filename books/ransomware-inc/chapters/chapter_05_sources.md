# Source Use — Chapter 5: The Recovery Trap

## Files read
- books/ransomware-inc/reports/task_1779014305_434487fb06.md (Report #5)

## Main facts used (Report #5)
- Strategic frame: 2025–2026 ransomware operations defined by deliberate targeting of recovery infrastructure (backups, identity services, hypervisors, disaster recovery).
- Active Directory / Entra ID compromise as the force multiplier converting limited intrusion into enterprise-wide business-continuity event (authentication, privilege escalation, lateral movement, security-policy enforcement).
- ESXi as strategic target; live exploitation of VMware ESXi zero-day vulnerabilities into January 2026.
- Edge-device exploitation: Trend Micro 2026 finding that edge-device exploitation rose from 3% to 22% of vulnerability-exploitation breaches in a single year; structural driver = attacker economics (perimeter appliances cheaper to exploit, weak telemetry, slow patching, sit in front of authentication flows).
- Clop's mass exploitation of Oracle E-Business Suite vulnerabilities.
- Akira's continued monetization of SonicWall vulnerabilities.
- BYOVD: Baidu Antivirus driver flaw used to bypass endpoint detection and response before DeadLock ransomware deployment.
- November 2025 Windows kernel privilege-escalation patch-cycle exploitation; SYSTEM-level access after foothold.
- MSP / ICT supply-chain / third-party access as downstream ransomware multipliers.
- Convergence of state-sponsored techniques (edge exploitation, zero-day use, stealthy persistence) with criminal ransomware tradecraft.
- "Log in not break in" continuation framing (also used in Ch 3 but anchored in Report #5 here).

## Reports NOT used
- Reports #1, #2, #3, #4 — not invoked (themes from Chs 1-4 referenced thematically without importing their statistics).

## Hypothetical Vignette
- Opening: a backup administrator getting a 3 a.m. alert, logging in, discovering immutable snapshots deleted gradually over 19 days, identity compromise looming, ESXi staging in progress. Illustrates only documented mechanics: patient backup-environment dwell, identity compromise as enabler, hypervisor encryption as final-phase operational catastrophe, contractor phishing as origin. No invented vendor names, no specific company, no quoted operator statements.
- Closing returns to the same character with the post-incident consultant timeline and board reaction.

## Cross-chapter references
- ONE explicit reference: the closing paragraph naming "The next chapter" (Ch 6 on agentic AI). Within the one-explicit-reference cap.

## Author voice / accuracy checks during revision
- Reviewed against the prompt's stated "Must Cover" items; all present.
- ENISA framing for the three primary targets (backups / identity / hypervisors) preserved verbatim in interpretation, not direct quote.
- Trend Micro 3-to-22% finding attributed correctly and explained structurally.
- Worked examples (Clop/Oracle, Akira/SonicWall, Baidu/DeadLock, November 2025 Windows kernel) attributed correctly with the "exploited in ransomware intrusions" framing the source uses.
