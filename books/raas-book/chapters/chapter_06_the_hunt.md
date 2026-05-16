# Chapter 6: The Hunt

*Strategic Targeting and the Resilience Stack*

---

The attacker is not here for your files.

They already have your files. That happened earlier — in the first 72 minutes, while you were still asleep, or in a meeting, or fielding calls about an IT issue that nobody had yet identified as a ransomware attack. The data was copied and transmitted to servers you will never find before anyone on your side understood what was happening.

What the attacker wants now is something different. Something more strategic. They want to make sure you cannot function without them — and without paying.

This is the defining strategic shift in ransomware operations in 2025 and 2026: the attack has moved up the stack. Ransomware operators are no longer primarily targeting your files. They are targeting your ability to recover from the loss of your files. They are targeting the systems that would allow you to restore your operations, verify your identity, access your backups, coordinate your response, and keep your organization running while you work on remediation.

The term researchers use for this collection of systems is the resilience stack: the infrastructure of recovery. Backup systems. Identity and access management platforms. Virtualization and cloud management layers. Software-as-a-service platforms. Remote management tools. Third-party integrations. These are not the primary operational systems of your organization — they are the systems that allow your primary operational systems to be restored when something goes wrong.

In 2026, they are the primary target.

---

Unit 42's 2026 Global Incident Response Report — drawing on data from more than 750 major incidents across 50 countries and every major industry sector — established two statistics that define the current threat landscape.

Modern ransomware attacks are roughly four times faster than they were just two years prior. The fastest intrusions — from initial access to complete data exfiltration — are now measured in hours. In the fastest documented cases, attackers achieved full data exfiltration in as little as 72 minutes.

And nearly 90 percent of the cases Unit 42 investigated had one thing in common: they were enabled by what the report called preventable exposure gaps. Not elite tradecraft. Not sophisticated zero-day exploits requiring years of research and development. Preventable gaps — identity vulnerabilities, misconfigured systems, unmanaged access credentials — that gave attackers the entry they needed without requiring anything close to extraordinary capability.

These two statistics together tell a specific and actionable story. Attacks are not primarily succeeding because criminal operators are becoming dramatically more technically sophisticated. They are succeeding because the organizations they target are leaving predictable, correctable gaps in their defenses — and because the attackers have become expert at finding and exploiting those gaps at machine speed, before defenders can detect and close them.

---

If you want to understand how modern ransomware attacks are designed, you need to understand identity.

Identity is the connective tissue of the modern organizational digital environment. Your employees have identities — usernames, passwords, authentication credentials, session tokens, access rights. Your systems have identities — service accounts, application credentials, API keys, OAuth tokens. Your vendors and contractors have identities — their own credentials, plus trusted relationships with your systems. Your cloud platforms are organized around identity — determining who can access which resources, at what level of privilege, through which applications.

When an attacker compromises an identity — any identity — they do not merely gain access to what that identity can directly do. They potentially gain access to everything that identity is trusted to reach. And in modern enterprise environments, a sufficiently privileged identity can reach almost everything: production systems, backup systems, cloud platforms, SaaS applications, administrative consoles, network management tools.

Unit 42's finding that identity loopholes drove nearly 90 percent of investigated cases is not a description of a technical vulnerability — it is a description of an architectural reality. Identity is the master key. Every door in the building opens with it, once you have it.

Remote Monitoring and Management tools — the software that legitimate IT teams use to administer thousands of computers simultaneously, pushing software updates, monitoring system health, and executing management tasks across an entire network from a single console — are among the most powerful identity-adjacent systems in any organization's environment. In the hands of an IT administrator, they are essential operational tools. In the hands of an attacker, they are a master key for one-to-many command execution: one compromised credential used to push malicious commands to every machine in the environment simultaneously. Not one infection spreading slowly from machine to machine. One command, one action, every machine, simultaneously.

Software-as-a-service platforms — the business applications that organizations access through a browser rather than installing locally, the tools that have migrated from internal servers to cloud providers over the past decade — represent a different dimension of the same problem. Unit 42 found that 23 percent of investigated cases involved SaaS application data. OAuth tokens — the digital access passes that allow SaaS applications to communicate with each other and with internal systems — and API keys — the access credentials that automated processes use to connect cloud services — are becoming primary attack vectors.

Think of an OAuth token as a hotel keycard that never expires, grants access to multiple floors, and works in any hotel in the chain. Once an attacker obtains one, they blend seamlessly into the legitimate traffic of applications communicating with other applications. Detection is difficult because the access looks, at a surface level, like normal business operations.

The supply chain dimension extends this further. EPRS analysis warned that compromising a single technology provider can yield simultaneous access to numerous integrated client organizations. Over 60 percent of cloud-native vulnerabilities exist not in the primary software organizations deliberately deploy, but in transitive dependencies — the supporting libraries and components that other software relies on, often invisible to the teams that deployed the primary application. In some documented cases, these transitive components can execute malicious code during the software build process itself, before the application is even deployed.

A single compromised dependency. Across every organization that uses any software built with that dependency.

---

Who is being targeted?

The short answer: almost everyone. The longer answer matters, because it tells you something about why specific sectors face specific levels of pressure.

Manufacturing is the most targeted sector across Germany, Spain, France, and Italy — the largest economies in the European Union — according to EPRS data. The reasons are structural: manufacturing organizations operate under extreme downtime cost pressure. A production line that stops loses money in direct proportion to every hour it doesn't run. Complex supplier and customer dependencies mean that a disruption doesn't stay contained within one company — it cascades through supply chains, affecting partners, clients, and ultimately end consumers. Legacy operational technology infrastructure, deployed before cybersecurity was a primary design consideration, creates persistent vulnerability surfaces. Unit 42's case study of the global medical technology firm from the Prologue represents this pattern: manufacturing halted, distribution frozen, supply chains unraveling downstream.

Healthcare faces a different and in some ways darker calculus. Ransomware attacks against hospital systems create what EPRS documented as a potential safety crisis: postponed procedures, inaccessible patient records, unavailable medication data, overwhelmed alternative care pathways. The coercive leverage available against a healthcare organization is not just financial. It is moral. A hospital cannot treat "we will restore when we figure out the ransom situation" as an acceptable decision when surgical procedures depend on digital systems. The pressure to pay is not only economic — it is measured in patient welfare, possibly in patient lives.

Public administration and municipalities represent a third distinct profile. Sanxenxo, a city council in Spain, is among the cases documented in EPRS reporting. Municipal organizations typically have aging technology infrastructure, limited security investment compared to their private-sector counterparts, and a high public visibility that makes ransomware incidents politically costly. They also hold sensitive citizen data — tax records, benefits information, personal records — that creates significant regulatory and reputational exposure when it lands on a leak site.

The legal sector's exposure has increased at a startling rate. GuidePoint Security found that the legal sector experienced a 132 percent year-over-year increase in victims in 2025 — from 196 organizations to 455. The reasoning is straightforward: law firms hold privileged communications and sensitive client documents; they operate under professional obligations of confidentiality; and a data breach affecting attorney-client privileged material creates exposure that extends far beyond the immediate financial impact. The threat of publishing privileged communications is coercive leverage of a different order of magnitude than publishing an ordinary corporate database.

And then there are small and medium enterprises.

---

The "this only happens to big companies" assumption is wrong. It has always been wrong, but the data from 2025 and 2026 makes it undeniably wrong.

EPRS research found that approximately 80 percent of German cyberattacks in 2025 targeted small and medium enterprises. Not the largest corporations — the smallest organizations. A separate EPRS analysis of the Irish market found that 28 percent of Irish SMEs risk shutting down entirely after a single ransomware attack.

SMEs are not soft targets. They are high-probability monetization targets.

The economics are clear. Large enterprises have security operations centers, incident response retainers, legal teams, crisis communications firms, and board-level executives with experience managing exactly this kind of crisis. They have the organizational infrastructure to sustain a ransomware incident, negotiate effectively, and recover with some semblance of control. They are also likely to have cyber insurance, which adds another dimension of support.

SMEs have none of this. When a ransomware attack hits a 50-person manufacturing company or a 200-person professional services firm, the organization is suddenly facing a crisis for which it has no personnel, no playbook, and no institutional experience. The IT manager — who is also the database administrator, the help desk, and the person who orders supplies — is on a phone call with a ransomware operator's "customer service" channel at 2 in the morning. The choice to pay is not made by a crisis committee with legal and insurance counsel. It is made by whoever can reach whoever is in charge, under time pressure, without adequate information.

This is not a coincidence. It is a targeting strategy. Ransomware operators understand the economics of victim selection. SMEs pay at higher rates relative to demand, require less sophisticated intrusion to compromise, and mount less effective resistance than enterprise targets. Volume plus conversion rate equals revenue. The math points toward SMEs.

---

The strategic logic of targeting the resilience stack rather than operational systems is, when you understand it, chillingly elegant.

If an attacker simply encrypts your production systems, you have a path forward: restore from backup. It hurts, but you survive. The attacker's leverage is limited to the time and cost of that restoration process.

If an attacker encrypts your production systems and also destroys your backup infrastructure, you have no path forward except payment or months of rebuilding. The backup systems — the systems that exist specifically to protect you against this kind of disruption — are exactly what the attacker has targeted. The backup administrator's credentials are the ones they compromised. The backup job scheduler is the system they tampered with. The backup repository is the storage system they encrypted first.

The attackers who target backup infrastructure are not being unsportsmanlike. They are being rational. They are targeting the one system whose destruction maximizes their leverage. Every hour spent on backup infrastructure in the first minutes of an attack purchases hours of negotiating advantage later.

The same logic applies to identity systems. If an attacker disables or corrupts your identity and access management infrastructure — the systems that authenticate employees, authorize access, manage multi-factor authentication, and govern what each account can do — your organization cannot function. Your employees cannot log in. Your administrators cannot access the systems they need to remediate the attack. Your incident response team cannot investigate because they cannot reach the logs.

Ransomware in 2026 should be understood less as a malware problem and more as a deliberate sabotage campaign against the victim organization's ability to recover independently. The malware is the mechanism. The strategy is paralysis.

---

If you work for a small or mid-sized company, a hospital, a city council, or a law firm, you are not watching this from a distance.

You are inside the target perimeter.

---

The sector-specific targeting logic reveals something important about how the ransomware economy has evolved beyond opportunistic crime.

In the early era of ransomware, targeting was largely indiscriminate. Attackers sent malicious emails to millions of addresses and waited to see who clicked. The victim population was essentially random within the constraint of who received the email. The attack was a scatter-shot approach, and the return was proportionally unpredictable.

Modern ransomware targeting is anything but scatter-shot. The existence of the Initial Access Broker market — described in Chapter 3 — means that affiliates are typically purchasing access to pre-identified organizations rather than discovering victims through indiscriminate phishing. IABs categorize access by sector, company size, revenue, geographic location, and security posture. An affiliate who specializes in attacking manufacturing companies, or healthcare organizations, or legal firms, can purchase exactly the kind of access they need for their preferred targeting profile.

This means that the choice of victim is an upstream decision made at the Initial Access Broker level, not a spontaneous consequence of who happened to click a phishing email. The organizations that appear on ransomware data leak sites in 2026 are, to a significant degree, there because someone in the criminal supply chain assessed their coercion profile and determined they were worth pursuing. The assessment considers how much downtime costs them, how sensitive their data is, how well-resourced their incident response is likely to be, and how payment-receptive they are likely to be under pressure.

---

The resilience stack targeting pattern also has a temporal dimension that is easy to miss.

Attackers who target backup infrastructure, identity systems, and virtualization management planes are not primarily trying to destroy these systems. They are trying to disable them during a specific window: the window between when the ransomware payload is deployed and when the victim organization detects and responds to the attack.

If an attacker can disable the backup system's control plane — not necessarily delete the backups themselves, but prevent the backup administrators from accessing the backup system during the critical first hours of the incident — they have effectively extended their coercive window. The victim organization cannot begin the recovery process because the recovery tools are inaccessible. Every hour the victim spends trying to restore access to their backup infrastructure is an hour in which the attacker's leverage grows.

This is the architecture of a surgical strike against organizational resilience. Not a brute-force assault on the target's entire digital environment, but a precise targeting of the specific systems whose loss maximizes the victim's helplessness and minimizes the victim's recovery options.

Unit 42's finding that over 90 percent of breaches were enabled by preventable exposure gaps translates directly into this context: the identity exposures that allow attackers to reach backup administrators' credentials, the configuration gaps that allow remote management tools to be weaponized against the systems they were designed to protect — these are the specific vulnerabilities that enable resilience stack targeting. Close them, and the attacker's ability to execute this surgical strike is dramatically reduced.

---

The supply chain dimension of the attack surface deserves additional emphasis, because it is the dimension that most directly affects organizations that have otherwise invested heavily in their own security.

An organization can implement excellent endpoint security, rigorous identity governance, and robust backup practices — and still be compromised through a vendor whose software it relies on, through a supplier whose network it trusts, or through a service provider whose credentials have been stolen by a criminal supply chain.

EPRS's warning about ICT supply chain attacks is not theoretical. Real incidents have demonstrated that compromising a single widely-used software component, platform, or managed service can yield simultaneous access to hundreds of organizations whose own defenses are otherwise sound. The SolarWinds incident of 2020 — where malicious code was inserted into a widely-deployed network management software update — is the canonical example at the nation-state level. The same logic applies at the criminal level.

Organizations that have invested in their own security but have not assessed the security posture of their critical technology vendors and service providers have secured their own front door while leaving the loading dock unguarded. Third-party security assessments, contractual security requirements in vendor relationships, and monitoring for anomalous access through trusted third-party channels are not optional extras. They are the necessary complement to internal security investment.

---

The attacker has disabled your ability to recover independently — the backup infrastructure is compromised, the identity fabric is disrupted, the production systems are locked — and the demand has arrived. What happens next is the subject of one of the most psychologically engineered pressure systems ever devised.

Chapter 7 will show you what that looks like from the inside.

---

The 28 percent figure deserves to be read slowly.

EPRS analysis of the Irish SME landscape found that more than one in four small and medium enterprises risk shutting down entirely after a single ransomware attack. Not losing a quarter, or a rough trading year from which recovery is possible. Shutting down. Permanently. Ceasing to exist as a functioning organization.

Statistics, by their nature, compress the human content out of a situation. So consider what "shutting down" looks like from the inside of one of those organizations.

A 60-person precision engineering firm. Family-owned, third generation. The founder's grandfather built it after the war with two lathes and one contract. His son expanded it into a regional supplier. His daughter brought it into the digital age — computerized machining, cloud-based inventory management, customer portals, electronic invoicing. She hired specialists. She grew the client list. She made payroll every month for twenty-three years without missing a cycle.

On a Wednesday morning, none of it works. The machines still run, but the design files are locked. The production schedule exists only on screens nobody can access. The inventory system is down. The customer portal is dark. The backup drive — the one the IT contractor set up eighteen months ago — connects to a management console that hasn't responded since Tuesday night. The ransom demand arrived overnight: 95,000 euros in Bitcoin, a 72-hour deadline, and a polite note explaining that the counter will be reset to 48 hours if law enforcement becomes involved.

Twenty-three employees are standing around waiting for someone to tell them what to do. There is no crisis committee. There is no incident response retainer. There is no legal team on call. There is the owner, a phone pressed to her ear, trying to reach an IT consultant who is three hours away and has never handled this before either.

Three weeks later, the firm enters voluntary liquidation. The ransom went unpaid — the organization couldn't verify it would actually restore access, and the cash reserve couldn't survive the liquidity hit anyway. Two of the twenty-three employees find positions quickly. The rest enter a regional jobs market that is already tight. The manufacturing contracts migrate to competitors. The supplier relationships, built over decades through personal trust and reliable delivery, dissolve. The firm that shaped metal parts for clients across four countries and put food on twenty-three tables closes without ceremony, because a criminal enterprise identified it as a high-probability monetization target and acted accordingly.

This is what "shutting down" means. Not a statistic. A community losing an employer. A family losing the thing it built. Two dozen people absorbing a shock they had no way to prevent and no vocabulary to explain.

---

Now scale that picture to the statistical reality.

When EPRS reported that approximately 80 percent of German cyberattacks in 2025 targeted small and medium enterprises, they were not describing an anomaly. They were describing the operational norm of the modern ransomware economy. Germany has more than 3.5 million small and medium enterprises. They employ roughly 55 percent of the country's workforce. They generate nearly half of total business revenue. They are not the background of the German economy; they are the German economy, in the same sense that the aggregate of similar firms constitutes the functioning foundation of most European economies.

When 80 percent of cyberattacks target this population, the consequences are not contained to individual balance sheets. They aggregate into something with systemic weight: disrupted supply chains, reduced investment capacity, lost employment, diminished tax revenues, and an underlying corrosion of the organizational confidence that sustains economic activity. Ransomware is not merely extracting money from businesses. At this scale, it is extracting stability from economies.

This is not hyperbole. The EPRS research that documents these figures frames ransomware as a threat to economic security — not metaphorically, but structurally. SMEs operate with thinner margins, smaller cash reserves, and less institutional resilience than their enterprise counterparts. A shock that a large corporation can absorb through financial engineering and organizational depth can be a terminal event for a firm operating with two months of payroll in reserve. The systematic targeting of this population by a sophisticated criminal supply chain — one that has deliberately selected SMEs because of their limited capacity to resist — is the targeting of the economy's most vulnerable load-bearing structure.

The scale of this problem means that it cannot be solved by individual firms hardening their own defenses, though that remains essential. It requires the kind of coordinated regulatory and enforcement response that EPRS has been pushing into European policy frameworks: mandatory baseline security standards, improved incident reporting to enable aggregate threat intelligence, law enforcement cooperation that can disrupt criminal infrastructure rather than merely prosecute individual cases after the fact.

The ransomware economy is not a collection of isolated crimes. It is a system, operating at industrial scale, against organizations that were never designed to absorb its pressure.

---

Which brings us back to the owner standing in the wreckage of her engineering firm, phone in hand, reading a ransom note for the third time.

The demand has arrived. The clock is running. And the operators behind this attack are not waiting passively for her to decide. What follows is a process — methodical, psychologically calibrated, and deliberately engineered to narrow her options down to one.

Chapter 7 will show you what that pressure campaign looks like from the inside.
