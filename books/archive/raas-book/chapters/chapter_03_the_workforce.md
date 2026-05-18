# Chapter 3: The Workforce

*Criminal HR and the Gig Economy of Cybercrime*

---

In November 2020, a contractor working for a company that used Snowflake — one of the world's most widely deployed cloud data warehousing platforms — downloaded something on their personal computer. The exact circumstances are unknown. Perhaps it was a game. Perhaps pirated software. Perhaps something that presented itself as a useful utility. Whatever it was, inside it was an infostealer — a piece of malware that, upon installation, did something remarkably simple and remarkably destructive. It quietly catalogued everything on the machine: every saved password in every browser, every session token, every stored credential, every piece of authentication material the computer held.

Then it sent all of that to its operators.

The contractor's corporate login credentials — their username, their password, the authentication details that let them access Snowflake's systems on behalf of their employer — were harvested, packaged, and listed on a criminal marketplace. A buyer purchased them. Validated them. Confirmed they were still active. And four years later, in 2024, Mandiant's incident response team was investigating one of the most consequential cloud data breaches in recent history: an intrusion campaign against multiple Snowflake customer environments, tracked as UNC5537, that had used credentials previously exposed by six different infostealer malware families — VIDAR, RISEPRO, REDLINE, RACCOON STEALER, LUMMA, and METASTEALER — some of which dated back to that 2020 infection.

Not a single zero-day exploit. Not a nation-state actor with classified tools. A credential stolen four years earlier from a contractor's gaming computer.

Mandiant was explicit in its assessment: the scale of the campaign was a consequence of the criminal marketplace for stolen credentials, not of any advanced tradecraft. The attackers were not elite hackers. They were buyers. The damage they caused was not the result of technical genius. It was the result of organizational design — a supply chain that moved stolen credentials from malware on a contractor's personal machine to an active intrusion in a Fortune 500 cloud environment, in a process that required no single actor to be either particularly skilled or particularly creative.

This is how the ransomware economy actually works. Not through heroic criminal masterminds. Through labor specialization, market efficiency, and a level of organizational sophistication that most people associate only with legitimate industries.

---

The workforce behind modern ransomware operations is organized in concentric rings, each with a distinct function and a distinct relationship to the criminal enterprise at the center.

At the innermost ring are the core operators: the organization's leadership, in effect. These are the people who built and maintain the brand — the malware platform, the leak site, the payment infrastructure, the negotiation frameworks, the affiliate agreements. Core operators are not, typically, the people conducting intrusions. They have moved up the value chain. They are executives and product managers in a criminal platform company. Their job is to build and maintain the franchise, not to run any individual location.

The second ring is the affiliates. These are the operators who actually conduct attacks — researching targets, gaining access, moving through networks, stealing data, deploying ransomware. They bring intrusion capability. The platform brings everything else. As Chapter 2 established, affiliates are the franchisees. They pay into the system and extract revenue from successful attacks.

The third ring — and this is where the workforce story becomes genuinely surprising — is the vast ecosystem of external suppliers: specialists who are not formal affiliates but whose services are bought and sold in the criminal marketplace to support operations at every stage of the attack chain.

This third ring is where most of the actual labor is performed.

---

The credential supply chain begins with infostealers.

An infostealer is exactly what its name implies: a piece of software — sometimes delivered through malicious email attachments, sometimes hidden in pirated games or counterfeit software, sometimes embedded in malicious advertisements on legitimate websites — that, upon installation, silently vacuums up every piece of authentication material it can find on the infected machine. Think of it as an invisible vacuum cleaner, running continuously in the background, hoovering up passwords, session tokens, saved browser credentials, authentication cookies, corporate login details, and anything else that might prove useful to a criminal buyer.

The malware families involved in the Snowflake campaign — VIDAR, RISEPRO, REDLINE, RACCOON STEALER, LUMMA, METASTEALER — are not unique or exotic. They are widely available criminal products, sold or rented through criminal forums, operated at scale by thousands of actors who specialize in exactly this one function: credential collection. Some operators run these tools against millions of machines simultaneously, generating enormous volumes of stolen credentials that they then sell to buyers through structured criminal marketplaces.

The buyers are Initial Access Brokers. These are the real-estate agents of the criminal economy — specialists who aggregate, validate, and sell corporate network access rather than individual credentials. An Initial Access Broker doesn't use the stolen credential to attack anyone. They package it, assess it, and list it for sale with a description that would not look entirely out of place on a legitimate market listing: organization type, industry, estimated revenue, level of access available, geographic location, security controls in place. According to CYFIRMA's research, brokers categorize access by organization size, privilege level, geography, and security controls — the same taxonomy a legitimate commercial real estate agent uses to categorize property listings.

Buyers on the other end of these listings are typically affiliates or other criminal operators who need corporate network access and would rather buy a validated foothold than spend the time and risk developing one themselves. The transaction is clean and efficient. The foothold passes from the infostealer operator who collected it, to the Initial Access Broker who packaged it, to the affiliate who uses it to conduct an attack — and none of these actors needs to know anything about the others except what the marketplace requires. CYFIRMA's research indicates that the chain from infostealer infection to operational use can occur in under 48 hours — a directional observation about market speed, not a universal timing guarantee. The underlying dynamic is clear: in a mature criminal marketplace, validated access moves fast.

---

Imagine, if you will, a contractor at a mid-sized technology firm. On a weeknight, after the work day is done, he downloads what appears to be a cracked copy of a video game — a relatively common and seemingly low-stakes decision. Hidden in the game's installation package is REDLINE, one of the most widely distributed infostealer families in the world. REDLINE runs silently in the background while he plays. It locates his saved browser passwords, his stored corporate authentication credentials, his session cookies. It packages all of this and sends it to the criminal server that manages it.

Within 48 hours, his corporate credentials appear on a criminal marketplace. An Initial Access Broker has already validated them — confirming they work, confirming the level of access they grant, categorizing the company by size and industry. An affiliate finds the listing, recognizes the target as worth attacking, and purchases the access.

He goes into the office the following Monday. Nothing seems different. He doesn't know anything has happened. He won't know until, weeks or months later, his employer gets hit with a ransomware attack and he's asked to confirm whether he was using corporate credentials on personal devices.

The cartel profited from both. They needed neither his cooperation nor his knowledge.

---

If the infostealer pipeline represents the most mechanized end of the criminal workforce, the social engineering function represents its most human-intensive work — and the two exist at opposite ends of the same supply chain.

Social engineers are the con artists of the criminal economy. Their tool is not malware but conversation: the ability to persuade a human being to take an action they should not take, using only voice, text, or chat. In the ransomware economy of 2025–2026, this has become a distinct labor class — not technically sophisticated, but highly skilled in manipulation, confidence, and organizational intelligence.

Mandiant's tracking of a threat actor group designated UNC3944 illustrates how this works at its most refined. UNC3944 operated by targeting corporate IT helpdesks — specifically, by calling helpdesk staff and persuading them to reset passwords and multi-factor authentication for employees. The social engineers had what they needed to be convincing: they knew the employee's name, their position, their contact details, and enough organizational context to sound like a frustrated employee who just couldn't get into their account. The helpdesk representative — following normal process, trying to be helpful — reset the credentials for what appeared to be a legitimate employee.

Once those credentials were reset, UNC3944 used the resulting access to exploit single sign-on systems — the centralized login platforms that grant access to multiple applications simultaneously, the digital equivalent of a master key for an entire office building. They assigned the compromised accounts to cloud applications. They created virtual machines in cloud environments for follow-on operations. A phone call to a helpdesk had yielded administrative access across an entire corporate environment.

This is not technical wizardry. It is social skill, organizational research, and patience. The social engineer is cheap labor in the criminal economy — they need a script, organizational intelligence, and the nerve to make a convincing call. They do not need to write a single line of code.

Mandiant's analysis of cloud access compromise methods in 2024 is instructive: 39 percent of incidents were initiated through email phishing; 35 percent through stolen credentials; 6 percent through SIM swapping; 6 percent through voice phishing. Add those together and the picture is stark: identity and trust exploitation — not technical vulnerability exploitation — sat at the center of the majority of investigated cases. The criminal workforce's comparative advantage is not hacking. It is manipulation.

---

The insider threat dimension of the ransomware workforce is perhaps the most unsettling aspect of the entire ecosystem.

The conventional understanding of insider threats involves a disgruntled employee, a rogue contractor, someone with access who chooses to misuse it. That exists, and it is real. But modern ransomware cartels have developed something more systematic: workforce programs that deliberately embed criminal assets inside target organizations.

Mandiant's tracking of a threat actor group designated UNC5267 documented the operational signature of a practice that has become increasingly common: North Korean workers, operating under stolen or fabricated identities, securing legitimate employment at U.S. and international organizations. These individuals generate revenue for the state-affiliated criminal operation behind them while potentially providing access to the internal systems of their employers. They show up for virtual meetings. They use corporate communication tools. They have email addresses, Slack handles, performance reviews.

This is not opportunistic. This is organized criminal staffing, managed as a workforce function.

And then there is the category that doesn't involve any criminal intent at all: the contractor who downloaded the game. The employee who clicked a phishing link because it looked exactly like the right email from the right colleague. The worker who used their corporate laptop on a home network, or their personal laptop for work tasks, without realizing what they were giving away.

The criminal economy benefits from the active insider who knows what they're doing. But it benefits just as much — sometimes more — from the innocent contractor whose compromised device functions as an involuntary credential provider. The line between "recruited insider" and "harvested employee" is increasingly blurred. From the ransomware cartel's perspective, both provide the same asset: a valid key to a locked building.

Mandiant found that in several of the Snowflake-related investigations, the original infostealer infection had occurred on contractor systems used for personal activities — gaming, pirated software downloads, recreational browsing. The corporate credentials that powered the breach were collected from machines that had never been formally enrolled in any corporate security program, machines the company may not have even known were being used to access its systems.

---

Criminal organizations don't have HR departments in the conventional sense. There are no formal interviews, no employment contracts, no health benefits. But the functions that those institutions serve — recruiting, vetting, performance management, compartmentalization, discipline — exist in the ransomware ecosystem in informal but highly effective forms.

Recruiting happens through criminal forums, through demonstrated track records, through referral networks among trusted operators. An affiliate looking to join a program proves their value by demonstrating prior access, providing evidence of successful campaigns, or being vouched for by an existing trusted member. The screening is rigorous precisely because the stakes are high — an undercover law enforcement officer who makes it through affiliate onboarding can compromise an entire operation.

Vetting relies on criminal reputation: a currency that is real, valuable, and carefully maintained in the underground ecosystem. Operators who defect, who steal from affiliates, who cooperate with law enforcement, or who deliver poor-quality services are sanctioned — through denial of payment, through public exposure in criminal forums, through doxxing, through exclusion from future operations. These sanctions are enforceable because criminal reputation is the only currency the market accepts.

Compartmentalization is a security architecture as much as an HR practice. The affiliate who gains initial access typically does not know the identity of the core operator. The infostealer operator who sold the credentials does not know which affiliate bought them or which organization they targeted. The social engineer who reset the MFA credentials does not know what happened after the call ended. Each actor knows only what they need to know to complete their function. This limits the blast radius of any single arrest, cooperation, or leak.

In the legitimate corporate world, compartmentalization is described as need-to-know security policy. In the criminal world, it is the organizational design that allows an enterprise to survive even when individual members are compromised.

---

The full picture of the ransomware workforce is not what most people imagine. It is not a small group of elite hackers in a basement. It is an ecosystem of hundreds or thousands of workers — credential thieves, access brokers, social engineers, network intruders, data classifiers, negotiators — each performing a specialized function in a modular, efficient criminal supply chain.

Some of them are highly skilled. Most of them are not. Unit 42's research found that low barriers to entry allow criminals "at all skill levels" to participate. The ransomware economy has made most attacks accessible to the moderately capable, which is far more dangerous than a market limited to the technically elite. You do not need to be brilliant to steal and sell credentials. You do not need to be technically sophisticated to call a helpdesk and ask for a password reset. You need a script, a criminal marketplace account, and a tolerance for risk.

The most dangerous employee a ransomware cartel has may not know they're working for one.

---

The broader picture of the criminal labor market reveals something that is easy to miss when focusing on individual incidents: this is not a workforce that is diminishing. It is a workforce that is expanding, becoming more specialized, and becoming more efficiently organized.

Unit 42's research found that low barriers to entry allow criminals "at all skill levels" to participate in the ransomware economy. This is not an observation about declining criminal quality — it is an observation about market maturation. A mature market does not require every participant to be an elite practitioner. It requires specialization: actors who are very good at one specific function and can be slotted into the supply chain at the appropriate point.

The infostealer operator does not need to know how to conduct a network intrusion. The Initial Access Broker does not need to know how to develop ransomware. The affiliate does not need to know how to process cryptocurrency transactions. The social engineer does not need to understand cryptography. Each participant contributes their specific function, and the platform connecting them ensures that the output of each function feeds into the input of the next.

This is a supply chain in the fullest sense — not a metaphorical supply chain, but a literal one, with upstream suppliers, value-adding intermediaries, and downstream customers. The raw material is stolen credentials. The value-adding intermediary is the Initial Access Broker, who validates and packages those credentials into sellable access. The downstream customer is the affiliate, who converts that access into a monetized ransomware event. The platform operator takes their margin at the monetization stage.

At every link in this chain, specialization has produced efficiency. Infostealer operators run their operations at scale, infecting millions of machines and generating enormous volumes of credential data for the market. Initial Access Brokers provide quality validation services, filtering the credential market for actionable corporate access and presenting it in a form that reduces affiliate research costs. Affiliates deploy their intrusion capability against pre-validated targets rather than spending time finding and evaluating potential victims.

Mandiant's 2024 cloud access data captures the end result of this supply chain efficiency: phishing accounted for 39 percent of initial access; stolen credentials for 35 percent. Together, these two vectors — both identity-based, both dependent on the criminal supply chain described in this chapter rather than on technical exploit development — accounted for nearly three-quarters of investigated cloud access events. The vulnerability exploitation that dominates popular imagination of hacking is the minority. The supply chain that delivers credentials and social engineering is the majority.

---

The North Korean IT worker program represents a different but equally instructive dimension of the criminal workforce problem.

The broader ransomware and criminal ecosystem has overlapping interests with state-sponsored actors, and the workforce dynamics sometimes intersect. Mandiant's tracking of UNC5267 documented a practice where workers using stolen or fabricated identities secured legitimate employment — generating revenue for the criminal operation while potentially providing embedded access to the internal systems of their employers.

This is state-scale workforce management applied to criminal goals. The individuals involved appear, from the outside, to be ordinary remote workers: they show up for video calls, they produce work product, they have Slack handles and email addresses and performance review cycles. Inside, they are assets of an organization that has a very different purpose than their nominal employer understands.

The lesson is not that every remote worker is suspect. The vast majority are not. The lesson is that the insider threat model has evolved beyond the disgruntled employee or the opportunistic rogue contractor into something more deliberately managed and more difficult to detect through conventional insider-threat monitoring.

---

Understanding the criminal workforce is not merely academic. It points directly to the most effective defensive interventions — and suggests that many organizations are defending the wrong layer.

If over 90 percent of intrusions are enabled by identity and trust exploitation rather than technical vulnerability exploitation — as Unit 42's broader data suggests — then the organizations defending primarily through endpoint security, network firewalls, and vulnerability patching are prioritizing the minority of the attack surface. The majority of the attack surface is identity: the credentials that grant access, the tokens that maintain sessions, the social trust that allows service desks to reset authentication factors.

The credential supply chain described in this chapter — infostealers, Initial Access Brokers, affiliate buyers — is what makes most ransomware attacks possible. Disrupting that supply chain, at the point where corporate credentials leak from unmanaged devices into criminal markets, is one of the highest-leverage interventions available.

Mandiant's specific finding about contractor devices — that infostealer infections on personal machines used for work have fed some of the most consequential corporate breaches — translates directly into defensive action: contractor devices need to be treated as a security surface, not as out-of-scope assets. The credential that leaked from a gaming laptop is the same credential that opened a Fortune 500 cloud environment. The perimeter of organizational security is wherever corporate credentials exist — including on machines the organization has never managed and may not even know are in use.

---

The next development in this story is that the cartels are about to automate most of this workforce. Not replace it. Augment it — so that one operator can do the work of ten, ten can do the work of a hundred, and the attacks that once required human expertise at every stage become increasingly capable of running themselves.

Chapter 4 will show you what that looks like.

---

Here is the detail that should disturb you most: none of this workforce emerged from nowhere.

The infostealer developer who built REDLINE learned to code somewhere — a university, a bootcamp, a self-taught curriculum of the same tutorials used by legitimate engineers. The social engineer who talked their way past a corporate helpdesk learned organizational psychology the same way anyone learns it. The Initial Access Broker who categorizes network access by revenue and privilege level understands enterprise security architecture well enough to grade it. Some of them hold certifications. Some of them spent time in legitimate security roles before the criminal market made a better offer.

The criminal economy does not exist in a different talent pool than the legitimate one. It fishes in the same water. It has built compensation structures, reputation systems, and career progression models compelling enough to compete — not for every candidate, but for enough of them that the workforce keeps growing.

This is the ecosystem that is about to be handed a new tool. Not a better phishing kit. Not a faster infostealer. Something categorically different: AI systems capable of amplifying every function in this supply chain simultaneously — drafting more convincing lures, validating access faster, conducting reconnaissance at scale, and doing it all with fewer humans in the loop.

The workforce is already here. Chapter 4 is about what happens when it gets leverage.
