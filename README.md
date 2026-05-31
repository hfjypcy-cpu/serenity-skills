# serenity-skills

<details open>
<summary>🇨🇳 中文介绍</summary>

## 项目简介

**serenity-skills** 是一个面向 Claude 的技能（Skill）集合，提供 Serenity 风格的市场研究能力。

### 收录技能

#### [serenity-market-scout](./serenity-market-scout/)

一套基于 Serenity 投研方法论的市场侦察技能，覆盖主题发现、行业扫描、低估线索挖掘和个股深度研究。

**适用场景**

- 寻找当前 AI 基础设施、半导体、CPO、HBM、玻璃基板、算力、机器人、稳定币等热门赛道
- 跨行业扫描潜在机会，不受预设板块限制
- 合成 X/订阅号/Newsletter 的内容形成选股逻辑
- 对指定个股进行终端需求、供应链地位、客户图谱、催化剂日历和估值偏差的完整深潜

**核心方法**

从大需求冲击出发 → 拆解技术/监管/物理/财务架构 → 识别卡脖子环节或功能型垄断 → 映射 A 股 / 美股 / 港股受益标的 → 标注确认/强推断/投机线索三档证据强度。

**文件结构**

```
serenity-market-scout/
├── SKILL.md                          # 技能主文件（行为定义 + 工作流）
├── agents/
│   └── openai.yaml                   # Agent 接口配置
├── references/
│   ├── methodology.md                # Serenity 评分框架与红旗信号
│   ├── source-playbook.md            # 信源分级与核实流程
│   ├── open-discovery.md             # 无约束行业扫描指南
│   ├── osint-techniques.md           # 客户映射与隐性供应商侦察
│   ├── theme-taxonomy.md             # 热门主题分类种子图谱
│   ├── casebook.md                   # CPO/HBM4/电力/NeoCloud 等案例
│   ├── deep-dive-template.md         # 个股深潜输出模板
│   ├── account-investigation-workflow.md  # X/订阅号语料研究流程
│   └── output-template.md            # 完整报告与观察名单格式
└── scripts/
    └── score_candidates.py           # 候选股批量评分脚本
```

</details>

---

<details>
<summary>🇬🇧 English Introduction</summary>

## Overview

**serenity-skills** is a collection of Claude Skills that bring Serenity-style investment research capabilities to any Claude-powered workflow.

### Included Skills

#### [serenity-market-scout](./serenity-market-scout/)

A market-scouting skill built on the Serenity research methodology. It finds current thematic opportunities, scans sectors for undervalued leads, and produces single-stock deep dives — all grounded in live web research.

**When to use**

- Discover AI infrastructure, semiconductors, CPO, HBM, glass substrates, power, robotics, stablecoin, or any emerging sector plays
- Run open-ended cross-sector discovery without a predefined universe
- Synthesize X/subscription/newsletter feeds into stock selection logic
- Deep-dive a single ticker: terminal demand, supply-chain moat, customer map, catalyst calendar, and valuation mismatch

**Core method**

Large demand shock → architectural decomposition (technical / regulatory / physical / financial) → bottleneck or functional monopoly → listed beneficiary mapping (US / HK / A-share) → three-tier evidence labeling: Confirmed / Strong Inference / Speculative Lead.

**File layout**

```
serenity-market-scout/
├── SKILL.md                          # Skill entry point (behavior + workflow)
├── agents/
│   └── openai.yaml                   # Agent interface config
├── references/
│   ├── methodology.md                # Serenity scoring framework & red flags
│   ├── source-playbook.md            # Source tiering & verification protocol
│   ├── open-discovery.md             # Unconstrained sector scanning guide
│   ├── osint-techniques.md           # Customer mapping & hidden supplier OSINT
│   ├── theme-taxonomy.md             # Hot-theme seed taxonomy
│   ├── casebook.md                   # CPO / HBM4 / power / NeoCloud case studies
│   ├── deep-dive-template.md         # Single-stock deep-dive output template
│   ├── account-investigation-workflow.md  # X / subscription corpus workflow
│   └── output-template.md            # Full report & watchlist format
└── scripts/
    └── score_candidates.py           # Batch candidate scoring script
```

</details>

---

> **免责声明 / Disclaimer**  
> 本仓库所有内容仅供研究参考，不构成任何投资建议。  
> All content is for research reference only and does not constitute investment advice.
