# Chapter 5: The Unbreakable Lock

*Post-Quantum Cryptography and the Coming Irreversibility Problem*

---

If we have backups, we're fine.

This is the assumption. The comfortable, widely held, professionally endorsed belief that sits at the center of most organizations' ransomware response plans. If the attackers lock your files, restore from backup. It costs time. It costs money. It is painful and disruptive. But it is recoverable. You do not need to pay the ransom if you have a clean copy of everything they encrypted.

This assumption is being attacked from two directions simultaneously. And both attacks lead to the same place.

The first direction: a small but growing number of ransomware groups are beginning to incorporate cryptographic techniques designed to make encrypted files resistant to recovery not just today but under any future technological advance. Post-quantum cryptography — encryption so advanced that even a computer powerful enough to break every lock ever devised cannot open it — is migrating from the domain of national security agencies and academic cryptographers into the ransomware supply chain. The window for future cryptanalytic rescue, already narrow, is being closed.

The second direction: a large and rapidly growing number of ransomware groups have abandoned encryption entirely. They don't lock your files. They steal them. And then they threaten to expose them. The backup cannot protect you against a threat that doesn't target your files at all. It can only protect you against a threat that targets your operations. The criminals have noticed.

Both roads lead to the same destination: a world where the "we have backups" defense is increasingly irrelevant. Not because backups are bad. Because the threat has evolved past them.

---

To understand post-quantum cryptography, you first need to understand the cryptography it is designed to replace — and why that existing cryptography is at risk.

Modern encryption protects nearly everything in the digital economy. When you send a bank transfer, when your hospital records are transmitted, when your company's files are stored in the cloud — the protection in each case relies on mathematical problems that are extraordinarily difficult to solve with conventional computers. Factoring very large numbers. Computing discrete logarithms. These problems take so long to solve, with current hardware, that the encrypted data is effectively secure against any realistic attack.

Quantum computers — computing systems that exploit the properties of quantum mechanics to perform certain calculations at speeds impossible for conventional hardware — threaten to change this. For specific cryptographic problems, particularly the factoring and discrete logarithm problems that underpin most current encryption, quantum computers promise a dramatic speedup. A sufficiently capable quantum computer could break the mathematical locks protecting most current encrypted data in a fraction of the time it would take conventional hardware.

Sufficiently capable quantum computers of this kind do not yet exist. They remain, in 2026, a future technology — perhaps five years away, perhaps twenty. The uncertainty is genuine. But the threat is taken seriously enough that the National Institute of Standards and Technology, a U.S. government body that sets cryptographic standards, has been working for years on what are called post-quantum cryptographic algorithms — mathematical systems designed to resist attack even from quantum computers. Among the standardized results of this work is ML-KEM, also known by its earlier designation Kyber, in its most secure variant referred to as Kyber1024.

ENISA — the European Union Agency for Cybersecurity — has been urging organizations to begin planning quantum-safe migrations now, not because the threat is imminent but because the lead time required to migrate cryptographic infrastructure across large organizations is measured in years, not months. The organizations that wait until quantum computers are a confirmed reality will have missed the preparation window.

The same migration logic applies, in mirror image, to criminal actors who want to harden their ransomware against future cryptanalytic rescue.

---

Here is how post-quantum cryptography could be applied to ransomware encryption, and why it matters.

Current ransomware encryption works like this: the malware generates a unique encryption key for each victim — a long random number that is used to lock every file on the victim's systems. The files are encrypted quickly and reliably using this key. The key itself is then protected using asymmetric cryptography — a mathematical lock whose protection depends on the hardness of factoring or discrete logarithm problems. The attacker holds the mathematical "private key" that unlocks this protection; without it, the victim cannot recover the session key; without the session key, the files cannot be decrypted.

The encryption is already, for practical purposes, unbreakable with today's technology. The practical path to recovery — short of paying the ransom — is either to obtain the attacker's private key through law enforcement action or to restore from backup.

Post-quantum hardening would close the cryptanalytic gap that quantum computing might eventually open. The technical design, as analyzed in ENISA's guidance and assessed in reporting by ISACA, works as follows:

First, encrypt the victim's files using a fast symmetric cipher — AES or ChaCha20, which work the same in a post-quantum world as they do today. File encryption itself does not need to change.

Second, protect the encryption key using ML-KEM/Kyber1024, a post-quantum key encapsulation mechanism. This means that instead of wrapping the encryption key in a mathematical lock that a quantum computer could eventually pick, you wrap it in one based on mathematical problems that quantum computers, as currently understood, cannot efficiently solve.

Third, destroy all plaintext key material on the victim's system once encryption is complete. What remains is only the encrypted files and the cryptographic "capsule" containing the protected key. Without the attacker's private quantum-safe key, neither a current computer nor a future quantum computer would provide an obvious path to recovery.

Industry reporting has referenced the existence of ransomware families claimed to already incorporate ML-KEM/Kyber1024. This claim should be treated with appropriate epistemic caution — it is an emerging assertion in industry reporting, not a primary-source confirmed fact. What is not in dispute is the technical feasibility: the implementation logic is sound, the underlying mathematical libraries are freely available, and the incentive for sophisticated ransomware operators is clear. If the claim proves accurate even in isolated instances, the appropriate response is to treat it as an early warning, not a curiosity.

ISACA's analysis is clear about the practical constraints that currently limit broader criminal adoption of post-quantum cryptography. Implementation is non-trivial: cryptographic engineering is difficult, and poorly implemented PQC can introduce bugs that break the encryption campaign entirely, or expose key material in ways that defeat the purpose. Payload size increases. Performance overhead exists. And perhaps most importantly: most victims currently pay ransoms based on operational pressure, not on concerns about future cryptanalysis. The economic case for PQC, from a purely criminal perspective, is strongest for sophisticated operators targeting high-value victims with long-term sensitivity — intelligence agencies, pharmaceutical companies, financial institutions — rather than for the average affiliate targeting a mid-sized manufacturer.

But "not yet mainstream" is not the same as "not a threat." ENISA's position — that organizations must begin quantum-safe migration now, not after quantum computers arrive — reflects a planning horizon of years, not months. The same logic applies in reverse. Defenders who assume they can address the PQC ransomware threat after it becomes widespread have already made the mistake that costs them.

---

While the post-quantum cryptography story is still in early chapters, the data-only extortion story is already being written — at scale.

DeepStrike's analysis of the ransomware landscape found that approximately 77 percent of ransomware intrusions now involve data exfiltration. Not some incidents. Not the sophisticated ones. Seventy-seven percent. Data theft has become the default behavior of a ransomware intrusion, not a specialized variant. The question for defenders has shifted from "will they steal our data?" to "did they steal all of it, or only some?"

This statistic matters because it reveals the true operational logic of modern ransomware. Attackers are not primarily interested in locking your files. They are primarily interested in your data. The encryption is leverage — a way to make the operational disruption acute and immediate. But the data is the enduring asset. The data can be threatened, leaked partially, leaked fully, sold, shared, weaponized against regulatory bodies, weaponized against customers, weaponized against business partners. The data generates leverage that persists long after any encrypted files have been restored from backup.

And then there is the Clop model, which takes this logic to its endpoint.

Clop is a ransomware group that has pioneered what researchers call "data-only extortion" — intrusion and data theft without ransomware encryption at all. Clop's operational pattern involves mass exploitation of vulnerabilities in widely used file transfer and collaboration software: gaining access to thousands of organizations simultaneously through a single software flaw, stealing data from all of them, and then initiating a staged public disclosure campaign. Victims receive demands. If they don't pay, their data appears on Clop's leak site, in partial releases that escalate to full publication.

No encryption. No operational disruption beyond the initial intrusion. Just data, and the threat of exposure.

The victim's backup is completely irrelevant. There is nothing to restore. The attack did not target files; it targeted data that was already being used, already accessible, already in motion. The backup represents the past; the stolen data represents the present. These are not the same thing.

DeepStrike and Chainalysis both documented the scale of the resulting extortion market: more than 7,500 organizations were publicly listed on ransomware data leak sites in 2025, representing a 50 to 58 percent year-over-year increase depending on the counting methodology. The leak site — the public pillory where criminals post victims' names, shame them before the entire internet, and release their stolen data in stages — is not a last resort. It is the primary extortion infrastructure of a significant and growing portion of the ransomware economy.

---

The four extortion archetypes now operating in the criminal market illustrate the range of the threat:

Traditional ransomware is the model most people know: encrypt the files, demand payment for the decryption key. Restore from backup if you have it; pay if you don't. This model still exists and still dominates many attack campaigns.

Double extortion adds data theft to the encryption event: encrypt the files and steal the data. Now the victim faces two threats simultaneously — operational disruption (file encryption) and data breach (exposure of sensitive information). Backup addresses only the first.

Multi-extortion adds additional pressure vectors to the two above: public naming on a leak site, regulatory notification threats, customer or partner notification, DDoS attacks against public-facing infrastructure. Each additional threat vector increases the coercive pressure and reduces the effectiveness of any single defensive measure.

Data-only extortion abandons encryption entirely. Steal the data; threaten to expose it. Operate without leaving the operational footprint of a ransomware deployment. Harder to detect, faster to execute, and immune to backup defenses.

The direction of travel is clear. The criminal market is not converging on any single model — different operators pursue different strategies. But the strategic trend is away from encryption as the primary coercive tool and toward data as the primary coercive asset. Encryption is becoming optional. Data theft is not.

---

The convergence of Chapter 4's subject and this chapter's is the most dangerous scenario in the current threat landscape.

Agentic AI — the autonomous, machine-speed operational capability described in Chapter 4 — dramatically accelerates the deployment of any ransomware attack. AI-assisted reconnaissance identifies targets faster. AI-generated phishing achieves higher click rates. AI-driven lateral movement executes faster than human operators working manually. The attack timeline compresses.

Post-quantum cryptography, applied to that accelerated attack, produces encrypted files that are resistant to recovery not just today but under any anticipated future technology. The AI gets you in fast; the PQC makes getting out expensive, possibly permanently.

Data-only extortion, applied to that same accelerated attack, produces a threat that the backup doesn't touch. The AI gets you in fast; the data is gone before you know it; the threat of exposure is the weapon.

Together — AI acceleration, PQC hardening, data exfiltration as the primary coercive asset — these developments represent an attack architecture that is faster to deploy, harder to remediate, and more resilient against future recovery than anything in the previous history of ransomware.

---

Post-quantum ransomware is the future. Data-only ransomware is the present. Organizations that understand neither are defending yesterday's threat.

---

The practical implication of the parallel-track analysis — traditional encryption, PQC-hardened encryption, and data-only extortion all operating simultaneously in the same criminal market — is that defenders cannot build a single coherent response to the encryption problem. They must build a coherent response to the extortion problem, of which encryption is only one component.

This is a significant conceptual shift. For most of the ransomware era, the primary defensive frame was: keep backups, patch vulnerabilities, block malware. These defenses are oriented toward the encryption event as the primary threat. Restore the files, recover the systems, return to normal.

The data-only extortion model — pioneered by Clop, adopted by a growing portion of the criminal market — operates entirely outside this frame. There is no encryption event to defend against. There is only data theft and the threat of exposure. Against this threat, backups are irrelevant. Patching helps only at the initial access stage. Malware blocking is less relevant when the attacker uses legitimate cloud services and administrative tools rather than traditional malware.

The defense against data-only extortion is a different category of response entirely: preventing the data theft in the first place (identity security, access governance, network segmentation); reducing the concentration of sensitive data that would be most damaging if exposed (data minimization, classification, controlled access); and preparing for the extortion scenario if theft cannot be prevented (the governance preparations described in Chapter 8).

---

The Clop model deserves additional attention, because it represents the most operationally advanced form of data-only extortion in the current landscape.

Clop's pattern involves mass exploitation of vulnerabilities in widely used file transfer platforms: software that organizations use to send and receive large volumes of sensitive data between themselves and their partners, clients, and regulators. These platforms are, by their nature, rich with exactly the data that creates maximum extortion leverage: legal documents, financial records, personal data, medical information, regulated communications.

By exploiting a single vulnerability in a widely deployed platform, Clop can simultaneously access data from hundreds or thousands of organizations. The intrusion itself may be completed in hours. The extortion campaign that follows may span months, with organizations being notified sequentially, their data released on a rolling schedule designed to maintain media attention and regulatory pressure across an extended period.

This is not a one-to-one criminal relationship between a single attacker and a single victim. It is a one-to-many exploitation event, followed by a managed extortion campaign at scale. The economics are strikingly efficient: one successful exploitation of one vulnerability yields access to data from an entire ecosystem of organizations, each of which then becomes an independent extortion target.

The defensive implication is that organizations which rely on file transfer platforms — and in the modern business environment, most organizations do — must treat those platforms as high-risk data concentrations. What data flows through these systems? Who has access to it? How would the organization respond if that data were stolen and threatened with exposure? These questions should have answers before an incident, not during one.

---

One additional concept mentioned in the research deserves a brief treatment: "Store Now, Decrypt Later."

Nation-state intelligence agencies have been documented — through defections, technical analysis, and intelligence reporting — as harvesting encrypted communications and data today with the intention of decrypting them once quantum computing capability develops. The logic is simple: data that is secret today may remain strategically valuable for decades. An encrypted intelligence communication that cannot be read today may be readable in ten years, when the cryptographic protection it relies on has been made obsolete by quantum computing advances. Collecting it now costs little; the potential future value is significant.

Criminal actors could apply the same logic in a more targeted way. Encrypt a victim's most sensitive data — trade secrets, privileged legal communications, classified research — with PQC-hardened ransomware today, and hold the cryptographic leverage indefinitely. The payment demand remains outstanding, backed by the threat that even future technological advances will not make the encrypted data recoverable. The criminal organization has created not just a current extortion event, but a permanent hold over the victim's most sensitive information.

This is speculative as an operational criminal strategy in 2026 — there is no documented evidence of ransomware operators pursuing this model at scale. But the combination of PQC-hardened encryption and indefinite retention of stolen data is technically feasible, and the strategic logic, applied to sufficiently valuable targets, is coherent. It should be part of any serious threat modeling for organizations with genuinely long-term sensitive data.

---

Before the attack can threaten to expose your data, it has to find the data worth threatening you with. It has to understand your organization: what you run, what you value, who administers your systems, where your backups live, how your identity infrastructure is constructed.

Chapter 6 explains exactly how attackers choose their targets — and what they're really after.

---

## What 77 Percent Actually Means

The statistic is clean. Seventy-seven percent of ransomware intrusions now involve data exfiltration, according to DeepStrike's analysis. GuidePoint GRIT's reporting on leak site activity confirms the scale: the data extortion economy is not a niche — it is the dominant operational logic of modern ransomware. But the statistic flattens something that deserves to be seen in full resolution. What does it actually mean for an organization to have its data stolen in a ransomware intrusion? What, precisely, gets taken?

Most people picture files. Documents, spreadsheets, PDFs. The contents of shared drives. Financial reports. Client contracts. These do get stolen. But they are the least dangerous component of what modern exfiltration tools actually collect.

The more damaging category is live credential material. When an attacker's tooling sweeps a compromised environment, it does not stop at the file system. It looks for browser credential stores — every saved password in Chrome, Firefox, Edge. It harvests active session tokens: the authentication cookies that allow your cloud services, your SaaS applications, your administrative consoles to recognize your device without requiring a new login. It finds OAuth tokens and API keys cached in configuration files, development environments, and CI/CD pipelines. These are not static files that become irrelevant when you restore from backup. They are live credentials that continue to function after the intrusion is over, until they are individually identified and revoked. An attacker who has stolen your Azure AD session tokens does not need your password. They are already inside your identity infrastructure, and restoring your file server does nothing about it.

Beyond live credentials, the exfiltration typically captures database contents — not the database application, but the records inside it. Customer tables. Employee records. Transaction histories. The full contents of whatever structured data stores were accessible from the compromised environment. Email archives, where they can be accessed, go with them: years of internal communications, executive correspondence, M&A discussions, legal advice, HR grievances, confidential board communications. HR records are a specific high-value category — salary data, performance reviews, disciplinary records, accommodation requests, benefit enrollment details — because their disclosure creates acute personal harm and regulatory liability simultaneously.

What this inventory reveals is that an organization suffering a full-scope ransomware exfiltration has not experienced a file theft. It has experienced a comprehensive intelligence harvest of its operational state at the moment of intrusion.

---

## The Half-Life Problem

Different categories of stolen data have different half-lives — the period over which they remain damaging.

Some stolen data expires quickly. Active session tokens, if identified and revoked within hours, lose their value. Credit card numbers captured from a payment system become less useful as cards are cancelled. This is the category where speed of detection and response can meaningfully limit the harm.

Other data has a half-life measured in years. Trade secrets — product formulations, manufacturing processes, algorithm designs, client acquisition strategies — remain valuable to competitors and adversaries for as long as the underlying knowledge advantage lasts. A pharmaceutical company's pre-approval research doesn't expire when the trial concludes; it expires when the product is superseded. Privileged legal communications retain sensitivity across the lifespan of the litigation they concern. Strategic planning documents remain embarrassing and damaging long after the plan has been executed or abandoned.

Patient records occupy a particularly cruel position: they are immediately damaging to the individuals whose data is exposed, and they remain sensitive — in terms of identity theft risk, insurance fraud risk, and personal exposure — for the remainder of those patients' lives. There is no statute of limitations on the harm a stolen medical record can cause. Healthcare organizations that treat a ransomware event as a recoverable operational incident are systematically underestimating the nature of what has happened.

The half-life concept matters because it determines the shape of the threat. An organization that experiences data exfiltration is not managing a point-in-time event. It is managing a risk that unfolds across time — the risk that stolen data surfaces in a competitor's product, in a regulatory investigation, in a targeted phishing campaign against its own executives, in a secondary extortion demand six months after the initial incident appears resolved. Restoring from backup addresses the operational disruption. It addresses nothing about this ongoing exposure.

---

## The Backup Mindset's Blind Spot

The "restore from backup" defense is real and important. For traditional ransomware encryption — the operational disruption model — it works. Organizations with clean, tested, off-network backups have a genuine recovery path that does not require paying the ransom. This is not in dispute.

What the backup mindset fails to account for is the class of harm that backup cannot touch: the data that is no longer only yours. Once exfiltrated data has left your environment, restoring your environment does not retrieve it. The backup represents your state at a point in time. The threat of exposure represents something that exists outside your environment entirely, in the attacker's hands, on their infrastructure, under their control.

This is the logic that drives double and multi-extortion models documented by both DeepStrike and GuidePoint GRIT. The encryption is the opening pressure — the acute operational pain that creates urgency. The exfiltrated data is the enduring leverage — the threat that survives your recovery, your incident response, your restored operations, your public statement that the incident has been contained. Victims who restore from backup and refuse to pay discover that the conversation is not over. The leak site listing goes up. The partial disclosures begin. The regulatory notifications follow.

The criminals have understood something that many defenders have not yet fully internalized: the backup is not a defense against the extortion. It is a defense against one component of the extortion, in one of the four attack models currently operating in the market.

---

The attackers who execute these intrusions most effectively do not arrive at the targeting decision blindly. Before they move against an organization, they have already developed a working picture of what that organization holds, where the most sensitive data concentrates, how it is protected, and what its exposure would cost. They know — because they have researched it — that a healthcare provider's patient records have a different extortion value than a law firm's privilege logs, which have a different value than a defense contractor's technical documentation. They know which data has long half-lives and which creates immediate regulatory consequences. That understanding — of the data landscape, of what you have and why it matters — is precisely what shapes their targeting decisions. Chapter 6 explains exactly how attackers choose their targets — and what they're really after.
