# Chapter 8: The Reckoning

*What Survival Looks Like*

---

Return, for a moment, to that factory.

The floor is silent. Workers who arrived for their shifts are standing at machines that won't respond, staring at screens that display nothing. The IT supervisor who noticed the frozen cursor at 6:47 a.m. is now five hours into a crisis she did not train for, fielding calls from executives who want answers she doesn't have, while somewhere on a server she cannot reach, a ransom note glows on a screen that nobody in her building controls anymore.

The question every reader is now asking is the question she was asking: what should they have done differently?

The answer is the subject of this chapter. Not a simple answer, and not a comfortable one. But an honest one, grounded in the specific threat that the previous seven chapters have documented. And it begins with a reframe that changes everything.

---

Stop thinking about ransomware as a malware problem.

Ransomware is not primarily a technology problem. It is an organizational resilience problem. The attacks that succeeded — the 2,122 organizations publicly listed in Q1 2026, the 7,500-plus organizations named on data leak sites in 2025, the factories silenced and hospitals disrupted and SMEs destroyed — did not succeed primarily because the criminals were technically brilliant. Unit 42's 2026 Global Incident Response Report found that over 90 percent of the breaches they investigated were enabled by preventable exposure gaps. Not zero-day exploits. Not classified attack tools. Preventable gaps — identity vulnerabilities, misconfigured systems, unmanaged credentials — that a security-conscious organization could have closed.

This is the most important statistic in this book. Over 90 percent of breaches enabled by preventable exposure gaps. Not because the attackers were unstoppable. Because the targets made it easy.

That means the situation, as bad as it is, is not hopeless. It means the organizations that choose to address those gaps — systematically, seriously, with appropriate investment — can meaningfully change their exposure profile. They will not be immune. No organization is. But they can be genuinely harder targets, and in a criminal market where the economic logic points toward attacking the easiest available victims first, being genuinely harder is materially protective.

The organizing framework for everything that follows is what this chapter calls the extortion-resilience model. Not the ransomware-recovery model — which focuses on restoring encrypted files — and not the prevention model alone — which focuses on stopping intrusions before they begin. Both of those are necessary but insufficient. The extortion-resilience model asks a different question: how do we survive the attack that will happen — including the psychological pressure campaign that follows it — in a way that preserves our ability to function and limits the harm?

Organizations that are building for ransomware recovery are preparing for last year's threat. Organizations building for extortion resilience are preparing for the threat that exists right now.

---

Identity is where the threat enters, as Chapter 6 established. Identity is therefore where the defense must be strongest.

Mandiant's M-Trends 2025 report, grounded in frontline incident response data from the cases they investigated, was specific about what works. The most impactful single credential defense is phishing-resistant multi-factor authentication. But not all multi-factor authentication is equal, and this distinction matters enormously.

Standard multi-factor authentication — the system where logging in requires both a password and a code sent to a phone via text message — has a known vulnerability. Attackers in the middle of the authentication transaction can intercept both the password and the code, passing them to the legitimate site in real time while simultaneously establishing their own authenticated session. This is called an adversary-in-the-middle attack. Organized criminal groups, including UNC3944 as documented by Mandiant, are specifically designed to defeat standard multi-factor authentication at scale.

AiTM-resistant multi-factor authentication — authentication-in-the-middle-resistant, to use the security industry's language — uses hardware security keys or device-bound mobile authenticators that generate cryptographic proof tied to the specific website being accessed. This proof cannot be captured and replayed by an attacker intercepting the authentication transaction, because it is mathematically bound to the legitimate site's cryptographic identity. An attacker who intercepts the authentication cannot use what they captured to authenticate to the real site.

Hardware security keys cost roughly fifty dollars per unit. They are the single most impactful security investment per dollar available to most organizations. They cannot be phished. They cannot be socially engineered away from a helpdesk. They cannot be intercepted in transit. For the most privileged accounts in any organization — administrators, executives, finance staff — hardware security keys should be treated as non-negotiable.

This defense extends beyond login authentication. Session cookies — the temporary credentials that browsers use to maintain a logged-in state after authentication — are primary theft targets for infostealer malware. The credential vacuum cleaners of Chapter 3 specifically harvest session cookies because they allow an attacker to bypass authentication entirely, inheriting an already-authenticated session without needing the original credentials. Organizations must implement cookie expiration policies that limit the useful lifetime of stolen sessions, monitor for anomalous session activity across users and systems, and deploy detection for the specific infostealer families documented by Mandiant — VIDAR, RISEPRO, REDLINE, RACCOON STEALER, LUMMA, METASTEALER — that feed the criminal credential supply chain.

Service desks — the internal IT helpdesks that reset passwords, unlock accounts, and process authentication exceptions — are attack surfaces in their own right, as UNC3944's social engineering campaigns demonstrated. Service desk staff who receive phone or chat requests to reset multi-factor authentication for privileged accounts should be required to verify identity through channels independent of the communication the request arrived through. A call asking for an MFA reset should require a verification process that a caller cannot fake by simply knowing the target employee's name and job title.

Contractor and vendor access is one of the highest-risk surfaces in any organization's identity landscape. The Snowflake breach described in Chapter 3 was powered by credentials collected from a contractor's personal device. Organizations must audit which vendors and contractors have standing access to internal systems, implement network segmentation that limits what contractor credentials can reach, require managed devices for contractor access to sensitive systems, and monitor for the use of corporate credentials from unusual locations or devices.

---

Backups are only as resilient as the identity infrastructure that administers them.

This is the insight that the resilience stack discussion in Chapter 6 makes necessary: an organization that has invested in backups but not in identity security may discover, during a ransomware incident, that the attackers compromised the backup administrator's credentials and used them to tamper with, encrypt, or delete the backups before the ransomware payload was deployed.

The principle of immutable backups addresses this directly. An immutable backup is a copy of data that cannot be modified or deleted — not by an attacker who has compromised an administrator account, not by ransomware with elevated system privileges, not even by a legitimate administrator acting under duress. Immutability is enforced at the storage infrastructure level, through technical controls that prevent any modification command from succeeding regardless of who issues it.

Immutable backups, stored in isolation from the primary production environment — ideally offline or in a separate, air-gapped environment with its own access controls — are the foundation of genuine recovery capability. They do not help against data-only extortion, as Chapter 5 established. But they make the encryption component of a ransomware attack reversible without payment.

The other half of the backup equation is testing. Many organizations maintain backups without ever testing whether they can be successfully restored under realistic conditions. A backup that has never been recovered from is not a recovery capability — it is an assumption. Organizations must regularly execute full restoration exercises, including restoring systems to functional states from backup alone, to verify that the capability is real.

---

Software-as-a-service platforms — the browser-accessed business applications that organizations now depend on for email, file sharing, collaboration, customer relationship management, financial systems, and dozens of other functions — require the same security rigor applied to internal infrastructure. They are often treated as external "safe" services that exist outside the organization's security perimeter. They are not. They are extensions of the internal attack surface.

OAuth tokens and API keys — the access credentials that allow SaaS platforms to communicate with each other and with internal systems — should be inventoried, assessed for privilege level, and governed with the same controls applied to production user credentials. Tokens with broad permissions that are never revoked represent an expanding, often invisible attack surface. Twenty-three percent of Unit 42's investigated cases involved SaaS application data — evidence that this surface is being actively targeted.

Third-party integrations — the connections between SaaS platforms and other services, the automated workflows that move data between systems, the supplier and vendor portals that access organizational resources — each represent a trust relationship that an attacker can potentially exploit. Organizations that understand which third parties can reach which internal systems, under what conditions, and with what level of access, are meaningfully better positioned than those that have deployed integrations without subsequent governance.

---

All of the technical defenses described above — identity protection, backup integrity, SaaS governance — are necessary. They are not sufficient. Because even an organization that implements them rigorously may still find itself receiving a ransom note one Tuesday morning.

The extortion pressure campaign that Chapter 7 described in detail is not primarily a technical attack. It is a psychological and governance attack. It targets decision-making processes — legal, executive, communications, insurance, regulatory — that are not hardened by firewall configurations or backup policies. Organizations that prepare specifically for the post-breach extortion scenario are in a fundamentally different position when the ransom note arrives.

Preparation for extortion means: knowing, before the incident, which executive makes the ransom payment decision and under what conditions. Knowing which legal counsel handles ransomware incidents, and having them on retainer. Knowing which incident response firm will be called, and having a pre-signed engagement agreement. Knowing what the organization's communications posture will be in the first 24 hours — what to say to employees, customers, regulators, and potentially media. Having a tested communication channel for executive coordination that does not depend on the organizational email and collaboration systems that may be compromised.

It means monitoring data leak sites for the organization's name. Not as an exotic security capability, but as a standard operational function equivalent to monitoring for the organization's name in news media. Knowing when a criminal group has listed your organization is better than finding out from a journalist who has already published the story.

It means reducing concentrations of sensitive data that have no operational necessity. Files that are collected and stored because they might be useful someday represent extortion exposure. If the data doesn't need to exist, the threat associated with its exposure doesn't exist either.

For executives specifically: tabletop exercises that simulate the moment the ransom note arrives. Not a seminar about ransomware. A scenario-based exercise where the specific people who will be in the room during an actual incident work through a simulated incident in real time — making the decisions, experiencing the time pressure, discovering where the governance process breaks down before it breaks down in a real crisis.

---

For small and medium enterprises, the full enterprise security program described above may feel unreachable. But the most impactful measures are not expensive.

Phishing-resistant multi-factor authentication is available from major identity providers at low or no cost for many accounts. A 50-person company can implement hardware security keys for its most critical accounts — the ones with access to financial systems, administrative consoles, and backup infrastructure — for less than the cost of a single day's productivity lost to ransomware incident response.

Cloud-based backup with versioning — the ability to restore files from multiple historical points in time — is available from major cloud providers for modest cost. It is not equivalent to a fully immutable enterprise backup solution, but it provides meaningful protection against the ransomware scenario where attackers encrypt current files but cannot reach cloud-stored historical versions.

Basic network segmentation — ensuring that a compromised endpoint cannot directly communicate with backup systems, administrative consoles, or other sensitive infrastructure — reduces the ability of an attacker who has gained access to one part of the environment to immediately reach the parts that matter most.

Vetted incident response retainers — a contract with a cybersecurity firm that includes access to rapid-response services in the event of an incident — can reduce the chaotic improvisation that characterizes SME incident response, where organizations are typically calling unfamiliar vendors at 2 in the morning under conditions of maximum stress.

EPRS research found that 28 percent of Irish SMEs risk shutting down after a single ransomware attack. That statistic represents the catastrophic cost of no preparation. The difference between an organization that survives a ransomware incident and one that doesn't is rarely the sophistication of its security program. It is almost always the presence or absence of the fundamentals.

---

Law enforcement disruption works. Temporarily.

Operation Cronos dismantled LockBit's infrastructure in early 2024 and created a period of reduced activity from that specific group. As Chapter 1 documented, LockBit was back in the global top tier by Q1 2026. Disruption is not elimination. It is a time delay — meaningful, worth pursuing, but not a solution.

International law enforcement cooperation is the most effective tool available at the structural level, and it requires sustained political will across multiple jurisdictions. Criminal groups routinely exploit jurisdictional complexity — operating from countries that lack extradition agreements with the countries where their victims are located, using money laundering infrastructure that spans multiple legal regimes.

Chainalysis's work demonstrates that attribution is improving. Investigators can now track ransomware groups not just by their malware signatures but by their negotiation patterns and their on-chain financial behavior — the specific paths by which ransom payments move through cryptocurrency networks. The technical capability for attribution is growing faster than the political and legal capacity to act on it. Closing that gap is a policy problem, not a technology problem.

Payment policy is among the most contested questions in ransomware policy, and the honest answer is that there are no comfortable positions. Paying ransoms funds criminal organizations, potentially violates international sanctions in some cases, and encourages future attacks. Not paying ransoms prolongs operational disruption and, in the data-only extortion context, does not prevent data exposure. Neither option is good. What organizations can do is ensure that the payment decision, if it is made, is made with full legal counsel, insurance consultation, and regulatory awareness — not improvised under the first night's time pressure.

---

Over 90 percent of the breaches that enabled the ransomware attacks of 2025 and 2026 were made possible by preventable failures.

The corporations behind these attacks did not win because they were brilliant. They built an efficient, consolidated, AI-augmented criminal economy — and then they targeted organizations that had left the doors open. Organizations that had not implemented phishing-resistant multi-factor authentication. That had not protected their backup infrastructure. That had not governed their SaaS access. That had never run an extortion-response tabletop exercise. That had treated ransomware as someone else's problem.

That can change. The preventable gaps are, by definition, preventable.

The question is whether we choose to prevent them — before the next Tuesday morning arrives.

---

A practical note on the economics of prevention, because the objection "we can't afford to do all of this" deserves an honest answer.

The measures described in this chapter are not uniformly expensive. Some are extremely costly — enterprise security operations centers, full-time incident response teams, sophisticated identity governance platforms. But many of the highest-impact measures are surprisingly affordable.

Phishing-resistant multi-factor authentication for the most critical accounts — finance, IT administration, executive leadership — can be implemented with hardware security keys at roughly fifty dollars per key. For a 200-person company with 20 critical accounts, that is a one-thousand-dollar investment that addresses the attack vector responsible for a significant fraction of all investigated intrusions.

Immutable cloud backup with versioning is available from major cloud providers at a cost that most organizations already spend on storage. The upgrade from "backup" to "versioned immutable backup" is often a configuration change and a modest price increase, not a fundamental new investment.

Basic contractor security hygiene — requiring managed devices for access to production systems, enforcing network segmentation that limits what contractor credentials can reach — is a policy decision as much as a technology investment.

The DLS monitoring capability — knowing when your organization is named on a criminal leak site — is available through commercial threat intelligence services at a range of price points, some accessible to SMEs.

The tabletop exercise — the single intervention most likely to reveal governance gaps before an actual incident — requires time and facilitation, not a technology budget. Organizations that cannot afford a commercial facilitator can run simplified self-directed exercises using publicly available frameworks.

The point is not that security is cheap or that the full program described in this chapter is affordable for every organization. It is that the marginal return on the first investments — the fundamentals — is extremely high, and those fundamentals are achievable at any organizational scale. The organization that has implemented phishing-resistant MFA, maintained immutable backups, and pre-designated its incident response decision-makers is dramatically better positioned than the one that has done none of these things, even if neither has a sophisticated security operations program.

---

The moral dimension of this threat deserves acknowledgment, even at the risk of stepping outside the analysis that has characterized the rest of this book.

When hospitals are targeted, patients face harm that extends beyond any financial calculation. When city governments are attacked, the essential services that citizens depend on fail. When manufacturers are disrupted, supply chains falter and workers lose income. When SMEs are destroyed by attacks they had no capacity to prevent, communities lose the employers that anchor them.

The ransomware economy is not, ultimately, a cybersecurity problem. It is a civilizational challenge: a global industry of organized crime that has grown powerful enough to impose significant harms on the systems that modern societies depend on for health, safety, and economic functioning. Individual organizations taking defensive measures is necessary but insufficient. Structural responses — international law enforcement cooperation, regulatory minimum security standards, serious engagement with the payment policy question — are also necessary.

None of these structural responses are sufficient on their own either. The problem requires action at every level simultaneously: individual organizations hardening their defenses, regulators setting and enforcing appropriate standards, law enforcement agencies cooperating across jurisdictions to impose real costs on criminal operators, and governments working together on the international dimensions of a criminal market that respects no borders.

The ransomware corporations described in this book have been growing for a decade. Reversing their growth — not eliminating them, but making their operations progressively less profitable and their attacks progressively more difficult — requires a sustained, multi-level response that has not yet fully materialized.

That response begins with the decision, made by individual organizations and individual policymakers and individual citizens, to treat this threat with the seriousness it deserves.

The preventable gaps are, by definition, preventable.

---

The question is whether we choose to prevent them — before the next Tuesday morning arrives. That is not a rhetorical question. It is a policy question, an investment question, and ultimately a question about what kind of future we are willing to accept.

---

Return, one final time, to that statistic. Over 90 percent of the breaches Unit 42 investigated were enabled by preventable exposure gaps. Sit with that number. Not as an indictment of the organizations that failed — most of them were under-resourced, under-warned, and operating in a threat environment that outpaced any reasonable expectation — but as a signal. A signal about what is actually possible.

The criminals won because they found open doors. Not because the doors were impossible to close.

That is the thing this book has been building toward. Not a roster of villains. Not a parade of catastrophes, though the catastrophes are real and the villains are real and neither should be minimized. The point is this: the ransomware economy is not a force of nature. It is a market. It runs on incentives, on efficiency calculations, on the simple criminal arithmetic of risk versus reward. And markets respond to friction. When targets become genuinely harder — when credentials are locked behind phishing-resistant authentication, when backups are immutable and tested, when incident response is pre-planned and rehearsed — the criminal arithmetic shifts. Not enough to eliminate the threat. Enough to redirect it.

Not every organization will make the changes described in these pages. Some will calculate that the probability of attack is too low to justify the investment. Some will be told by leadership that security is someone else's budget. Some will not make the changes until the Tuesday morning arrives, and by then it will be too late to make them. That is the tragedy embedded in this threat, and it is a tragedy that will keep recurring.

But some organizations will choose differently. They will harden their identities, protect their backups, prepare their people, and sit down at a table before the crisis and walk through what they will do when it comes. They will not be invincible. They will be harder. And in a criminal market built on the exploitation of the easiest available targets, being harder is survival.

The ransomware era will not end because the criminals run out of ambition. It will end — if it ends — because we run out of easy targets.

That is not a fate. That is a choice.
