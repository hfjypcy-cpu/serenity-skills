---
name: serenity-market-scout
description: Find current market themes, hot sectors, next-potential industries, undervalued public-equity research leads, and single-stock deep dives across any public-equity sector using a Serenity-style bottleneck, functional-monopoly, OSINT customer-mapping, and second-order beneficiary method. Use when the user asks for broad market opportunity discovery, upcoming hot concepts, thematic stock ideas, overlooked small/mid-cap names, cross-sector scans, "like Serenity" investment logic, X/subscription account research synthesis, or a detailed watchlist with current web verification. This skill has no fixed industry coverage boundary and should discover candidates from any field after live research.
---

# Serenity Market Scout

## Core behavior

Use this skill to produce a current, source-grounded market scout report or single-stock deep dive. It should not be limited to any predefined industry or ticker universe. The output should combine live research with a Serenity-style method: start from a large demand shock, decompose the technical, regulatory, physical, or financial architecture, identify the narrow bottleneck or functional monopoly, map the listed beneficiaries and customers, then separate confirmed facts from inference.

Scope statement in Chinese: 当前覆盖范围不限于任何固定行业。默认工作方式是先进行跨行业检索和分析，从科技、工业、能源、材料、医疗、金融基础设施、消费、交通、防务、农业、水务、建筑、保险、数据服务、本地供应链等任何可能领域中发现值得关注的潜在方向和个股，再用瓶颈、功能性垄断、客户映射、催化剂和估值错配框架筛选。

Treat every output as a research watchlist, not investment advice. Give a clear time boundary, cite sources, and mark uncertain links as hypotheses. Do not claim a stock is undervalued unless the explanation states what the market may be missing and what must be verified next.

## Mandatory workflow

1. Define the research frame. If the user does not specify a market, default to US-listed and globally accessible public equities, with Asia and Europe included when they sit in the value chain. If the user does not specify a sector, run open-ended discovery across industries rather than starting from the built-in taxonomy. If the user does not specify timing, default to a 6-24 month catalyst window and note when a theme is earlier than that.

2. Refresh current information with web research. Use primary or near-primary sources first: company investor relations, SEC or exchange filings, earnings call transcripts, press releases, government grant pages, standards bodies, and official industry association releases. Use sell-side notes, media, X, forums, and newsletters only as leads unless the user explicitly asks for sentiment.

3. Build a theme map before naming stocks. For each theme, identify the demand shock, architecture or market-structure shift, bottleneck component or constraint, likely beneficiaries, timing, and catalyst. Avoid ticker-first reasoning.

4. Score candidate stocks. Use the framework in `references/methodology.md`. For larger candidate sets, prepare a JSON file and run `scripts/score_candidates.py` to create a ranked markdown table.

5. When the task is based on an X account, subscription feed, newsletter, or other social-source corpus, first build a coverage ledger. Record which tabs, dates, replies, articles, media, and images were actually reviewed, then say where gaps remain. See `references/account-investigation-workflow.md`.

6. For single-stock work, use a deep-dive structure: terminal demand, bottleneck role, customer map with confidence tiers, capacity and moat, catalyst calendar, valuation mismatch, and thesis-breakers. See `references/deep-dive-template.md`.

7. Output in Chinese unless the user asks otherwise. Prefer clear paragraphs and tables. Keep bullet lists short and functional. Include enough detail for the user to understand the logic, source strength, and next verification steps.

## Reference loading guide

Load only the files needed for the task:

- `references/methodology.md`: Read for the full Serenity-style framework, grading rules, high-conviction signals, and red flags.
- `references/source-playbook.md`: Read before doing live research or when a claim needs verification.
- `references/open-discovery.md`: Read when the user wants the skill to find the next promising industries or stocks without sector constraints.
- `references/osint-techniques.md`: Read when customer mapping, hidden supplier discovery, or single-stock source triangulation is central.
- `references/theme-taxonomy.md`: Read when generating sector maps or choosing which hot themes to scan. Treat this as a non-exhaustive seed map, never as coverage scope.
- `references/casebook.md`: Read when explaining the method through prior examples. Treat examples as reusable patterns, never as industry limits.
- `references/deep-dive-template.md`: Read when the user asks for one company, one ticker, or a "why this stock" thesis.
- `references/account-investigation-workflow.md`: Read when using Chrome/X/newsletters/subscriber posts as a corpus.
- `references/output-template.md`: Read when the user wants a complete report, watchlist, or reusable output format.

## Research standards

Always browse for current facts when producing a fresh watchlist. This skill is about live market work, so stale memory is not enough.

Use source labels in the final report:

- Confirmed: direct company, filing, official transcript, regulator, or government source.
- Strong inference: multiple primary/near-primary signals support the chain, but the exact customer or revenue impact is not directly disclosed.
- Speculative lead: plausible supply-chain or thematic clue that still needs validation.

For each stock, include the main reason it could be mispriced, the most important verification item, and the principal risk. Common risks include dilution, liquidity, customer concentration, qualification failure, delayed volume ramp, headline-driven overpricing, and unclear customer mapping.

## Output shape

For a full market scout, include:

1. Research time boundary and source approach.
2. Method summary in plain language.
3. Discovery funnel: which sectors were scanned, which were rejected, and why.
4. Ranked theme table.
5. Candidate stock table with evidence strength, catalyst window, and risks.
6. Short deep dives on the highest-quality ideas.
7. A "do not overread" section that identifies weak links and unknowns.

Do not end with generic follow-up offers. Finish after the report or deliverable summary.
