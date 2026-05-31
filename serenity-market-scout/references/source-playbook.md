# Source Playbook

## Table of Contents

- Source hierarchy
- Search patterns
- Evidence extraction
- OSINT triangulation
- Citation rules
- Verification checklist

## Source hierarchy

Use current web research for every fresh market scout. Prioritize sources in this order:

1. Company investor relations pages, press releases, annual reports, quarterly reports, and presentations.
2. SEC, EDGAR, exchange filings, stock exchange announcements, and regulator disclosures.
3. Earnings call transcripts and prepared remarks.
4. Government grants, industrial-policy documents, standards bodies, and official project award pages.
5. Official customer or partner announcements.
6. Reputable industry associations and primary technical bodies.
7. Financial media and sell-side notes as leads only, unless no primary source exists.
8. Social media, forums, and blogs as discovery leads only.

If a fact materially affects the investment logic and cannot be verified from a primary or near-primary source, label it as inference or unknown.

## Search patterns

Use targeted searches that combine the architecture, component, customer, and source type.

Examples:

- `<company> investor presentation AI data center 2026`
- `<company> earnings call transcript 1.6T CPO volume production`
- `<component> supplier Nvidia CPO press release`
- `<company> annual report photonics customer qualification`
- `<company> CHIPS Act grant semiconductor photonics`
- `<company> convertible notes ATM resale registration`
- `<ticker> market cap dilution investor presentation`
- `<customer> <supplier> co-packaged optics press release`
- `<technology> mass production 2027 supplier`

For non-US names, search both English and local-market identifiers when available. Use company names, exchange tickers, and product names.

## OSINT triangulation

Use OSINT only to build or strengthen an inference. It does not replace primary-source verification.

Useful checks:

- Archived webpages for customer logos, product pages, and language changes.
- Investor presentations across several quarters to catch new wording.
- Customer and supplier job postings that name product lines, process tools, or locations.
- Patent assignees and technical conference programs.
- Grant pages and local-government announcements.
- Competitor annual reports that identify market structure and customer categories.
- Product unit-volume, geography, and funding-amount matching.
- Sell-side or industry reports used as omission maps: note which obvious large players are covered, then search for missing upstream suppliers that enable the same architecture.

Label the result as confirmed, strong inference, or speculative lead.

## Evidence extraction

Extract only facts that help the thesis:

- Customer or partner name.
- Component or process supplied.
- Production stage: R&D, sampling, qualification, volume production, mass production.
- Timing: quarter, year, ramp window.
- Capacity: units, wafers, tools, modules, MW/GW, or other physical quantity.
- Backlog, pipeline, revenue guide, margin target.
- Financing, dilution, debt, convertible notes, ATM, share authorization.
- Government funding, grants, subsidies, strategic partnerships.

Then convert facts into thesis variables:

- Bottleneck role.
- Evidence strength.
- Catalyst window.
- Valuation mismatch.
- Principal risk.
- Next verification item.

## Citation rules

Cite sources in the final answer. For web sources, provide markdown links. Keep direct quotes short and use paraphrase. Do not overquote subscription or paywalled material.

Use source labels:

- `Confirmed`: direct company, filing, government, or regulator evidence.
- `Strong inference`: direct evidence supports most of the chain, but one link is inferred.
- `Speculative lead`: early clue requiring follow-up.

Do not cite X subscription text verbatim. Summarize its logic instead.

## Verification checklist

Before listing a stock as a research candidate:

- Verify the company still trades and identify the primary listing.
- Check market cap and major recent rerating if practical.
- Check whether the relevant segment is material or still tiny.
- Check whether the company has recent dilution, ATM, converts, or going-concern issues.
- Check whether the catalyst is within the user's time frame.
- Check whether the customer relationship is public, inferred, or speculative.
- Check whether the idea is already crowded or heavily promoted.

If live market data is unavailable, state that pricing and valuation must be refreshed before action.
