# Chapter 4: The Access Economy

## Core Question

How does a stolen password become a ransomware attack — and what is the criminal supply chain that turns raw credentials into targeted intrusions?

## Purpose in the Book

This chapter is the supply-chain story. Before a ransomware affiliate can attack anyone, they need inside access. This chapter reveals the vast underground economy that provides it: infostealer malware harvesting credentials silently on millions of machines, Initial Access Brokers (IABs) packaging and selling that access to ransomware crews, and a market that treats human passwords like commodity inventory. By the end, the reader understands that the ransomware attack started long before anyone typed a ransom note — it started the day someone's password was stolen.

## Required Content

### Must Cover

- The infostealer pipeline: how malware harvests browser passwords, session cookies, VPN credentials, and SSO tokens silently from infected endpoints
- The IAB market: who IABs are, what they sell, how they price it (low-privilege credentials from $20; domain-admin access up to $10,000+), how they package and validate access
- The full supply chain from stolen credential to ransomware deployment — the "repeatable pipeline" model
- The timeline compression: the gap between credential theft and ransomware deployment is often days to weeks, not months

### Should Include

- Scale of the credential market: 16% of infostealer-infected endpoints expose enterprise SSO credentials; 79% of logs contain Microsoft Entra ID credentials; 1.17 million logs contain credentials plus session cookies enabling MFA bypass
- The "logging in instead of breaking in" shift: attackers increasingly use valid credentials rather than exploits, because credentials bypass most security controls
- How IABs sort and price access inventory: by geography, industry, revenue band, privilege level, and likelihood of payment
- Why this market makes ransomware accessible to non-technical actors: you don't need to hack in if you can buy your way in

### Optional (if it fits naturally)

- The access-as-lead-generation analogy: IAB listings as the criminal equivalent of a qualified sales pipeline — victims pre-scored by revenue, industry, and security posture

## Source Material Focus

Primary sources for this chapter:
- **Report 2:** Full IAB/infostealer supply chain, access validation market, credential pricing, supply chain mechanics, timeline compression data
- **Report 5:** Edge-device exploitation as a parallel access source; how large-scale vulnerability exploitation generates bulk access inventory for IABs

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779007686_c4a3e64a89.md`
- `books/ransomware-inc/reports/task_1779014305_434487fb06.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points to incorporate:
- 16% of infostealer-infected endpoints expose enterprise SSO credentials
- 79% of logs contain Microsoft Entra ID credentials
- 1.17 million logs include credentials plus session cookies (MFA bypass potential)
- Low-privilege credentials: as low as $20; domain-admin access: can exceed $10,000
- Gap between theft and ransomware deployment: often days to weeks
- Cisco Talos Q1 2026: phishing was top initial access vector in more than one-third of engagements
- Clop's Oracle E-Business Suite exploitation; Akira's SonicWall targeting — edge devices as bulk access generators

## Structural Requirements

### Opening

Hypothetical vignette: trace the journey of a single password. An employee at a manufacturing firm downloads what looks like a cracked software tool. An infostealer runs silently in the background, harvesting credentials. Thirty-six hours later, those credentials appear on an underground market. Three days after that, they're in the hands of a ransomware affiliate who has just been assigned the company as a target.

### Body Flow

1. The infostealer pipeline: how credentials are harvested at scale, what gets stolen, and how it flows to market
2. The IAB market: how brokers validate, price, and sell access — the quality-control layer of the criminal supply chain
3. The access-to-attack timeline: what happens between access purchase and ransomware deployment, and why it's happening faster than ever

### Closing

End on the revelation: the credential theft happened before anyone at the company knew anything was wrong. The attack began not with a hacker typing commands, but with a single infected download weeks ago. The defensive perimeter people imagine — a wall keeping criminals out — has already been bypassed. The criminals are already inside.

## Continuity Notes

### Thematic Links (use sparingly)

- The infostealer pipeline introduced here is the upstream supply for the AI-assisted phishing discussed in Chapter 7
- The IAB "lead generation" model connects naturally to Chapter 9's victimology argument (attackers choose victims based on pre-scored access inventory)

## Style Reminders

- Follow the book bible's voice guidelines exactly
- Target length: 3,500 — 5,000 words
- Maintain consistent POV and tense throughout
- No chapter subheadings — flowing prose only
