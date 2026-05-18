# Chapter 2: The Franchise

*Inside the RaaS Economy*

---

To open a McDonald's, you pay a fee, sign a contract, and follow a manual. The food, the logo, the fryer — it all comes from headquarters. The recipes are standardized. The packaging is specified. The quality-control framework is imposed from the top of the organization downward. You, the franchisee, provide the labor, secure the real estate, and run the location. In return, you get the brand, the supply chain, and the support infrastructure of an operation that has already solved most of the hard problems for you.

In 2026, ransomware works the same way.

This is not a metaphor that stretches the truth. It is a description of an actual business architecture — one that security researchers, incident responders, and law enforcement agencies have documented in operational detail. The ransomware-as-a-service economy is structured like a franchise system, operates like a franchise system, and produces the competitive dynamics of a franchise system. Understanding this is not just analytically interesting. It is necessary for understanding how these organizations have become as powerful as they are — and why they are not going away.

---

The architecture of a mature ransomware operation has three distinct tiers, and each tier has a different function in the criminal enterprise.

At the center — the headquarters, in the franchise analogy — are the core operators. These are the organizations that build and maintain the ransomware platform itself: the malware, the supporting infrastructure, the leak sites where victim data is published, the negotiation support systems, the payment processing workflows, the revenue accounting. Core operators run the business. They are not, as a general rule, the ones conducting the actual intrusions. That would be inefficient. Instead, they have built a platform that allows others to conduct intrusions on their behalf, using their tools, under their brand guidelines, and within their rules of engagement.

The second tier is the affiliates. These are the franchisees — criminals who want to conduct ransomware attacks but have chosen to buy into an established platform rather than build one from scratch. An affiliate brings intrusion capability: the ability to research targets, gain initial access, move through a network, steal data, and deploy the ransomware payload. What they don't need to bring is the encryption technology, the payment infrastructure, the legal threats, the leak site, or the negotiation framework. All of that is provided by headquarters.

When an affiliate successfully extorts a victim, the ransom proceeds are split. The precise percentages are not documented in authoritative sources for the Q1 2026 period — claims about specific splits should be treated as speculation, not fact. The structure, however, is confirmed: the operator takes a cut, and the affiliate keeps the rest. The exact share matters less than the principle: the affiliate pays for the service, and the service is worth paying for, because it works.

The third tier is the external supply chain: specialists who are not formal affiliates but who feed the operations of both tiers above them. This tier includes the credential brokers, the malware distributors, the social engineering crews, the SIM-swappers, the data-theft specialists. They will get their own chapter, because they deserve one. For now, it is enough to note that they exist — and that their existence is what makes the whole system function without any single operator needing to master every element of the attack chain.

---

Three brands define the competitive landscape of the 2026 ransomware market. They are worth examining individually, because each one represents a different strategy for building a dominant criminal franchise.

**Qilin** is the volume leader. In Q1 2026, Qilin posted 338 victims on its data leak site — the highest of any group, for the third consecutive quarter. More tellingly, Check Point Research found that Qilin alone posted more victims than the bottom 50 active groups combined. That is the kind of market dominance that, in legitimate industry, attracts antitrust scrutiny. In the criminal market, it simply reflects the value of operational scale.

Qilin operates what researchers describe as a semi-open affiliate model. This means the barriers to becoming a Qilin affiliate are relatively low — the platform is accessible to a broad pool of operators, not just an elite few. The implication is double-edged: openness recruits volume, but it also recruits less vetted actors. GuidePoint Security has flagged Qilin's semi-open model as a potential law enforcement infiltration risk, precisely because the lower bar for entry means a wider variety of people can get in — including undercover investigators. Qilin apparently accepts this trade-off. The volume it generates justifies the exposure.

**The Gentlemen** represent a completely different model: access-inventory-driven growth. As Chapter 1 established, this group grew from 40 victims in Q4 2025 to 166 in Q1 2026 — a 315 percent quarterly increase — reaching second place globally by year-to-date accounting. By the end of the first five months of 2026, they had published data from approximately 332 organizations.

The mechanism behind that growth is worth examining closely, because it reveals how a ransomware operation can scale in ways that have nothing to do with malware quality or technical innovation. The Gentlemen had accumulated a large inventory of pre-positioned access — including, according to secondary reporting summarizing Check Point's findings, roughly 14,700 compromised FortiGate network security devices. Think of this as a warehouse operation: they had stocked the shelves before they needed to fill orders. When the time came to attack, there was no preliminary hunting phase, no months-long reconnaissance. The targets were already compromised and waiting.

This is inventory management. This is supply chain optimization. This is how a sophisticated commercial operation thinks about resource allocation.

The group's geographic profile adds another dimension. Only 13 percent of their publicly listed victims were U.S.-based organizations, compared to an ecosystem average of nearly 50 percent. The Gentlemen were not hunting American companies because American companies are the most lucrative targets — the conventional wisdom in ransomware threat intelligence. They were attacking wherever their inventory pointed. They had compromised access to networks in Asia-Pacific, Latin America, and elsewhere; those were the networks they attacked. The access drove the targeting, not the other way around. This is the behavior of an inventory-driven business, not a target-prestige-driven one.

There is one additional detail about The Gentlemen that deserves attention, because it says something important about the organizational maturity of modern ransomware groups. At some point, an anonymous actor breached The Gentlemen's internal back-end database and exfiltrated more than 16 gigabytes of data — communications, internal records, tooling information — and offered it for sale at $10,000 in Bitcoin. The leaked material reportedly included internal discussions about rival groups, interest in code-signing capabilities, and what appears to be the work of an organization that was actively studying competitors, analyzing its own operations, and iterating on its methods.

A ransomware cartel, hacked by a competitor. Internal databases, internal discussions, internal corporate intelligence. The irony is noted. So is the implication: these organizations have become complex enough to be attacked the way complex organizations are attacked. They have assets worth stealing. They have secrets worth selling. They have enough internal structure that a breach of their systems is a meaningful event.

They are, in other words, corporations.

**LockBit 5.0** is the recovery story. LockBit was arguably the world's most prolific ransomware brand for much of the period between 2020 and 2024, running what many researchers described as the most sophisticated RaaS operation ever documented. Then, in early 2024, Operation Cronos — a coordinated law enforcement action involving agencies from a dozen countries — disrupted LockBit's infrastructure, seized its servers and website, and publicly exposed details about its operations. At the time, it was held up as a demonstration of what international cooperation could achieve against ransomware.

LockBit survived.

Not immediately and not at full strength — the group posted 79 victims in Q4 2025, a diminished presence compared to its peak. But Q1 2026 told a different story: 163 victims, a 106 percent increase quarter-over-quarter, and a return to the global top tier. LockBit had rebuilt.

The rebuilt version was not simply the old version repackaged. LockBit 5.0, which launched on criminal forums in September 2025, represented genuine technical modernization. Multi-platform support for Windows, Linux, and ESXi virtualization infrastructure — meaning a single affiliate can deploy against any major operating environment. Enhanced evasion and anti-analysis capabilities. Faster encryption. Randomized 16-character file extensions that frustrate signature-based detection. These are not cosmetic changes. They are the product of a development process, carried out by a team with resources and time.

The affiliate deposit requirement is perhaps the most revealing single feature of LockBit 5.0's governance model. To operate as a LockBit affiliate, a criminal must deposit approximately five hundred dollars in Bitcoin. This sum is not a barrier — for anyone with genuine criminal intention, five hundred dollars is trivial. It is a screening mechanism. It separates committed operators from casual tourists. It creates financial exposure that discourages abuse and defection. It is, in functional terms, equivalent to a franchise fee: proof of commitment, skin in the game, a relationship that both parties have a reason to maintain.

LockBit also made a strategic adjustment at the geographic level. Historically, more than half of all LockBit victims had been U.S.-based organizations. By Q1 2026, the U.S. share of LockBit's victims had fallen to 21.2 percent. The group had diversified: Europe, Latin America, other regions. The explanation is straightforward — U.S. victims are lucrative, but U.S. law enforcement attention is also intensive. Reducing U.S. exposure reduces jurisdictional risk. This is not a criminal instinct. This is a business strategy. LockBit is practicing geographic risk diversification, the same way a multinational corporation balances its revenue exposure across markets to avoid over-dependence on any single regulatory environment.

---

The cooperative dimensions of the ransomware economy deserve attention, because they illustrate something that is often missed in discussions of these organizations: they are not simply competitors. They are also collaborators.

Huntress, a cybersecurity firm, documented a supply chain relationship between LockBit, Qilin, and DragonForce that operates like a coordinated cartel rather than a set of rival gangs. If a victim organization refuses to pay a LockBit ransom, stolen data from that victim may be passed to DragonForce for publication. The victim's refusal to cooperate with one group does not protect them from another. The data circulates in the criminal supply chain until it finds a monetization path, just as unsold goods in a supply chain move through secondary markets until they reach a buyer.

This is cartelization. It is the behavior of an industry that has matured beyond pure competition into structured cooperation. In legitimate markets, antitrust law prohibits this kind of coordination. In the criminal market, there is no antitrust law. There is only efficiency, and coordinated victim pressure is more efficient than uncoordinated competition.

---

Then there is the frontier beyond franchising: white-label ransomware.

The DragonForce RansomBay model represents the logical endpoint of the RaaS architecture. In the standard affiliate arrangement, the affiliate still needs operational capability — the ability to conduct intrusions, deploy malware, manage communications. These are non-trivial skills. They represent a threshold, however low, that limits the pool of potential affiliates.

White-label ransomware eliminates that threshold. Under the RansomBay model, a criminal who wants to run a ransomware operation buys a fully configured package. The back-end infrastructure — malware, encryption technology, leak site, payment processing, negotiation support — is provided as a service. The buyer presents their own brand, operates their own "front-end" presence, and uses the platform's infrastructure for everything that actually requires technical sophistication. They need not write a single line of code. They need not build a single server. They are, in pure terms, front-end operators of a back-end platform.

The paradox of this development is that it appears to increase fragmentation — more brands, more apparent groups, more names appearing on leak sites — while actually deepening concentration. The proliferation of front-end brands masks the consolidation of back-end infrastructure. Visible diversification at the surface conceals monopolization at the core. This is precisely the dynamic observed in the legitimate technology industry: many consumer-facing services, many brand names, many apparent choices — all running on two or three cloud platforms, two or three payment processors, two or three operating systems.

The criminal economy is converging toward the same structure.

---

What does this mean for the quality of the threat?

It means better service. And "better service" in this context is genuinely terrifying.

In a fragmented criminal market with dozens of unreliable operators, victims who paid ransoms sometimes discovered that the promised decryption tool didn't work, or arrived late, or decrypted only some of their files. The Obscura bug — an encryptor that rendered files over one gigabyte permanently unrecoverable regardless of payment — is the archetype of this problem. When you cannot trust that paying will work, the incentive to pay is diminished.

Consolidated operators cannot afford this problem. Their entire business model depends on payment working. If word spreads in the victim community — through insurance carriers, incident response firms, legal advisors — that a particular ransomware group does not deliver functional decryptors, payment rates decline. Revenue declines. Affiliates defect to better-managed brands. The flywheel runs in reverse.

So the dominant operators of 2026 invest in operational consistency. They maintain functional decryptors. They honor their commitments — the commitment, specifically, that paying the ransom will restore access to encrypted files. They have, in the most perverse possible sense, built customer trust. They are reliable criminal counterparties. And that reliability, that paradoxical trustworthiness, is one of the most dangerous things about them.

---

Behind every ransomware brand is a workforce.

Not a small one. Not a simple one. Behind the market statistics and the brand profiles and the franchise fees, there is an entire ecosystem of human beings — and increasingly, non-human systems — doing the actual work. Recruiting targets. Stealing credentials. Social-engineering helpdesks. Moving through networks. Classifying stolen data. Negotiating payments. Maintaining customer-service chat channels.

Some of them know exactly what they are part of. Some of them think they are doing something else entirely.

---

It is worth dwelling on the governance mechanics of the affiliate relationship, because they reveal something important about what has changed in the criminal economy.

In the early ransomware era, an operator who wanted to monetize a successful intrusion had to handle every stage of the process: the attack, the encryption, the ransom note, the negotiation, the Bitcoin collection, and — if they were even slightly principled in the criminal sense — the delivery of a working decryptor. This is a lot of work for a single actor. It requires multiple skill sets: technical intrusion capability, cryptographic implementation, negotiation skill, and financial operations. Very few criminals are equally capable across all of these domains.

RaaS solved this by decomposing the problem. The core operator handles the technical infrastructure and the financial plumbing. The affiliate handles the intrusion execution. The result is that a criminal who is excellent at gaining network access but has no interest in developing malware can channel their capability into the platform that provides the malware. A criminal who has built infrastructure but lacks the operational reach to conduct intrusions at scale can recruit affiliates who provide that reach. Specialization drives efficiency, and efficiency drives the scale that produces the victim counts documented in Check Point's research.

The revenue split that flows through this relationship is the financial engine of the system. The specific percentage splits in operation during Q1 2026 are not documented in authoritative sources — claims about precise numbers should be treated as speculation. What is confirmed by reporting from multiple sources is the structural logic: the affiliate executes the attack and collects the ransom; a portion of the ransom flows back to the core operator as a platform fee; the affiliate retains the remainder. The size of the platform fee is presumably a competitive variable — operators who provide better infrastructure, more reliable decryptors, stronger brand credibility, and better negotiation support can command higher fees. Operators who provide lower-quality services must accept lower fees or lose affiliates to better-managed platforms.

This fee competition between platforms is what drives the quality improvements that make consolidated ransomware operators more dangerous than fragmented ones. They are competing for affiliates. Affiliates have choices. Affiliates migrate toward the best platform, just as legitimate developers migrate toward the most reliable cloud infrastructure. Platform operators who don't invest in quality lose affiliate market share. The market mechanism is identical to the legitimate technology economy; only the application differs.

---

The cooperative dimensions of the ransomware economy deserve careful examination, because they are frequently missed in coverage that focuses on competition between groups.

Ransomware operators in 2026 are not purely in competition with each other. They are also collaborators — sharing infrastructure, passing victim data between platforms, coordinating on geographic and sector targeting to avoid diluting each other's extortion leverage. The Huntress-documented relationship between LockBit, Qilin, and DragonForce — where a victim's stolen data can be passed between platforms if the victim refuses to pay the first group's demands — is one documented example of this cooperation.

Think of what this means for the victim. An organization that refuses to pay a LockBit ransom on principle — believing that payment funds criminal organizations, or following insurance or regulatory guidance that discourages payment — may find that its data appears on DragonForce's leak site anyway. The refusal to cooperate with one criminal organization does not protect from another if the data has been shared between them. The victim has not avoided harm by refusing to pay. They have only redirected it.

This cooperative dynamic is the behavior of an industry that has matured beyond pure competition into structured market-making. In legitimate markets, competition law prohibits the kinds of data-sharing and cooperative pricing arrangements that maximize collective revenue at the expense of the market's "customers." The criminal market has no such constraints. Cooperation is simply good business.

---

The "customer service" implication of all of this consolidation and cooperation is perhaps the most counterintuitive and important insight in the modern ransomware landscape.

Consolidated operators invest in the victim experience of the payment process. Not because they care about victims — manifestly they do not — but because their payment conversion rate depends on it. A victim organization that believes paying the ransom will definitely restore their files is more likely to pay. A victim organization that has heard from an incident response firm or an insurance carrier that a particular group routinely fails to deliver working decryptors is less likely to pay.

The Obscura bug — the encryptor that rendered files over one gigabyte permanently unrecoverable — is the archetype of the quality problem in smaller, less-organized operators. When victims discover (through their own experience or through published incident reports) that a ransomware group's decryptor is defective, payment rates decline. The criminal organization's revenue per intrusion falls. Affiliates take their business to better-managed platforms that have invested in functional, reliable decryption infrastructure.

Qilin's 338 victims in a single quarter. The Gentlemen's 315 percent growth. LockBit's return to the top tier after a devastating law enforcement disruption. These are not stories about technical superiority alone. They are stories about operational reliability, affiliate management, and the perverse competitive advantage that comes from delivering a "service" that actually works.

The criminal organizations of 2026 are not winning because they are more clever. They are winning because they are more consistent.

---

There is a hypothetical scenario worth considering, because it makes the franchise dynamic visceral and immediate.

Imagine a would-be criminal — not a sophisticated hacker, but someone with internet access, some money in cryptocurrency, and a willingness to engage with criminal marketplaces. Until recently, building a ransomware operation would have required genuine technical capability: the ability to write or acquire malware, to build and maintain supporting infrastructure, to handle ransom negotiations, and to manage cryptocurrency transactions. The technical barrier was real, even if it had been declining.

Under the white-label RansomBay model, that barrier largely disappears. The aspiring operator browses criminal forums the way a prospective small business owner browses franchise opportunity listings. They compare platforms: which one provides the most reliable malware, the most user-friendly victim management dashboard, the most supportive negotiation infrastructure, the most aggressive affiliate terms. They make a selection. They pay the platform fee, which may take the form of a percentage of future ransom proceeds rather than an upfront cost. They receive access to the backend infrastructure, the branding, the playbooks.

And then they go looking for victims.

They do not need to write a single line of code. They do not need to build a server or maintain a leak site. They need to find a way into a target organization — and they can buy that too, from an Initial Access Broker who has already done the work of finding and validating corporate network access. One criminal buys the entry; another provides the malware; the platform handles the pressure campaign; the victim pays the ransom; the proceeds flow upward through the stack.

This is the ransomware economy of 2026 operating at full maturity. It has distributed every element of the attack chain to the specialist best positioned to handle it, connected those specialists through market mechanisms that price each contribution, and delivered the whole system on a platform that requires its operators to possess almost nothing except the willingness to participate.

The barrier to becoming a ransomware operator, in 2026, is primarily a moral one. The technical barriers have been methodically lowered.

---

Behind every ransomware brand, behind every franchise fee and platform agreement and affiliate deposit, there is a workforce that makes the operations real. Chapter 3 will introduce you to the human beings — and the supply chains — that execute what these brands have designed. Including some who have no idea they're involved at all.
