# Chapter 1: The Corporation

*How Crime Became a Platform*

---

## Part One: The Corporation

---

Picture ransomware in 2016.

A hacker — likely working alone, or in a loose partnership with a handful of others — writes some malicious code, blasts it out to tens of thousands of email addresses, and waits. A fraction of victims click the attachment. A fraction of those get successfully infected. The malware locks their files, demands a few hundred dollars in Bitcoin, and the hacker collects whatever they can. Some of the victims pay. Some don't. Some discover that even after paying, the decryptor doesn't work — the hacker's code is buggy, the key is never delivered, or the whole operation has already collapsed by the time they try to recover.

It is chaotic. Opportunistic. Frequently incompetent. The digital equivalent of smash-and-grab crime: high volume, low precision, unreliable returns. The criminal who ran this operation might clear a few thousand dollars in a good month. More likely, he ran it sporadically, between other activities, with no expectation of building anything durable.

Now picture ransomware in 2026.

The comparison should feel like the difference between a street corner drug dealer and Goldman Sachs.

---

In the first quarter of 2026, ransomware operators publicly posted 2,122 organizations to their data leak sites — the equivalent of nailing 2,122 company names to a digital public pillory for the entire internet to see. According to Check Point Research, which tracked the data across all major ransomware groups, that figure represented the second-highest Q1 total ever recorded. Not a spike. Not an outlier. The second-highest on record — evidence that 2026 was not a break from the recent trend but its continuation.

On average, more than 700 organizations were posted every month. That is roughly one attack — logged, completed, and turned into extortion leverage — every hour of every day, without interruption, throughout the entire quarter.

And the market was getting more concentrated, not less.

This is the number that changes everything: the top ten ransomware groups captured 71 percent of all victims in Q1 2026. In Q3 2025, just six months earlier, that same top ten had accounted for 57 percent. The number of active groups actually fell — from a peak of 85 in Q3 2025 to 71 in Q1 2026, even as 21 new groups tried to enter the market. Most of those 21 new entrants posted fewer than ten victims each. They were noise at the edges of a market rapidly organizing itself around dominant players.

The economics of this phenomenon have a name, and it should be familiar to anyone who has followed the history of technology platforms. This is called industry consolidation. It is what happened to the taxi industry when Uber arrived, to the bookstore business when Amazon expanded, to the hotel market when Airbnb scaled. A fragmented ecosystem of many small, often unreliable actors gives way to a smaller number of more capable, more consistent, more economically efficient platforms. The small players don't disappear immediately — but they stop mattering. Market share concentrates at the top. Quality improves. Volume stays high. The platform operators collect their margins.

The ransomware market in 2026 is following exactly this trajectory. Not as an accident. Not as a coincidence. As a consequence of the same economic forces that organize every other industry, applied to organized crime.

---

For most people, the instinct when hearing that there are fewer ransomware groups is to reach for comfort. Fewer groups means less threat, right? If the market is shrinking, things are getting better?

They are not getting better. The market is not shrinking. It is maturing.

Consider what consolidation actually produces. When there were 85 groups competing for victims, the criminal market was characterized by exactly the problems you'd expect in any fragmented, low-trust market: unreliable delivery, shoddy products, poor customer relationships, chaotic pricing, and frequent fraud. Check Point Research documented an instructive example — a ransomware group called Obscura that shipped an encryptor with a bug that rendered any file over one gigabyte permanently unrecoverable, regardless of whether the victim paid the ransom. The decryption key, if it arrived at all, couldn't restore the data. The money was gone; the files were gone; the victim had paid for nothing.

This is the kind of operational dysfunction that characterizes fragmented criminal markets. Groups are too small, too unstable, or too technically immature to deliver reliable results. That unreliability actually reduces their leverage: victims who believe the criminals can't actually restore their systems have less incentive to pay. And word travels — through incident response firms, through insurance carriers, through industry information-sharing groups. When it becomes known that a particular ransomware group doesn't deliver on its promises, victims resist. The criminal organization's payment conversion rate drops. Revenue declines. The operation becomes less viable.

Consolidation solves this problem. Larger, more established operators have strong incentives to deliver functional decryptors, to maintain consistent communication, to honor the perverse "bargain" at the center of the ransomware business model. Their entire business depends on victims believing that payment works. And because the most successful operators of 2026 have refined their processes over years of operation, payment increasingly does work — which means victims pay, which means the criminals collect revenue, which means they can invest in better infrastructure, better affiliates, better attacks. It is a flywheel. Once it spins, it is very hard to stop.

The analogy in legitimate business is clear: when an industry consolidates around well-capitalized, reliable platforms, the quality of the "product" goes up, consumer trust increases, and market volume typically rises. This is exactly what is happening in the ransomware economy. The platform operators of 2026 are not just more dangerous because they are larger. They are more dangerous because they are better.

---

Ransomware-as-a-Service — RaaS, in the shorthand of security researchers — is the business model that made this possible. The concept is best understood through a familiar analogy.

To open a McDonald's franchise, you pay a fee, sign an agreement, and follow a detailed operational manual. The food recipes come from headquarters. The logo, the branding, the cooking equipment specifications — all provided. The real estate is yours to secure; the operations are yours to manage. But the core product, the supply chain, the quality standards, the customer-facing identity — all of that belongs to the franchisor. You are a local operator of a global brand.

RaaS works on the same logic. A criminal organization — the core operator — develops and maintains the malware, the supporting infrastructure, the leak sites where victim data is published, the negotiation support, the revenue processing systems. They build the product and run the platform. Then they recruit affiliates: criminals who want to conduct ransomware attacks but lack the capability or resources to build everything from scratch. The affiliate pays into the platform — in reputation, in Bitcoin deposits, in adherence to the operator's rules — and in return gains access to everything the platform provides. When the affiliate executes a successful attack, the ransom proceeds are split: some percentage to the operator, the rest to the affiliate.

The affiliate is the franchisee. The operator is the franchisor. The victim is the customer who has no choice about whether to walk through the door.

This model is, in strategic terms, a masterpiece of efficiency. It separates the people who are good at building criminal technology from the people who are good at executing criminal operations. It allows the platform to scale without the core operators needing to personally conduct every attack. It distributes legal and operational risk. And it turns ransomware from a one-person or small-team operation into a scalable criminal economy with multiple layers of specialization and capital investment.

The data leak site — the platform where victim names and stolen data are published — is one of RaaS's most powerful innovations. It converts data theft into ongoing leverage. It is where the "franchisee" reports the results of a successful attack. It is where the coercion campaign, described fully in Chapter 7, is waged in public. For now, it is enough to understand it as the criminal equivalent of a product listing page: where victims are inventoried, their exposure is advertised, and the pressure to pay accumulates.

---

The oligopoly that has emerged from this system consists of a handful of dominant brands, each pursuing a distinct strategy, each illustrating a different way to win in the same market.

Qilin was the dominant force of Q1 2026 by almost any measure. The group posted 338 victims — the most active single group for the third consecutive quarter. Check Point Research noted that Qilin alone posted more victims than the bottom 50 active groups combined. That kind of market dominance is the stuff of legitimate antitrust investigations. In the ransomware economy, it simply reflects operational maturity: a semi-open affiliate program that successfully recruits and manages a broad pool of operators, consistent technical infrastructure, and an extortion process sophisticated enough to convert victims into payers at scale.

The Gentlemen arrived with a different kind of force. In Q4 2025, the group had posted 40 victims — a mid-tier presence, unremarkable. In Q1 2026, they posted 166, a 315 percent quarterly increase that made them second-ranked globally by Check Point's year-to-date accounting, with 332 total organizations listed in just the first five months of 2026. The source of that growth was not superior malware. It was inventory — a pre-positioned stockpile of compromised access to roughly 14,700 FortiGate network security devices that allowed the group to attack at volume without the usual reconnaissance phase. When it came time to execute, they didn't need to find victims. The victims were already waiting, already compromised, catalogued and queued.

Their geography told the same story. Only 13 percent of The Gentlemen's victims were in the United States, compared to a ransomware ecosystem average of nearly 50 percent. They did not hunt U.S. companies because U.S. companies are the most prestigious targets. They attacked where the access was. That is an inventory-management decision. That is a supply-chain decision. That is how a sophisticated commercial operation thinks about resource allocation — optimizing against available inputs rather than against idealized targets.

LockBit 5.0 represents the third archetype: the comeback story. LockBit was arguably the world's dominant ransomware brand until a major international law enforcement operation in early 2024 — Operation Cronos — disrupted its infrastructure, seized servers, and momentarily seemed to deal the group a fatal blow. The group posted 79 victims in Q4 2025. Not gone, but diminished. Then Q1 2026: 163 victims, a 106 percent increase, re-entry into the global top tier. LockBit had rebuilt.

The recovery was not accidental. LockBit rebuilt not just its malware but its entire operational architecture. LockBit 5.0, which launched on criminal forums in September 2025, featured multi-platform support — able to attack systems running Windows, Linux, and ESXi virtualization infrastructure simultaneously. Enhanced evasion capabilities. Faster encryption. Randomized 16-character file extensions that foil simple signature detection. And — notably — a required affiliate deposit of approximately five hundred dollars in Bitcoin. That deposit is not a technical barrier. It is a governance mechanism. It screens out casual affiliates who aren't committed enough to put something at risk. It reduces opportunistic abuse. It is, in the language of corporate governance, a quality-control filter on the affiliate pipeline.

LockBit also made a geopolitical adjustment. Historically, more than half its victims had been in the United States — a high-value targeting strategy that also concentrated law enforcement exposure. By Q1 2026, its U.S. share had fallen to 21.2 percent. The group had diversified across Europe, Latin America, and other regions. This is jurisdictional risk management. This is how a multinational corporation thinks about political exposure. Diversifying revenue away from a jurisdiction that has demonstrated willingness and capacity to disrupt your operations is basic corporate strategy, applied to criminal enterprise.

Together, Qilin, The Gentlemen, LockBit, and Akira accounted for 41 percent of all ransomware victims in Q1 2026. Four organizations — controlling nearly half the market. The rest of the 71 active groups competed for the remaining 59 percent, with most of the 21 new entrants posting fewer than ten victims in the quarter.

---

There is one more development that deserves attention, because it represents the logical endpoint of everything described above.

In the normal RaaS model, an affiliate still needs some technical capability: the ability to execute an intrusion, deploy malware, manage victim communications. The model requires some minimum level of operational competence. What happens when even that barrier disappears?

It disappears through white-label ransomware.

The model, exemplified by DragonForce's RansomBay offering, takes the franchise metaphor to its limit. A criminal who wants to run a ransomware operation no longer needs to develop malware. They no longer need to build a leak site, a payment system, a negotiation infrastructure, or even a brand. They buy a fully configured package — backend infrastructure, malware, the works — and operate under it. The technical capability is entirely outsourced. The criminal simply runs the local "franchise location," handling the victim-facing interactions while the backend platform handles everything that requires engineering.

This has a counterintuitive implication. The visible landscape of ransomware brands may be about to expand — more names, more apparent groups, more apparent fragmentation. But that visible proliferation masks a different kind of concentration happening at the infrastructure level. Fewer real operators are building fewer backend systems that power an ever-increasing number of front-end brands. The market is diversifying at the surface while consolidating beneath it.

This is how platform monopolies work in legitimate technology too: many apps built on top of a handful of cloud providers; many storefronts built on top of two or three e-commerce platforms; many brands manufactured by a shrinking number of factory operators. In each case, what looks like a diverse, competitive market on the consumer-facing surface is actually a highly concentrated infrastructure market one layer below.

Huntress, the cybersecurity company, documented another dimension of this cooperative evolution: partnerships between ransomware groups that operate as a coordinated cartel rather than competing gangs. If a victim refuses to pay a LockBit ransom, stolen data from that victim may be passed to DragonForce for publication. The victim's refusal to cooperate with one group doesn't protect them from another. The data circulates in the criminal supply chain until it finds a monetization path, just as unsold inventory in a supply chain moves through secondary markets. This is not competition. This is cartelization.

---

Check Point Research also documented something that illustrates just how corporate these criminal organizations have become. The Gentlemen, that breakout group with 315 percent quarterly growth, suffered a significant data breach of its own. An anonymous group penetrated The Gentlemen's internal back-end database and exfiltrated more than 16 gigabytes of communications, tooling records, and internal data. The stolen material was offered for sale at $10,000 in Bitcoin. Internal discussions about rival groups. Interest in code-signing capabilities. Lessons drawn from competitors' operational histories.

A criminal empire that gets hacked. A criminal empire that keeps internal databases. A criminal empire that studies its competitors, benchmarks their methods, and iterates on its own operations.

These are not the behaviors of a gang. They are the behaviors of a corporation — a learning organization with market intelligence operations, an R&D function, and a competitor analysis practice.

This is not a gang. This is a corporation.

---

The question isn't what these organizations look like today. It's what they look like tomorrow — once they've finished hiring.

Because behind every one of these market statistics, behind every percentage point of victim share, behind every quarterly growth figure and geographic diversification decision, there is a workforce. There are people — and increasingly, non-human systems — doing the actual work of ransomware: stealing credentials, researching targets, writing code, social-engineering helpdesks, negotiating ransom payments, maintaining customer communication channels.

The labor market that supplies this workforce is one of the most consequential and least understood developments in modern organized crime. Chapter 2 will show you how the franchise brands work in operational detail — who gets what, how the money flows, and what the dominant criminal brands actually offer their affiliates. Chapter 3 will introduce you to the people who make it all run.

Because the corporation has employees. And some of them may be closer to you than you think.

---

The question of what this consolidation means for defenders is not abstract. It translates directly into the nature of the threat organizations face when they are targeted.

When ransomware was fragmented — dozens of small groups, inconsistent tools, unreliable decryptors — the threat landscape was genuinely varied. Different groups had different technical capabilities, different target selection logic, different extortion approaches. Some were sophisticated; many were not. An organization that survived one group's attack might be better prepared against a similar group's attack later.

Consolidated ransomware has different characteristics. The dominant operators of 2026 have had years to refine their operations — to identify what works, to discard what doesn't, to invest the proceeds of successful attacks into better tools, better infrastructure, and better personnel. They have survived law enforcement actions that destroyed smaller competitors. They have attracted the best available affiliate talent, because talented affiliates migrate toward the best-paying, most reliable platforms.

This means that when an organization encounters a consolidated operator — Qilin, LockBit, The Gentlemen — it is encountering the result of years of competitive selection and operational refinement. The affiliate who conducted the attack has done this before, probably many times. The malware is well-tested. The extortion process has been calibrated to maximize payment rates. The decryptor, if one is offered, is likely to work.

The competition that the criminal market prizes has produced the equivalent of an industry leaders board where the leaders keep getting better. Amateur attackers are deterred by marginal improvements in security — they will move on to easier targets. Professional operators with access to specific victim organizations through Initial Access Broker markets will invest effort proportional to the expected return. Security investment changes the economics of targeting. It makes the attacker's calculation less favorable. And in a market where the attacker has many potential targets to choose from, raising your cost above the average shifts the attack to a different target.

The improvement in "attacker customer service" that consolidation enables — the functional decryptors, the reliable payment processing, the consistent negotiation — changes the victim's calculus around paying ransoms in ways that make the criminal extortion economy function more smoothly, which makes it more financially successful, which makes it more worth investing in, which makes it better still. The flywheel keeps spinning.

Behind every ransomware brand, behind every franchise fee and affiliate deposit and victim management dashboard, there is a workforce that makes the operations real. Chapter 3 will introduce you to the human beings — and the supply chains — that execute what these brands have designed. Including some who have no idea they're involved at all.

---

Consider what "fewer groups, more dangerous" actually means when you are the one holding the ransom note.

Think back to that factory floor from the Prologue. The lines going quiet. The workers standing at terminals that won't respond. The production supervisor who called the helpdesk, then watched the calls multiply — five, a dozen, more — as it became clear that something systemic had happened, something far beyond an IT outage, something that had a name and a demand attached to it. Now imagine that the group responsible for that attack had shipped a broken decryptor.

That is not a hypothetical. It is, in miniature, what Obscura did.

Check Point Research documented the Obscura group's encryptor bug in its Q1 2026 analysis: a flaw that rendered any file exceeding one gigabyte permanently unrecoverable, regardless of payment. The decryption key, when it arrived, couldn't actually decrypt. The data was gone. The ransom was gone. And the factory — or the hospital, or the law firm, or the manufacturer — was left with the worst possible outcome: no money and no files. What was already a crisis became an irreversible catastrophe.

This is what criminal market fragmentation looks like from the inside of a victim organization. It is not an abstraction about market efficiency or competitive dynamics. It is a company that paid because it had no other choice, because its operations were hemorrhaging by the hour, because its legal team and its insurance carrier and its incident response firm all ran the numbers and concluded that paying was the fastest path back to function — and then discovered that the criminals on the other end of the negotiation were not competent enough to honor the transaction.

The perverse effect is this: in a fragmented market, the victim has less reason to pay, because payment is less likely to work. And less reason to pay means lower conversion rates for the criminal enterprise, which means less revenue, which means less investment in better operations, which means the cycle continues. Fragmentation creates mutual distrust that corrodes the extortion economy from within.

Consolidation dissolves that distrust — from the criminal's side. The dominant operators of 2026 have every economic incentive to deliver functional decryptors, to maintain professional communication, to make payment work. Their whole business model depends on the next victim believing that payment will restore their systems. The factory in the Prologue faces an adversary who has run this process thousands of times. The ransom note on the screen was not written by someone who will disappear when the wire transfer clears. It was written by an organization with a help desk, a negotiation team, and a reputational interest in a successful outcome — on their terms.

That is what fewer groups, more dangerous actually means. It means that when the lines go quiet, the people on the other end of the note know exactly what they are doing. They have done it before. They will do it again. And the market has selected them, above all their competitors, precisely because they are reliable enough to be believed.
