# Methodology

## Table of Contents

- Core model
- Theme selection
- Bottleneck mapping
- Customer and evidence mapping
- Candidate grading
- High-conviction signals
- Stance taxonomy
- Pass and avoid signals
- Common mistakes

## Core model

The method starts from a large, unavoidable demand shock and walks down the supply chain until it finds a small, hard-to-replace constraint. The best candidates are not necessarily the most famous companies. They are often second- or third-order suppliers that become important only after a new architecture enters volume production.

Use this chain:

Demand shock -> architecture or market-structure shift -> bottleneck or functional monopoly -> beneficiary map -> listed company -> catalyst -> valuation mismatch -> risk check.

Examples of demand shocks include AI data center capex, rack-scale networking, HBM4, 800V DC power, liquid cooling, humanoid robots, LEO satellite deployment, stablecoin regulation, supply-chain sovereignty, defense procurement, grid modernization, water scarcity, healthcare reimbursement changes, biosimilar or GLP-1 supply shifts, insurance cycle changes, logistics automation, and new compliance mandates.

Examples of bottlenecks include lasers, FAU, external light sources, inspection, metrology, bonding, glass-substrate tools, high-end substrates, transformer capacity, switchgear, cooling hardware, harmonic reducers, force sensors, rare earth materials, specialty chemicals, permits, licenses, reimbursement access, regulated capacity, data rights, distribution, land, water, and specialized labor.

The strongest version of this method looks for a small market that can become strategically unavoidable. The market may begin as a niche material, tool, component, license, data layer, distribution channel, or regulated-capacity category, then re-rate when several larger systems need it at the same time.

## Theme selection

Prioritize themes with all of these properties:

1. A large buyer or policy force is already spending money.
2. The architecture, regulation, procurement pattern, or market structure is changing, so old comps and old coverage miss the new beneficiary set.
3. Volume production is near enough to matter in public markets, usually 6-24 months.
4. The bottleneck is physically, legally, commercially, or operationally hard to bypass.
5. Public equities exist that capture the bottleneck.

Themes that are technically exciting but still 2-4 years from volume ramp should usually be marked "too early" unless a clear financing, customer, or policy catalyst has pulled the timeline forward.

## Bottleneck mapping

For each candidate, answer these questions before assigning conviction:

- What exactly does the company provide?
- Which architecture or product cannot scale without that input?
- Who are the direct customers and one-hop end customers?
- Is the link confirmed, inferred, or speculative?
- Is the company sole source, primary source, dual source, or one of many?
- Does the company control output, IP, process know-how, capacity allocation, or certification?
- When does sampling, qualification, mass production, or revenue recognition occur?
- Does the expected revenue matter relative to current market cap?

Do not treat every supplier as a bottleneck. A supplier becomes a bottleneck when removal or undercapacity would delay the roadmap, impair yield, or force customers into inferior alternatives.

## Customer and evidence mapping

For hidden suppliers, build a customer map before writing the thesis. Use confidence tiers:

- Confirmed: direct company, filing, customer, regulator, government, or official partner source.
- Strong inference: multiple independent clues support the link, but the exact relationship is not directly disclosed.
- Open hypothesis: plausible link that still needs proof.

Useful clues include archived website changes, product-spec matches, qualification timing, geography, revenue concentration, funding amounts, unit volumes, job postings, foundry or manufacturing partner disclosures, and competitor filings. See `osint-techniques.md` for the full workflow.

Keep customer links separate from position stance. A company can have a real customer link while still being a poor investment because valuation, dilution, timing, or materiality is weak.

## Candidate grading

Score each candidate from 0 to 5 on six dimensions:

- Bottleneck strength: how hard it is to bypass.
- Evidence quality: how direct and current the source chain is.
- Timing: whether the catalyst falls in the 6-24 month public-market window.
- Valuation mismatch: whether market cap, multiples, or coverage appear disconnected from the new segment.
- Risk quality: inverse score for dilution, liquidity, financing stress, customer concentration, and technical risk.
- Discovery gap: whether the name is undercovered, non-US, small-cap, hidden in old segments, or not in obvious reports.

Suggested interpretation:

- 24-30: core research candidate.
- 18-23: watchlist candidate requiring targeted verification.
- 12-17: speculative lead.
- Below 12: too weak or too early unless the user asks for moonshots.

## High-conviction signals

Signals that can justify deeper work:

- Explicit customer qualification or production order.
- Management confirms demand exceeds supply.
- Pipeline or backlog grows faster than historical revenue.
- Gross margin target implies pricing power.
- Company controls a narrow technical component with few alternatives.
- The market still values the company on a legacy business.
- A government grant, strategic funding, or capacity expansion de-risks production.
- A bigger peer or downstream customer confirms the same architecture shift.
- The company appears repeatedly across independent supply-chain traces.

High conviction still requires risk disclosure. A good thesis can fail through timing, dilution, customer loss, or dual sourcing.

## Stance taxonomy

When synthesizing a public account or social-source corpus, classify every ticker mention by stance:

- Core holding or high conviction.
- Active watchlist.
- Tiny position or optional exposure.
- No position but interesting.
- Passed after research.
- Too early.
- Just a news note or sentiment comment.

This prevents casual mentions from being treated like portfolio ideas.

## Pass and avoid signals

Mark a candidate as "pass for now" when the technical story is interesting but:

- Volume ramp is more than 24 months away.
- The company is still in R&D or sampling with no customer conversion.
- Financing depends on repeated ATMs or toxic convertibles.
- The market already repriced the stock without new evidence.
- The candidate only has thematic proximity, not a true bottleneck role.
- The company depends on one customer that may dual source.
- The sourcing chain comes mainly from rumor, screenshots, or social posts.

Mark "too early" when the likely payoff is real but the public-market timing is poor. Record the trigger that would make it actionable, such as first qualification, revenue guide, new capacity, customer announcement, or standards adoption.

## Common mistakes

Avoid ticker-first work. Start with architecture and bottleneck.

Avoid treating market size as enough. A large TAM without a narrow capture mechanism does not create an investable edge.

Avoid copying a public personality's names after the stock has already rerated. Rebuild the evidence chain from current filings and sources.

Avoid assuming that "supplier to Nvidia" or "AI exposure" is meaningful. Identify the component, price content, production timing, and supply constraints.

Avoid hiding uncertainty. The method depends on inference, so the output must label what is confirmed and what is still a hypothesis.
