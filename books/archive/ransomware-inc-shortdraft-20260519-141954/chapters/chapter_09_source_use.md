# Chapter 9 Source Use

## Files Read
- books/ransomware-inc/reports/task_1779010243_15a209c49d.md (Report #3)
- books/ransomware-inc/reports/task_1779012482_285007975a.md (Report #4)

## Main Facts Used (Report #3)
- Modern ransomware uses hybrid cryptography (symmetric file encryption + asymmetric key wrapping); defenders rarely recover via brute force absent implementation errors, key reuse, leaked private material, or infra compromise.
- NIST FIPS 203 (ML-KEM, the standardized form of Kyber) finalized in 2024.
- SoftwareSeni 2026 alleged live ML-KEM/Kyber1024 ransomware use — explicitly cautioned to require corroboration by major IR firms, malware repositories, or government advisories before being treated as established fact. Honor caveat.
- Defensive implication: well-implemented PQC for per-victim key wrapping could make decryption infeasible absent backups, key seizure, attacker cooperation, or implementation flaws.
- Harvest-now-decrypt-later threat model (Federal Reserve framing applied to long-lived sensitive data + ransomware exfiltration).
- FinCEN: approximately $2.1B in ransomware payments across 2022–2024.
- AI-assisted cryptographic industrialization framing.

## Main Facts Used (Report #4)
- BlackFog: 96% of tracked ransomware incidents involve data exfiltration (relevant to harvest-now framing).
- Multi-extortion architecture as context for closing argument.
