# Prologue: 72 Minutes

*The Anatomy of a Perfect Attack*

---

The first sign was a cursor that wouldn't move.

The IT supervisor noticed it at 6:47 on a Tuesday morning — a workstation at the far end of the production floor, its screen awake but unresponsive. She walked over, tapped the mouse. Nothing. Pressed the spacebar. Nothing. She glanced at the others nearby. All up. All fine. She rebooted the one bad machine and went back to her desk.

She did not know it yet, but the company had already lost.

The attackers had been inside the network for more than an hour by then. Not physically inside — the factory operated across three continents, its headquarters in a mid-sized European city, its operations stretching from assembly plants to distribution centers to pharmaceutical supply chains that ended in hospitals. The attackers were nowhere and everywhere at once: invisible threads moving through the company's digital nervous system with the patience of a surgeon and the speed of an automated process.

They had gotten in through a search engine.

---

Sometime in the weeks before that Tuesday, an employee — it could have been anyone: a procurement officer researching a software vendor, an operations manager looking for a technical manual, a contractor looking up a troubleshooting guide — had typed a search query into a browser on a company-connected machine. The results looked legitimate. The top hit had the right name, the right logo, the right language. It was not the right site.

Security researchers call this SEO poisoning. A more honest name would be ambush. Criminal operators study which search terms bring corporate employees to specific kinds of pages. They build counterfeit sites that rank near the top of results — dressed identically to the real thing — and seed them with what appears to be a useful download: a driver, a manual, an administrative utility. The employee clicks. The file downloads. The file executes. And somewhere in the program code, hidden inside a legitimate-looking administrative tool — the kind used by IT departments to manage software across thousands of computers at once — a small, quiet passenger begins its work.

No alarm sounded. No warning appeared. The security desk at the lobby of this company's digital building never saw anyone walk through.

---

By the time the IT supervisor noticed the frozen cursor, the attackers had completed the hard part.

They had used that initial foothold — one machine, one compromised process — to move laterally through the network. Think of a corporate network as a building with floors, stairwells, maintenance corridors, and back offices that most employees never visit. The attackers had found the maintenance corridors. They had discovered which systems connected to which. They had mapped the backup infrastructure — the systems that stored copies of every critical file, the digital equivalent of a fireproof vault — and they had targeted it specifically. The vault would be the first thing they neutralized.

This was not a smash-and-grab operation. It was methodical. Targeted. What intelligence analysts would call purpose-built.

By the time the manufacturing line noticed something was wrong, the attackers were no longer exploring. They were executing.

---

At 6:51 a.m., a production supervisor in one of the company's assembly facilities noticed her order processing terminal had gone offline. She called the IT helpdesk. The helpdesk was fielding three other calls. Then five. Then a dozen. Something was wrong with the inventory system. Something was wrong with shipping coordination. Something was wrong with the distribution network that linked the factories to the warehouses to the hospitals at the end of the supply chain.

The factory floor, which had been running at full capacity since the previous night shift, began to go quiet.

One line stopped. Then another. Workers stood at their stations looking at dark screens, at machines that wouldn't respond to input, at terminals that displayed nothing at all. Supervisors with phones pressed to their ears conveyed partial information to management who could not yet tell what was partial and what was complete. The word "cyberattack" was not yet being used. The words being used were: "outage," "system issue," "IT problem."

Manufacturing halted. Distribution stopped. Shipping froze. Order processing went dark.

A global medical technology firm — a company whose products ended up in operating rooms and intensive care units — had been brought to silence in less than two hours.

---

The attackers were already gone.

This is the detail that people rarely understand about modern ransomware: the encryption event — the moment when files are locked and the digital locks are changed — is not the beginning of the story. It is the end of one chapter and the beginning of another. By the time a target organization discovers that something is wrong, the criminals have already stolen everything they came for. The data — patient records, supplier contracts, intellectual property, financial projections — has already traveled across the internet to servers the victims will never find. The backup systems that might have enabled a clean recovery have already been located and neutralized. What appears to the victim as the beginning of an attack is, in fact, the moment the attacker has decided they no longer need to hide.

Unit 42's 2026 Global Incident Response Report, drawn from more than 750 major incidents across fifty countries, documented what had been happening to attack timelines. Modern ransomware attacks are roughly four times faster than they were just two years prior. In the fastest cases, attackers reached full data exfiltration — extracting every file worth stealing — in as little as seventy-two minutes. Some cases took longer. This one took more than an hour, possibly several. The specifics are less important than the principle: by the time the helpdesk phone rang for the twelfth time, the theft was already complete.

Over ninety percent of the breaches Unit 42 investigated in 2026 were enabled not by elaborate zero-day exploits — not by master keys forged before their locks ever existed — but by preventable gaps. A search result that looked legitimate. A download that seemed useful. A machine that someone forgot was connected to the corporate network.

---

At some point that morning — the exact moment varies in the accounts of those who were there — a ransom note appeared on screens across the company's environment. The note was professionally formatted. It was written in fluent English. It explained, calmly, that the company's files had been encrypted and its data had been exfiltrated. It provided a link to a secure communication channel. It named a price. It set a deadline. And it promised — with the particular confidence of an organization that had done this before — that if terms were met, the decryption key would be delivered and the data would not be published.

It read, in other words, like a contract. A very bad contract, under very bad terms, with a counterparty who held all the leverage. But a contract nonetheless.

The supply chain of a global medical technology firm unraveled downstream. Hospitals waiting on shipments received no status updates. The company's financial systems were inaccessible. Executives who had prepared for many kinds of business emergencies — regulatory failures, product recalls, market disruptions — discovered they had no protocol for this. There is no business continuity plan for the moment when the entire company's nervous system goes dark simultaneously.

---

This was not an unusual event.

That is the point that must be held in the mind before any of what follows can be properly understood. The attack on this company was not the work of a nation-state. It was not a uniquely sophisticated operation mounted by elite operatives with years of preparation. It was, in the parlance of those who track these events for a living, a Tuesday-morning transaction. One incident among more than two thousand that would be publicly documented in the first three months of 2026. One entry in a ledger maintained by criminal organizations that, combined, ran more than seven hundred attacks every month — roughly one every hour, all day, every day, without pause, without remorse, without visible limit.

The factory went quiet because someone clicked a search result.

The supply chain unraveled because a tool designed to help IT teams manage computers was turned against the company by people who understood its architecture better than most of its own engineers.

And the ransom note glowed on the screen because somewhere — in a city the victims will never know, behind a name they will never learn, inside an organization with a workforce they could not have imagined — a business had decided this company was worth targeting. Had assigned it to an operator. Had watched the operation proceed. Had received confirmation that the data was secured and the encryption deployed.

And had moved on to the next target.

---

By the end of the week, the factory would still be struggling to restore normal operations. The IT team would be working around the clock. Lawyers would be consulting with insurance carriers. Executives would be making decisions they had never been trained to make, under time pressure they could not fully understand, about an adversary they had never faced.

The ransom note was still glowing.

Who built this machine? And how did they get so good?

---

*That question has an answer. It begins with an industry.*
