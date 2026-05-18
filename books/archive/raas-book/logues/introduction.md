# Introduction

*A Note on Sources, Scope, and the Peculiar Challenge of Writing About a Moving Target*

---

This book covers a twelve-month window: roughly Q1 2025 through Q1 2026.

That framing is deliberate and requires explanation, because ransomware is not a static subject. It is an industry in active evolution — developing new capabilities, absorbing new personnel, targeting new sectors, and adapting to each new disruption with the organizational resilience of a well-capitalized corporation. Writing about it is, in some respects, like writing about a company in the middle of its most aggressive growth phase. By the time a sentence is printed, the underlying reality has shifted.

The response to that challenge is not to pretend the text is timeless. It is to be specific about what evidence the analysis is grounded in and when that evidence was collected.

---

## The Source Foundation

Every factual claim in this book — every statistic, every named threat actor, every documented capability — traces to one of five primary research sources. They are identified here so that readers who want to go deeper can find the original material, and so that the analytical framework of the book is transparent rather than opaque.

**Report 1: Macro-Economic Structure and Market Consolidation of Ransomware-as-a-Service, Q1 2026.**
The core source for market data: group rankings, victim counts, consolidation statistics, and the detailed profiles of Qilin, The Gentlemen, LockBit 5.0, and Akira. Primary source authorities: Check Point Research and Mandiant's M-Trends 2026 report, with additional data from Huntress. This report provides the quantitative spine of Part One.

**Report 2: Recruitment, HR Practices, and Labor Partitioning in Ransomware Cartels, 2025–2026.**
The source for everything concerning the ransomware workforce: how operators are organized, how affiliates are managed, what initial access brokers do, how infostealers feed the criminal supply chain, and what insider threats look like in practice. Primary source authorities: Mandiant's M-Trends 2025 report and Unit 42. The UNC5537 Snowflake campaign and UNC3944 social engineering operations documented here are among the most instructive case studies in the book.

**Report 3: Technological Evolution of Ransomware Payloads and Automation, 2025–2026.**
The technical foundation for Part Two: AI-driven attack automation, the specific malware families PROMPTFLUX, PROMPTSTEAL, and PROMPTLOCK, and the emerging integration of post-quantum cryptographic algorithms into criminal tooling. Primary source authorities: ISACA and ENISA. The distinctions in this report between current capabilities and near-future risks are carefully preserved in the text.

**Report 4: Ransomware Extortion Mechanics, 2025–2026.**
The analytical foundation for Chapter 7: multi-extortion architecture, the psychology of ransom coercion, data leak site operations, countdown timers, proof-of-theft packages, and the sector-specific targeting of legal firms. Primary source authorities: GuidePoint Security's GRIT team, Chainalysis, BlackFog, and DeepStrike. The named case studies — Houston Symphony/Qilin, Rent-2-Own/Medusa, Vanan/KillSec — are documented incidents, not composites.

**Report 5: Strategic Targeting and Victimology of Ransomware Operations, Early 2026.**
The source for attack speed data, identity statistics, sector victimology, and the resilience stack targeting that defines modern ransomware strategy. Primary source authorities: Unit 42's 2026 Global Incident Response Report, drawn from more than 750 major incidents across more than fifty countries, and the European Parliamentary Research Service. The EPRS analysis provides the EU-specific geographic and sectoral dimensions that give this book its international scope.

---

## What These Reports Confirm — and What They Don't

Honest engagement with source material requires acknowledging its limits as well as its findings. Several specific constraints shaped this book's analysis:

The precise revenue-sharing arrangements between ransomware operators and their affiliates are not publicly documented with authoritative specificity for the Q1 2026 period. The structure — operators take a percentage, affiliates retain the rest — is well established. The exact percentages reported in some secondary analyses are not confirmed by the primary sources used here, and this book does not present them as fact.

The timing cited for access transfer in the criminal market — the description of credential sales and network access transactions as occurring at near-instantaneous speed — reflects an analytical characterization of market frictionlessness rather than a measured timing metric. It is directionally accurate; it is not a documented universal benchmark.

The integration of post-quantum cryptographic algorithms into live ransomware deployments is presented in the research as an emerging strategic risk, not a confirmed widespread operational reality. This book treats it accordingly — as an early warning that demands immediate defensive response, not as a description of current majority criminal practice.

No ransomware attack or criminal capability described in this book has been invented or extrapolated beyond what the source material supports. Where the book uses hypothetical vignettes — unnamed characters experiencing documented attack scenarios — this is clearly a narrative device to make abstract technical realities tangible. The vignettes illustrate real attack patterns; they are not reported incidents presented as fact.

---

## A Note on Names

The named threat actors in this book — Qilin, LockBit, The Gentlemen, Akira, CLOP, UNC5537, UNC3944, and others — are tracked entities in published security research. Their activities are documented by the organizations cited above. The named malware families — VIDAR, RISEPRO, REDLINE, RACCOON STEALER, LUMMA, METASTEALER, PROMPTFLUX, PROMPTSTEAL, PROMPTLOCK — are similarly documented in published threat intelligence.

No individual criminal is identified by their real name in this book. The criminal ecosystem operates under aliases, organizational handles, and deliberate anonymity. Where individuals are discussed, they are discussed through the organizational structures they operate within.

---

## The Intended Audience

This book was written for readers who are not security professionals but who need to understand the threat as well as any security professional does.

That includes the CEO of a manufacturing company who is about to learn what percentage of European ransomware attacks target their sector. The board member who believes that cybersecurity is an IT problem rather than a business survival problem. The hospital administrator who has been told that backups are sufficient protection against ransomware and has not yet learned that attackers routinely neutralize backups before deploying encryption. The mayor of a mid-sized city whose municipality has no incident response plan. The owner of a small business who has assumed, incorrectly, that their size makes them invisible to criminal organizations that have decided small is the new prime target.

It was also written for anyone who is simply trying to understand what is happening — in the invisible war being waged across the world's digital infrastructure, at this moment, at scale. The stakes of that war are not abstract. They are measured in disrupted hospitals, silenced factories, collapsed small businesses, and accumulated human costs that no public data source fully captures.

Understanding the war is not the same as winning it. But it is the necessary beginning.

---

## How to Read This Book

*Ransomware, Inc.* is structured in four parts that build on each other.

**Part One: The Corporation** (Chapters 1–3) establishes the organizational reality of modern ransomware — market structure, business model, workforce architecture. Read it to understand that this is not a technology story. It is a business story.

**Part Two: The Arsenal** (Chapters 4–5) examines the weapons now in use — AI-driven automation and emerging post-quantum cryptographic defenses. Read it to understand how the technical threat has evolved beyond the images most people carry.

**Part Three: The Hunt** (Chapters 6–7) analyzes targeting strategy and psychological coercion — who gets attacked and why, and what happens after the ransom note arrives. Read it to understand why the organizations that believe they are safe are often the most exposed.

**Part Four: The Reckoning** (Chapter 8) synthesizes the defensive response. Read it last, when the full weight of the preceding seven chapters has settled, and the question of what to do has become genuinely urgent.

The Prologue and Epilogue frame the book as a story about a specific attack and a near-term future. They are the human ends of an analytical arc.

Start at the beginning. The first chapter begins, as all good horror stories do, with a reassurance that no longer holds.

---

*The threat is not distant. It is operational, right now, at scale. That is what all of this was written to make visible.*
