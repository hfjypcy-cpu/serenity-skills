#!/usr/bin/env python3
"""Score Serenity-style market scout candidates.

Input JSON schema:
[
  {
    "ticker": "SAMPLE",
    "company": "Sample Co",
    "theme": "Cross-sector bottleneck theme",
    "bottleneck": "regulated capacity or hard-to-replace component",
    "evidence": 4,
    "bottleneck_strength": 5,
    "timing": 4,
    "valuation_mismatch": 3,
    "risk_quality": 2,
    "discovery_gap": 5,
    "catalyst": "customer qualification or policy catalyst",
    "risk": "timing, dilution, or customer concentration",
    "source": "company filing or primary-source release",
    "notes": "optional"
  }
]

Scores must be integers from 0 to 5. The script prints a ranked Markdown table.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCORE_FIELDS = [
    "bottleneck_strength",
    "evidence",
    "timing",
    "valuation_mismatch",
    "risk_quality",
    "discovery_gap",
]


def _as_score(value: Any, field: str, ticker: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{ticker}: {field} must be an integer from 0 to 5")
    try:
        score = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{ticker}: {field} must be an integer from 0 to 5") from exc
    if score < 0 or score > 5:
        raise ValueError(f"{ticker}: {field}={score} is outside 0-5")
    return score


def total_score(item: dict[str, Any]) -> int:
    ticker = str(item.get("ticker") or item.get("company") or "UNKNOWN")
    return sum(_as_score(item.get(field, 0), field, ticker) for field in SCORE_FIELDS)


def bucket(score: int) -> str:
    if score >= 24:
        return "核心研究候选"
    if score >= 18:
        return "重点观察"
    if score >= 12:
        return "早期线索"
    return "暂缓"


def esc(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("\n", " ").replace("|", "\\|").strip()


def render_markdown(items: list[dict[str, Any]]) -> str:
    ranked = sorted(items, key=total_score, reverse=True)
    lines = [
        "| 排名 | 股票 | 公司 | 方向 | 瓶颈角色 | 总分 | 分层 | 催化 | 主要风险 | 来源/备注 |",
        "|---:|---|---|---|---|---:|---|---|---|---|",
    ]
    for idx, item in enumerate(ranked, 1):
        score = total_score(item)
        source_note = item.get("source") or item.get("notes") or ""
        if item.get("source") and item.get("notes"):
            source_note = f"{item['source']}; {item['notes']}"
        lines.append(
            "| {rank} | {ticker} | {company} | {theme} | {bottleneck} | {score} | {bucket} | {catalyst} | {risk} | {source} |".format(
                rank=idx,
                ticker=esc(item.get("ticker", "")),
                company=esc(item.get("company", "")),
                theme=esc(item.get("theme", "")),
                bottleneck=esc(item.get("bottleneck", "")),
                score=score,
                bucket=bucket(score),
                catalyst=esc(item.get("catalyst", "")),
                risk=esc(item.get("risk", "")),
                source=esc(source_note),
            )
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank Serenity-style market scout candidates.")
    parser.add_argument("input", help="Path to JSON candidate file, or '-' for stdin")
    args = parser.parse_args()

    if args.input == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(args.input).read_text(encoding="utf-8")

    data = json.loads(raw)
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of candidate objects")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each candidate must be a JSON object")
        total_score(item)

    print(render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
