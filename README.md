<div align="right">
  <a href="README_zh.md">中文</a> &nbsp;|&nbsp; <strong>English</strong>
</div>

---

# Serenity Market Scout

**A Claude skill for Serenity-style thematic market research and equity deep dives.**

---

## What is this skill?

Serenity Market Scout is a research skill for Claude that replicates the core analytical process behind Serenity-style investment research — the kind that starts from a real-world demand shock, traces it through a supply chain, finds the structural bottleneck or functional monopoly, and surfaces the public-market beneficiaries most likely to be mispriced.

Unlike generic financial skills, this one is built around a specific, repeatable method with clearly defined evidence standards. Every output distinguishes between confirmed facts (filed disclosures, official transcripts, government grants), strong inferences (multiple near-primary signals pointing the same direction), and speculative leads (plausible but still needing verification). The result is a research artifact you can actually act on — not a list of tickers.

---

## Where does it come from?

The method behind this skill is adapted from the Serenity research framework, a bottleneck-first approach to equity idea generation developed for technology, industrials, and infrastructure themes. The framework treats markets as systems of constraints: the entity that controls the narrowest, hardest-to-replace link in a demand chain typically captures disproportionate economics and is the most durable long position.

The skill packages that method into a set of structured instructions and reference documents that Claude can load on demand — covering the scoring framework, source protocols, OSINT customer-mapping techniques, thematic taxonomy, and output templates.

---

## What can it do?

**Thematic discovery**  
Scan across industries for emerging demand shocks and the supply chains they stress. The skill does not require you to name a sector upfront — it can run open-ended discovery across equities and surface the highest-signal themes from first principles. Current coverage spans AI infrastructure (GPU, CPO, HBM, glass substrates), power and cooling, robotics and automation, stablecoins and payments infrastructure, and any adjacent area the research trail leads to.

**Bottleneck and functional monopoly identification**  
For each theme, the skill identifies where the supply chain is structurally narrow — a single material, a sole-source component, a certification gate, a geographic concentration — and maps which listed companies sit at that choke point.

**Equity candidate ranking**  
Candidate stocks are evaluated on a multi-factor framework: demand confirmation, bottleneck role, moat durability, customer revenue concentration, near-term catalyst, and valuation mismatch signal. Larger candidate sets can be scored programmatically and returned as a ranked table.

**Single-stock deep dives**  
Given a ticker or company name, the skill builds a structured research case covering terminal demand, the company's position in the value chain, customer mapping with confidence tiers, capacity and qualification status, the catalyst calendar, what the market may be missing, and the principal thesis-breakers.

**Social and subscription corpus synthesis**  
When you feed in content from X accounts, newsletters, or subscription research feeds, the skill builds a coverage ledger, extracts the investable ideas, maps them to the bottleneck framework, and returns a synthesized watchlist with sourcing notes.

---

## What is it used for?

- Building a thematic watchlist when a macro event, policy announcement, or product launch has changed the supply-demand picture in a sector
- Vetting a stock idea you already have — checking whether it actually holds a bottleneck position and what the evidence quality is
- Synthesizing a large volume of market commentary or analyst notes into a short, high-signal research memo
- Generating the raw material for an investment pitch, portfolio review, or sector update
- Running a recurring market scan on a 6–24 month catalyst horizon to stay ahead of inflections before they are fully priced

---

## What value does it bring?

Most AI-assisted research tools produce output that looks like analysis but lacks a coherent method. This skill enforces a specific discipline: no ticker-first reasoning, no conclusions without stated evidence tier, no "undervalued" claims without an explicit explanation of what the market is missing and what needs to be verified next.

The result is research that is faster to produce than manual work, transparent about its own uncertainty, and structured in a way that a second reader can challenge, extend, or hand off without losing the thread.

---

> All outputs are research reference material only and do not constitute investment advice.
