# OSINT Techniques

## Table of Contents

- Purpose
- Evidence tiers
- Customer mapping
- Hidden supplier discovery
- Timeline and catalyst reconstruction
- Valuation and mismatch checks
- Failure controls

## Purpose

Use this reference when the edge depends on reconstructing a customer, supplier, or capacity chain that is not fully disclosed in one source. The goal is to build a defensible hypothesis while making the weak links visible.

## Evidence tiers

Use three confidence tiers for non-obvious links:

- Confirmed: direct company, customer, filing, regulator, government, exchange, or official partner source names the relationship or product.
- High-confidence inference: several independent clues point to the same relationship, such as geography, unit volume, timing, funding amount, product specs, and customer language.
- Open hypothesis: the link is plausible but depends on one or two indirect clues.

Never upgrade a customer link because it is attractive. Upgrade it only when the evidence chain improves.

## Customer mapping

Useful customer-mapping methods:

- Compare customer language across supplier presentations, customer roadmaps, and conference transcripts.
- Match product generation, module speed, wavelength, process node, package type, or qualification timing.
- Match volume clues. An RFQ for tens of millions of units can suggest consumer hardware, while a small number of high-value systems may suggest telecom, defense, or AI infrastructure.
- Match geography and segment disclosure. A revenue line in Finland, Korea, Taiwan, Israel, or the US may narrow the customer set when the supplier has few customers in that region.
- Match funding amounts or grant descriptions to public program awards.
- Use archived websites to detect newly added or removed customer logos, product pages, partner claims, and market language.
- Compare job postings, facility locations, manufacturing partners, and import/export descriptions with disclosed product ramps.

Present the map as a table with customer, link type, confidence tier, supporting clues, missing proof, and revenue materiality.

## Hidden supplier discovery

Start from the architecture, not the ticker. Search for the non-obvious component that must scale before the downstream product can ramp.

Useful trails:

- Customer product architecture and standards documents.
- Supplier pages for materials, wafers, lasers, FAU, substrates, bonding, inspection, metrology, power shelves, cooling hardware, sensors, or specialty chemicals.
- SEC and exchange filings that list customers, competitors, segment revenue, capacity, backlog, and concentration risk.
- Government grant pages, EU or US industrial-policy awards, defense procurement pages, and local-language press releases.
- Archived supplier pages, conference exhibitor lists, patent assignee searches, and technical conference programs.
- Competitor filings. A peer may describe the market structure more clearly than the target company.

For each hidden supplier, record whether it is a bottleneck, a capacity beneficiary, a design-win beneficiary, or merely a thematic participant.

## Timeline and catalyst reconstruction

Build a sequence:

1. R&D or design collaboration.
2. Sampling or prototype.
3. Qualification.
4. Capacity expansion.
5. Initial production.
6. Volume ramp.
7. Revenue recognition.

Public markets often price the story before revenue, but the strongest window usually begins when qualification, capacity, or customer capex becomes visible. If volume is more than 24 months away, mark the idea as early unless a financing, policy, or customer event has moved the timeline forward.

## Valuation and mismatch checks

Look for mismatch between the new bottleneck role and the current market framing:

- The company is still valued as a legacy business.
- The relevant segment is hidden inside a small line item.
- The stock is listed in a less-covered market or trades under multiple tickers.
- Sell-side or media coverage focuses on the downstream winner while omitting the upstream constraint.
- The pipeline, backlog, or capacity target is large relative to current revenue or market cap.

Treat mismatch as a hypothesis until current valuation, dilution, liquidity, and segment materiality are checked.

## Failure controls

Common failure modes:

- Mistaking a supplier for a bottleneck when it is one of many.
- Treating a customer rumor as confirmed.
- Ignoring dilution, debt, or funding needs in small caps.
- Overweighting old investor decks after the product roadmap changes.
- Using X posts or screenshots as final proof.
- Forgetting that qualification can fail or volume can shift to a second source.

State the top thesis-breaker in every deep dive.
