# Chapter 0: Prologue — 72 Minutes

## Subtitle
The Anatomy of a Perfect Attack

## Core Question
What does a modern ransomware attack feel like from the inside — in real time, before anyone knows what is happening?

## Purpose in the Book
The prologue is the book's opening blow. It does not explain; it shows. Before the reader understands what ransomware has become, they must feel it. This chapter drops the reader inside a real intrusion — drawn directly from Unit 42's documented case of a global medical technology manufacturer — and lets them experience the speed, precision, and inevitability of a modern attack. By the time the prologue ends, the reader is shaken and hungry for answers. The rest of the book provides them.

---

## Required Content

### Must Cover
- The intrusion sequence: SEO poisoning as the entry vector, administrative tool as the malware dropper, escalation to backup and production systems.
- The speed: attacks are now 4x faster than they were just two years ago. The fastest intrusions in 2026 reached exfiltration in as little as 1.2 hours.
- The scale of disruption: manufacturing halted, distribution stopped, shipping frozen, order processing gone. A factory brought to silence.
- The moment of discovery — and the gap between "something is wrong" and "we know what is happening."

### Should Include
- The human cost: workers arriving to dark screens; management receiving calls they cannot answer; a supply chain unraveling downstream.
- A brief flash-forward to the ransom note / leak site appearance to make clear this is only the beginning of the pressure campaign.
- A statement — without explanation yet — that this attack was not unusual. It was Tuesday.

### Optional (if it fits naturally)
- A single line establishing that the attackers were done before the company's incident response team was even notified.

---

## Source Material Focus

Primary sources for this chapter:
- **Report 5 (Unit 42 2026 Global IR Report):** Case study of a global medical technology firm — intrusion via SEO poisoning and malicious administrative tool, leading to prolonged disruption of manufacturing, distribution, shipping, and order processing. Speed statistics (4x faster attacks, 1.2-hour exfiltration).

Key data points to incorporate:
- Attacks are now 4x faster than comparable periods in recent years.
- The fastest intrusions reached data exfiltration in as little as 1.2 hours.
- Over 90% of breaches were enabled by preventable exposure gaps, not elite tradecraft.
- The specific case: a global medical technology firm, SEO poisoning, malicious admin tool, manufacturing/distribution/shipping/order processing disruption.

---

## Structural Requirements

### Opening
Open in medias res — inside the attack. A hypothetical IT manager or operations supervisor notices something odd. A system that should respond doesn't. A login fails. The wrong number appears on a dashboard. Everything is about to change and no one knows it yet.

### Body Flow
1. The entry: SEO poisoning delivers the first foothold. The attacker is in, invisible, patient. (Establish the concept of access-as-commodity before explaining it; let the reader feel the wrongness.)
2. The spread: automated tools push through the network. Backup systems go dark. Production systems freeze. The clock is running — 1.2 hours to total exfiltration in some cases. This case takes longer, but the principle is the same: by the time alarms sound, it is too late to stop the theft.
3. The silence: manufacturing stops. The factory floor goes quiet. Workers look at each other. Management scrambles. The attacker is already gone.
4. Transition: "This was not a sophisticated attack by a nation-state. This was a Tuesday-morning transaction for a criminal business that ran 700 attacks last month."

### Closing
End with a single, spare question. Something like: "Who built this machine? And how did they get so good?" — then cut to Chapter 1. No answer. Only the question.

---

## Continuity Notes

### References to Other Chapters
- Do not explain the attacker's organization yet — that is Chapter 1 and 2.
- Do not explain the technology yet — that is Chapters 4 and 5.
- Do not explain who was targeted or why — that is Chapter 6.
- Foreshadow: The ransom note that appears at the end of the prologue sets up the "customer service" apparatus in Chapter 7.

### Terms & Concepts to Use
- Use plain language here — no acronyms. "A tool used to manage software across thousands of computers at once" rather than "RMM." The glossary world comes later.
- The metaphor the reader should carry away: a precision burglary so fast the locks hadn't even tripped before the thief was gone.

---

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Target length: 1,500–2,500 words (shorter than full chapters; this is a punch, not a lecture).
- Present tense or past tense — pick one and hold it. Past tense recommended for this chapter (it happened; it's done; now let's understand it).
- No chapter number visible in the heading — just "Prologue."
