# Source Use — Chapter 9: The Cryptographic Wall

## Files read
- books/ransomware-inc/reports/task_1779010243_15a209c49d.md (Report #3)
- books/ransomware-inc/reports/task_1779012482_285007975a.md (Report #4)

## Main facts used (Report #3)
- NIST 2024 finalization of post-quantum cryptography standards: FIPS 203 (ML-KEM, derived from CRYSTALS-Kyber) for key establishment; FIPS 204 (ML-DSA, derived from CRYSTALS-Dilithium) for digital signatures; FIPS 205 (SLH-DSA, derived from SPHINCS+) for digital signatures.
- Hybrid-cryptography baseline of modern ransomware: symmetric file encryption (typically AES, sometimes ChaCha20) with asymmetric key wrapping; per-victim or per-file symmetric key wrapped by RSA or elliptic-curve public-key crypto with the operator-held private key.
- Defender's historical margin has been implementation errors: reused keys, leaked private keys, predictable random-number generators, seized infrastructure with plain-text private keys, miswritten integrations between symmetric and asymmetric layers — not brute-force cryptanalysis.
- PQC-in-ransomware as plausible near-term evolution: if well-implemented, ML-KEM key wrapping would resist both classical and future quantum cryptanalysis.
- SoftwareSeni 2026 claim of live ML-KEM/Kyber1024 ransomware use — explicitly framed in the report as requiring corroboration by major IR firms, malware repositories, or government advisories before being considered established fact. The chapter carries that caveat.
- "As of May 17, 2026, there is no widely verified public evidence that major ransomware families have broadly deployed standardized post-quantum cryptography in operational payloads at scale" — paraphrased into the chapter's calibration paragraph.
- Harvest-now-decrypt-later threat model: adversary captures encrypted data today, stores it, decrypts later when quantum cryptanalysis becomes available; Federal Reserve and financial-sector framing.
- AI-assisted cryptographic industrialization: language-model tooling reduces the implementation work for new cryptographic primitives from weeks to days; better-resourced criminal-software ecosystems likely to reach high cryptographic-implementation quality across the next several years.
- Platform-specific dimension: Windows endpoints, Linux servers, ESXi hypervisors with asymmetric cryptographic adoption curves; ESXi as the most consequential operational shift surface.
- Defensive shift away from cryptographic reversal toward prevention, segmentation, immutable backups, identity security, rapid containment, resilience engineering.
- FinCEN figure: ~$2.1B U.S. ransomware payments across 2022–2024 as the economic engine funding criminal-market investment.

## Main facts used (Report #4)
- Encryptionless extortion as operationally rational post-Operation-Secure model — used in the harvest-now-decrypt-later overlap paragraph.
- Multi-extortion architecture and the negotiation desk as the surface where the cryptographic wall converts to payment.
- The data-leverage centrality (BlackFog 96% exfiltration; one-in-nine public) is referenced thematically in the closing economic-summary frame, without directly citing the figures (Report #4 was secondary economic context per the chapter prompt).
- The "negotiation desk is the entire operation" framing inherits Report #4's documented architecture.

## Reports NOT used
- Reports #1, #2, #5 — not invoked. No data points, threat actors, or capabilities from those reports appear in this chapter.

## Hypothetical Vignette
- Opening + closing bookend: an incident-response lead in a windowless lab analyzing a recovered ransomware binary from a regional hospital network compromise. He finds a clean, textbook ML-KEM implementation wrapping the symmetric session key, with no obvious flaws. The hospital ultimately pays roughly 40% of the opening demand; three patients die from delays in care plausibly attributable to the systems outage during the two-week restoration window.
- All vignette mechanics are documented in Report #3 (hybrid cryptography baseline, ML-KEM/Kyber FIPS 203 specification, implementation-error margin as the historical decryption path) and Report #4 (staged-discount negotiation architecture, "data deletion" upsell, cryptocurrency wire payment, decryption-key delivery, two-week restoration, regulatory disclosure).
- The "three patients die from delays attributable to the systems outage" detail is consistent with documented operational consequences of ESXi-cluster compromise in hospital environments described in Report #3's platform-specific framing. No specific real-world incident is named or invented.
- No real victim hospital or named operator brand is invented for the vignette.

## Cross-chapter references
- ZERO explicit cross-chapter pointer references. This is the closing chapter; there is no "next chapter." All convergence language is thematic ("the economy this book has described," "every prior layer," "the cryptographic wall is the boundary the space ends at") and respects the chapter prompt's "let the convergence speak for itself" instruction.
- "This book" appears as natural closing-frame language (8 instances), which the chapter prompt's closing directive explicitly supports ("End the book on revelation… the book's last beat should land with the reader feeling the weight of what it means to live in an economy where extortion has been industrialized and may soon be cryptographically locked in place").

## Calibration discipline
- The SoftwareSeni 2026 ML-KEM/Kyber1024 claim is presented with the explicit caveat that it has not been corroborated by major incident-response firms, malware repositories, or government advisories.
- The PQC-in-ransomware adoption is presented as a forecast, not a confirmed current state. The opening vignette is anchored in the forecast language ("a clean, textbook implementation… no obvious flaws") rather than in a claim that this is universally observed in the wild.
- Quantum-computer arrival forecasts are framed as a range (early 2030s to late 2040s), consistent with the Federal Reserve and financial-sector framing.
- The defensive prescription (prevention, segmentation, immutable backups, identity security, rapid containment, resilience engineering) is taken directly from Report #3's "defensive shift" framing.
- The closing call ("not panic… recognition") respects the Book Bible's "calm alarm" voice guidance and the threat-intelligence community's avoid-overclaiming discipline.
