# Chapter 4: The Map of Coercion

## Core Question
Why does the ransomware economy reliably hit manufacturing, healthcare, and digital infrastructure — and what does the map of victims reveal about what extortion actually rewards?

## Purpose in the Book
This chapter answers the question every reader silently asks when they hear "ransomware": *Why them? Why this hospital, this factory, this town?* It establishes that victim selection is not random or even purely opportunistic; it is shaped by what produces the most coercive leverage. The chapter introduces the strategic-targeting model — operational dependency as the real variable — and lays the groundwork for Chapter 5's deeper dive into the deliberate destruction of recovery.

## Required Content

### Must Cover
- ENISA's framing that ransomware accounted for 81.1% of cybercrime activity affecting EU organizations during the 2025 reporting period.
- Sector concentration: in the EU, manufacturing led ransomware claims with 14.9%, followed by digital infrastructure and services at 10.3%. Cybercrime overall: digital infrastructure and services 13.7%, manufacturing 13.26%, business services 9.7%. Data-breach claims: digital infrastructure 28.2%, public administration 16.8%.
- Geographic concentration: Germany 23.4%, Italy 11.33%, Spain 9.8%, France 9.5%, Belgium 3.7% as the top five most-named EU member states in ransomware and data-breach claims.
- The strategic logic: manufacturing, transport, digital infrastructure, finance, healthcare, media, and public administration present high extortion value because outages rapidly become production stoppages, public-service disruption, regulatory exposure, patient-safety risk, reputational harm, and contractual penalties.
- The shift from opportunism to operational-dependency targeting: the question is no longer who has money; it is who can least afford an outage.
- Technology-commonality victimology: as access supply chains industrialize, victim selection partly decouples from sector and follows shared technology stacks (a single Fortinet, SonicWall, Palo Alto, Citrix, or Oracle E-Business Suite exposure can yield victims across many sectors).

### Should Include
- A grounded opening: a vignette inside a hospital, factory, or municipal operation at the moment when its outage becomes a public crisis. Use only attack mechanics described in Report #5.
- The cautious framing that ransomware data is not a complete incident census; numbers are leak-site signals, with the caveats and convergences the report names.
- The brief framing that 2025 was characterized by elevated activity, fragmentation into more brands, and renewed Q4 acceleration — the strategic instability under which targeting decisions are being made.
- The setup line: choosing victims is not the only act of strategy. Choosing which *systems inside the victim* to compromise is what determines whether the organization survives. (This is the bridge to Chapter 5.)

### Optional (if it fits naturally)
- The CYFIRMA observation that December 2025 reached 801 incidents (highest in the four-year dataset) and that January 2026 rose to 683 from 511 in January 2025 — to drive home that elevated activity is now the baseline.

## Source Material Focus

Primary sources for this chapter:
- **Report #5:** Sector and geographic targeting, ENISA dataset, strategic-targeting framework, technology-commonality victimology, edge-device shift (set up here, deepened in Chapter 5).

## Required Source Files

Before drafting, read only these exact source files:
- `books/ransomware-inc/reports/task_1779014305_434487fb06.md`

Do not draft this chapter until these files have been read. Do not use reports not listed here unless the Book Bible explicitly requires it.

Key data points, quotes, or findings to incorporate:
- ENISA: ransomware = 81.1% of cybercrime activity affecting EU organizations.
- Manufacturing 14.9% of ransomware claims; digital infrastructure & services 10.3%.
- Cybercrime overall: digital infrastructure & services 13.7%; manufacturing 13.26%; business services 9.7%.
- Data-breach claims: digital infrastructure & services 28.2%; public administration 16.8%.
- Geographic: Germany 23.4%; Italy 11.33%; Spain 9.8%; France 9.5%; Belgium 3.7%.
- 2025 group count: 117 monitored (GRIT); public release 124 active groups (+46% YoY).
- Q4 2025: 2,287 (GuidePoint) / 2,416 (Check Point) victims; Q1 2026: 2,122.
- Sector logic: operational dependency, regulatory exposure, patient-safety risk.

## Structural Requirements

### Opening
Open inside one of the most operationally dependent victim types — a hospital scheduling system, a factory floor's logistics platform, a municipal water utility, or a regional logistics carrier — at the moment when the outage stops being an IT problem and becomes a public one. Then widen to the map.

### Body Flow
1. The opening operational-disruption scene → widen to the question of why this kind of organization keeps appearing in the data.
2. The sector and geographic data → translate into the strategic logic of operational dependency.
3. The technology-commonality angle: when affiliates buy access by software stack rather than by sector, victims become partially correlated by what they run.
4. The bridge: choosing the victim is only the first strategic decision. The second, and more decisive, is choosing which internal systems to break.

### Closing
End on the recognition that the map of victims is also a map of operational fragility — and that the next chapter is about how the attackers deliberately deepen that fragility once they are inside.

## Continuity Notes

### Thematic Links (use sparingly)
- The platform-economy framing from Chapter 1 echoes here through the technology-commonality angle; let it surface without explicit reference.
- Concepts that may naturally recur: resilience-denial targeting, edge-device exploitation, identity compromise (all deepened in Chapter 5).

## Style Reminders
- Follow the book bible's voice guidelines exactly.
- Expected length: write to editorial completeness. Most chapters likely fall around 4,000–6,500 words, but do not pad to reach a number. If the assigned story is complete and source coverage is sufficient, concise is preferred.
- Maintain consistent POV and tense throughout.
- ONLY `# Chapter 4: The Map of Coercion` as the heading — no subheadings inside the chapter body.
- No horizontal rules, no italic subtitle line, no bracketed citations.
