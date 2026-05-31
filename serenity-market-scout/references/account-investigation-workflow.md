# Account Investigation Workflow

## Table of Contents

- Purpose
- Coverage ledger
- Chrome and X collection pattern
- What to extract
- Handling images, tables, replies, and subscriptions
- Synthesis rules
- Coverage statement

## Purpose

Use this when researching an X account, paid subscription tab, newsletter archive, or similar corpus. The goal is to learn the person's method, not merely collect tickers.

## Coverage ledger

Before synthesis, create a lightweight ledger:

- Source: profile, Posts, Replies, Subs, Highlights, Articles, Media, external links.
- Date range actually reviewed.
- Number of unique posts or articles captured when available.
- Gaps: replies not loaded, media not OCRed, images not transcribed, deleted posts, protected content, paywall limits, or virtual-scroll cutoff.
- Confidence in coverage: high, medium, or partial.

The final report should say what was reviewed and what remains incomplete.

## Chrome and X collection pattern

For long X feeds, use a repeatable loop:

1. Open the tab and wait for posts to render.
2. Expand visible "Show more" or equivalent controls before extracting text.
3. Extract visible articles or post containers, including status URL, handle, display name, timestamp, text, metrics if visible, image count, and subscription marker.
4. Deduplicate by status ID or URL.
5. Scroll by view height and repeat until dates reach the target window or no new IDs appear.
6. Periodically save the accumulator in memory or a scratch object, because X virtualizes the DOM and older visible nodes disappear.

When direct DOM extraction fails, combine accessibility tree text, screenshots, and manual inspection. Avoid claiming full coverage if the page stops loading or time limits prevent older posts.

## What to extract

For each post or article, capture:

- Topic and ticker mentions.
- Stated position: held, no position, passed, watching, tiny position, conviction, or bragging-rights only.
- Thesis type: bottleneck, functional monopoly, policy catalyst, liquidity/flow, valuation mismatch, or event trade.
- Evidence type: primary source, management comment, image/table, X rumor, analyst report, or inference.
- Time horizon and catalyst.
- Risk language and invalidation conditions.
- Whether the idea later evolved, was abandoned, or became a core framework.

This separates the person's process from a static list of names.

## Handling images, tables, replies, and subscriptions

Images often contain the real evidence: customer tables, conference slides, backlog charts, maps, and product roadmaps. If images drive the thesis, inspect or OCR them and say which images were not reviewed.

Replies are useful for stance calibration. They often reveal what the account rejects, how it handles pushback, and whether a ticker is a core idea or only a passing note.

Subscription posts may carry early-stage ideas, position sizing clues, or process notes. Record whether the subscription tab was covered across the full date range or only sampled.

Articles usually contain the most reusable frameworks. Read them as method documents, then map later posts back to those frameworks.

## Synthesis rules

Synthesize at three levels:

- Philosophy: how the account thinks about markets, timing, risk, and edge.
- Process: how ideas are discovered, verified, sized conceptually, and abandoned.
- Playbook: repeatable templates, theme maps, and stock-screening rules.

Do not overfit to current tickers. The durable output is the method for finding the next set of bottlenecks.

## Coverage statement

End an account investigation with a direct coverage statement:

```
Coverage reviewed: [tabs, date range, approximate unique posts/articles].
High-confidence findings: [frameworks supported across many posts].
Partial findings: [areas sampled but incomplete].
Known gaps: [replies/media/images/older posts not fully reviewed].
```

This prevents a partial scrape from sounding like a complete archive.
