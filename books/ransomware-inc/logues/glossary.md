# Glossary

Access broker. See Initial Access Broker.

Active Directory (AD). Microsoft's on-premises directory service. It governs which users and machines exist in an enterprise network and what each is allowed to do. In the architecture this book describes, a compromise of Active Directory converts a single foothold into enterprise-wide control. Ransomware operators target it early in the intrusion.

Affiliate. A semi-independent criminal contractor who carries out intrusions and deploys a ransomware platform's payload in exchange for the majority share of the resulting ransom. Affiliates pay platforms a deposit to join, accept the platform's terms, and use the platform's tooling, infrastructure, and brand for the duration of their attacks. Affiliates can migrate between platforms when their preferred platform fails.

Affiliate program. The set of terms a ransomware platform offers to recruit affiliates. Includes the revenue-share split, the deposit requirements, the supported targets, the tooling provided, and the operational rules the affiliate is expected to follow.

Agentic AI. A category of artificial-intelligence systems in which a model performs multi-step tasks by selecting and invoking tools, rather than producing a single response to a prompt. In the ransomware context, the reporting frames agentic capabilities as augmentation of human attacker labor rather than autonomous attack. Forecasts of more autonomous agentic capability appear in the underlying reports as 2026 projections rather than confirmed widespread current activity.

AES (Advanced Encryption Standard). The symmetric encryption algorithm used to encrypt files in almost all modern ransomware payloads. Mathematically infeasible to defeat by brute force at standard key lengths.

Anchoring. A negotiation tactic in which the opening demand is set artificially high so that subsequent reductions feel like concessions even when the final price remains high. Used routinely by ransomware negotiation desks.

Bring Your Own Vulnerable Driver (BYOVD). An attack technique in which an operator loads a legitimately signed but flawed kernel driver onto a victim's system to disable endpoint security software. The Baidu Antivirus driver case associated with the DeadLock operation is a documented example.

Cartel signaling. Public or semi-public coordination language used by ransomware brands to imply joint market power, even when actual operational integration is limited. Distinct from a verified operational alliance. The threat-intelligence community is divided on whether the 2026 cartel language between DragonForce, LockBit, and Qilin reflects coordination or theater.

Conditional access. An identity-security architecture in which authentication and authorization decisions are made dynamically based on user, device, location, and risk signals. Used to make stolen credentials less useful by adding conditions the attacker cannot easily satisfy.

Continuous access evaluation. A complementary identity-security mechanism in which already-granted sessions are revalidated against current risk signals and revoked if conditions change. Reduces the operational value of session-cookie theft.

Creative destruction. An economic term, borrowed from twentieth-century capitalism literature, that describes the redistribution of resources when established firms fail. Applied in the underlying reporting to the ransomware market: when a platform is taken down, its affiliates, infrastructure recipes, and brand credibility do not vanish but redistribute toward the surviving platforms. The term is descriptive, not approving.

Cryptocurrency. The payment medium in which ransomware payments are made. Most commonly Bitcoin and, increasingly, privacy-focused coins such as Monero. The medium's pseudonymity and irreversibility are operational requirements for the criminal market.

Cryptographic wall. The closing-chapter framing of the book: the point at which post-quantum cryptography is integrated into operational ransomware payloads such that the per-victim key cannot, by any means available to the defender, be recovered without payment.

Data Leak Site (DLS). See Leak site.

DDoS (Distributed Denial of Service). A pressure tactic in which a target's services are overwhelmed by traffic from many compromised endpoints. Used by some ransomware operators as one component of multi-extortion.

Discount schedule. The published timeline on a ransomware leak site indicating how the demand will be reduced if payment is made within early windows and how the discount disappears as the deadline approaches. Engineered to accelerate the victim's decision.

Double extortion. The combination of file encryption with the threat to publish stolen data if payment is not made. Standard model across the leading ransomware platforms.

Edge device. Internet-facing hardware such as a VPN appliance, firewall, or remote-access gateway. A common ransomware entry point. The reporting documents edge-device exploitation rising from approximately three percent to twenty-two percent of vulnerability-exploitation breaches.

EDR (Endpoint Detection and Response). Security software running on individual endpoints to detect and respond to malicious activity. Targeted by BYOVD and other techniques designed to disable it before payload deployment.

Encryption. In the ransomware context, the algorithmic transformation of files into a form that cannot be read without the corresponding key. Modern ransomware uses hybrid encryption: a symmetric algorithm (usually AES) for files, an asymmetric algorithm for wrapping the symmetric key.

Encryptionless extortion. A model in which the operator steals data but does not encrypt the victim's files. The leverage comes entirely from the threat of data publication. Has become operationally rational for some operators as legal and regulatory pressure on payment processing has increased.

ENISA (European Union Agency for Cybersecurity). A European Union institution that publishes threat-landscape reports. Source of the ransomware sector and geographic figures the book cites in the chapter on strategic victimology.

Entra ID. Microsoft's cloud identity service, formerly known as Azure Active Directory. Plays the same role in cloud environments that Active Directory plays on premises. A primary target of access brokers and affiliates because compromise of the directory typically converts a single intrusion into enterprise-wide control.

ESXi. VMware's hypervisor product. A single ESXi host can run many virtual machines, so encrypting a hypervisor can disrupt an entire datacenter. ESXi-targeting ransomware payloads have been among the most damaging in the period the reports cover.

Exfiltration. The transfer of stolen data out of a victim's environment to operator-controlled infrastructure. Distinct from encryption. Required for double, triple, and quadruple extortion.

FinCEN (Financial Crimes Enforcement Network). A bureau of the United States Department of the Treasury responsible for tracking financial crimes including ransomware payments. The source of the approximately two-point-one billion dollar United States ransomware payment figure for the 2022 to 2024 period.

FIPS 203. The Federal Information Processing Standard for ML-KEM, published by the United States National Institute of Standards and Technology in August 2024. The standard that makes post-quantum key establishment available as a library call.

Harvest-now-decrypt-later. The threat model in which encrypted data stolen today is retained against future cryptanalytic capability. Originally framed for diplomatic and intelligence contexts; increasingly relevant to ransomware operators who steal but do not delete data.

Hybrid encryption. The standard modern construction in which a symmetric algorithm encrypts data and an asymmetric algorithm encrypts the symmetric key. Used in essentially all current ransomware.

Hypervisor. A software layer that allows multiple virtual machines to share a single physical server. ESXi is the most operationally consequential hypervisor in the ransomware threat landscape.

Hyper-personalization. A category of social-engineering tactic in which messages and calls are calibrated against detailed public and stolen data about the specific target. The reporting forecasts increasing AI-driven hyper-personalization across phishing and vishing operations.

Immutable backups. Backup systems designed so that data, once written, cannot be modified or deleted by an attacker who has compromised the production environment. A core defensive layer against the recovery-trap mechanic.

Initial Access Broker (IAB). A specialist who breaks into networks, validates the access, packages it, and resells it to ransomware affiliates without participating in the final attack. A central role in the access economy.

Infostealer. Malware designed to harvest credentials, session cookies, browser data, and authentication tokens from a victim's device and exfiltrate them to a market for resale. The primary feedstock of the access economy.

Intrusion. The early phase of an attack in which the operator establishes initial access, elevates privileges, performs reconnaissance, and moves laterally. Distinct from the payload-deployment phase that follows.

Kernel driver. Software that runs at the most privileged level of an operating system. Targeted by BYOVD attacks because compromise of a driver typically defeats endpoint security software.

Kyber. The academic name of the lattice-based key-encapsulation algorithm that NIST standardized as ML-KEM in FIPS 203.

Lateral movement. The phase of an intrusion in which the attacker, having established initial access, moves from one part of the victim's environment to others. Often involves directory-service compromise.

Lattice cryptography. The mathematical family from which ML-KEM and most current post-quantum candidates are constructed. Believed, on current evidence, to resist quantum cryptanalysis.

Leak site (Data Leak Site, DLS). A criminal-operated public website used to name victims, display countdown timers, publish stolen data when negotiations fail, and provide a public face for the platform. The threat-intelligence community uses leak-site listings as the primary measurement instrument for the industry.

LockBit 5.0. The September 2025 relaunch of the LockBit ransomware platform after its 2024 disruption by Operation Cronos. Supports Windows, Linux, and ESXi in a single package. Requires affiliates to deposit approximately five hundred dollars in Bitcoin.

ML-DSA. The NIST-standardized post-quantum digital-signature algorithm derived from Dilithium. Published as FIPS 204.

ML-KEM. The NIST-standardized post-quantum key-encapsulation algorithm derived from Kyber. Published as FIPS 203. The cryptographic primitive at the center of the book's closing chapter.

Multi-Factor Authentication (MFA). An authentication architecture that requires a second factor beyond a password. Historically considered a strong defense. Increasingly bypassed by session-cookie theft, MFA fatigue attacks, and adversary-in-the-middle phishing.

Multi-extortion. A general term for extortion models that combine multiple pressure layers. Double extortion adds data-publication threat to encryption; triple and quadruple extortion add further layers such as customer notification, DDoS, executive harassment, or regulatory disclosure threats.

Negotiation desk. The criminal-side workflow that runs the chat-window negotiation between operator and victim. Staffed by personnel who, in the transcripts the underlying reports analyze, behave more like enterprise sales representatives than like criminals.

NIST (National Institute of Standards and Technology). The United States standards body responsible for, among other things, the FIPS 203, 204, and 205 post-quantum cryptography standards.

NordStellar. The threat-intelligence vendor whose published analysis of 256 ransomware negotiation transcripts the book cites in the chapter on the negotiation desk.

Operation Cronos. The 2024 multinational law-enforcement action against LockBit. Seized infrastructure, exposed source code and affiliate panels, and humiliated leadership in public. Did not prevent LockBit's September 2025 relaunch as LockBit 5.0.

Patch compression. The decreasing window between vulnerability disclosure and active mass exploitation. Documented in the reports as a 2025 trend in ransomware operator behavior.

Phishing-resistant authentication. Authentication mechanisms designed to be resistant to credential theft and adversary-in-the-middle attacks. Includes hardware security keys and certificate-based authentication.

Platform. In this book's framing, a ransomware brand that provides infrastructure, software, and brand presence to affiliates who run intrusions under that brand's banner. Examples in 2026 include Qilin, LockBit 5.0, Akira, The Gentlemen, and DragonForce.

Platform economy. An economic model in which a central operator provides infrastructure to independent contractors who deliver a service to end users. Applied in this book to the ransomware market, in which the platforms provide tooling, the affiliates run attacks, and the victims are extorted.

Post-Quantum Cryptography (PQC). Cryptography designed to resist attacks by sufficiently powerful future quantum computers. NIST finalized the first PQC standards in 2024.

Qilin. The ransomware platform that was, across 2025 and into 2026, the most active in the world by leak-site volume. Posted 338 victims in Q1 2026.

Quadruple extortion. A multi-extortion model adding a fourth pressure layer beyond encryption, data-publication threat, and DDoS. Often involves executive or customer harassment campaigns or regulatory-disclosure leverage.

Random-number generator (RNG). A component of cryptographic systems that produces unpredictable values for keys and nonces. Implementation flaws in RNG seeding have, historically, produced some of the decryption-tool opportunities defenders have exploited.

Ransomware. Malicious software that encrypts a victim's files and demands payment for the decryption key. In the contemporary market, the term also covers data-theft extortion that may not involve encryption at all.

Ransomware-as-a-Service (RaaS). The business model in which a core operator builds and maintains a ransomware platform and licenses it to affiliates who pay a share of ransom proceeds. The dominant model across the leading 2025 and 2026 brands.

RansomHub. A ransomware platform that, in April 2025, went offline without announcement. Its affiliates migrated to Akira, Qilin, DragonForce, and other surviving platforms. Cited as the clearest worked example of the access-redistribution dynamic.

Recovery trap. The mechanic in which operators deliberately destroy or impair the victim's ability to recover without paying: backups, directory services, hypervisors, and identity infrastructure are targeted as a precondition for the leverage the negotiation desk later applies.

Recovery time objective (RTO). The maximum tolerable duration of a service outage, as defined in an organization's continuity planning. The realistic ransomware recovery time, in the cases the reports document, routinely exceeds the contractual RTO by orders of magnitude.

Regulatory leverage. The use of regulatory disclosure obligations — securities filings, breach-notification laws, sector-specific reporting — as additional extortion pressure. Documented in the underlying reporting in cases including the SEC complaint that ALPHV filed against MeridianLink.

Resilience-denial. See Recovery trap.

RSA. An asymmetric cryptographic algorithm based on the difficulty of factoring large integers. The dominant key-wrapper algorithm in modern ransomware. Believed, on current evidence, to be vulnerable to a sufficiently powerful quantum computer.

Segmentation. An architectural defense in which networks and identity domains are divided so that an attacker who compromises one segment cannot, from there, reach every other segment. A core defensive layer.

Session cookie. A small piece of authentication data that a browser stores after a successful login, used to keep the user logged in across page loads. Stolen session cookies can be used to bypass multi-factor authentication, since the session is already authenticated. The infostealer market specifically prioritizes session cookies.

Single Sign-On (SSO). An identity architecture in which a single authentication grants access to many applications. Increases convenience for users and risk concentration for defenders.

SLH-DSA. The NIST-standardized post-quantum digital-signature algorithm derived from SPHINCS+. Published as FIPS 205.

SSO exposure. The phenomenon in which infostealer-infected endpoints expose enterprise single-sign-on credentials. The reporting documents approximately sixteen percent of infostealer-infected endpoints exposing enterprise SSO in the period studied.

Symmetric encryption. Encryption that uses the same key for both encryption and decryption. AES is the standard symmetric algorithm in ransomware payloads.

Triple extortion. A multi-extortion model adding a third pressure layer — commonly customer or partner notification, or DDoS — beyond encryption and data-publication threat.

Validated access. Access listings that have been tested by the broker to confirm they still work, before being sold. Commands a price premium over unvalidated listings in the access economy.

Vishing. Voice phishing. Social-engineering attacks conducted by phone. Increasingly combined with voice-cloning technology to impersonate executives or trusted contacts. The Zscaler ThreatLabz reporting forecasts a substantial increase in voice-based social engineering across 2026.

Voice cloning. The use of AI models to reproduce a target person's voice from limited audio samples, used to make vishing calls more convincing. A core component of hyper-personalized social engineering.

White-label ransomware. A criminal franchise model in which a less-skilled operator uses a larger platform's payload, infrastructure, and negotiation systems under the smaller operator's own brand. DragonForce is the documented example in the underlying reports.

Zero-day. A vulnerability exploited before a patch exists. The ESXi zero-day exploitation through January 2026 is documented in the reports.

ZeroFox. The threat-intelligence vendor cited in the book for skepticism of the 2026 cartel signaling between DragonForce, LockBit, and Qilin.
