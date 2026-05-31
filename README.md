<div align="center">

[中文](#中文) &nbsp;|&nbsp; [English](#english)

</div>

---

<a id="中文"></a>

# Serenity Market Scout

## 这是什么技能？

Serenity Market Scout 是一个面向 Claude 的研究技能，复现了 Serenity 风格投研的核心分析过程——从真实的需求冲击出发，沿供应链追溯，找到结构性卡脖子环节或功能型垄断，最终浮现公开市场中最可能被低估定价的受益标的。

与通用金融类技能不同，这套技能围绕一套可复现的具体方法构建，并设有清晰的证据强度分级标准。每份输出均区分：已确认事实（公司公告、官方会议纪要、政府拨款页面）、强推断（多个近一手信源指向同一结论）以及投机线索（逻辑可信但尚待核实）。最终产出是真正可供使用的研究素材，而非一张股票代码列表。

## 这个技能从何而来？

本技能的底层方法来源于 Serenity 研究框架——一套以"卡脖子优先"为核心的股票创意生成方法论，专为科技、工业和基础设施主题而设计。该框架将市场视为约束系统：控制着需求链中最窄、最难被替代节点的主体，通常能够获得不成比例的超额收益，也是最具持久性的多头头寸。

本技能将该方法论打包为一套结构化指令与参考文档，Claude 可按需加载，内容涵盖评分框架、信源分级协议、OSINT 客户映射技巧、主题分类图谱和输出模板。

## 它能做什么？

**主题发现**  
跨行业扫描新兴需求冲击及其压力传导路径。使用时无需预先指定行业，技能可从第一性原理出发进行开放式发现，找出信号最强的主题。当前覆盖范围包括：AI 基础设施（GPU、CPO、HBM、玻璃基板）、电力与散热、机器人与自动化、稳定币与支付基础设施，以及研究路径延伸至的任何相邻领域。

**卡脖子与功能型垄断识别**  
对每个主题，技能识别供应链中结构性收窄的位置——单一原材料、唯一来源零部件、认证壁垒、地理集中度——并映射哪些上市公司坐落在这个卡口位置。

**候选股评分排序**  
通过多维度框架对候选标的进行评估：需求确认度、卡脖子角色、护城河耐久性、客户收入集中度、近期催化剂、估值偏差信号。较大候选集可程序化评分，以排序表格形式返回。

**个股深潜**  
给定一个代码或公司名称，技能构建完整的结构化研究案例，涵盖：终端需求、公司在价值链中的定位、分置信度层级的客户图谱、产能与认证状态、催化剂日历、市场可能忽视的信息盲点，以及主要论点破坏因素。

**社交与订阅语料合成**  
输入来自 X 账号、Newsletter 或订阅研究源的内容，技能构建覆盖台账，提取其中的可投资逻辑，将其映射至卡脖子框架，并返回带信源注释的合成观察名单。

## 适用场景

- 宏观事件、政策公告或重磅产品发布重新改变某行业供需格局后，快速构建主题观察名单
- 验证已有股票想法——检查该标的是否真正占据卡脖子地位，以及证据质量如何
- 将大量市场评论或研报内容浓缩为一份简短、高信号密度的研究备忘录
- 生成投资路演、组合复盘或行业更新的原始研究素材
- 以 6–24 个月催化剂窗口为周期，持续运行市场扫描，在拐点被充分定价前提前卡位

## 它带来什么价值？

大多数 AI 辅助研究工具产出的内容形似分析，却缺乏一贯的方法论支撑。本技能强制执行一套明确的研究纪律：不允许先想代码再找理由、不允许在未说明证据等级的情况下下结论、不允许在未明确"市场忽视了什么"以及"还需核实什么"的前提下声称某标的"被低估"。

产出结果在比人工研究更快的同时，对自身不确定性保持透明，并以结构化方式呈现——第二个读者可以完整挑战、延伸或交接，而不会丢失研究脉络。

> 所有输出内容仅供研究参考，不构成任何投资建议。

## 在不支持 Skill 的客户端中使用

如果你使用的 AI 客户端无法加载 Skill（例如 Claude 项目指令、ChatGPT 项目指令，或任意单次对话），可以直接使用独立提示词版本，效果与 Skill 等价：

- **[中文提示词](./serenity-market-scout/prompt/zh.md)** — 适用于中文环境
- **[English Prompt](./serenity-market-scout/prompt/en.md)** — For English-language sessions

---

<a id="english"></a>

# Serenity Market Scout

## What is this skill?

Serenity Market Scout is a research skill for Claude that replicates the core analytical process behind Serenity-style investment research — the kind that starts from a real-world demand shock, traces it through a supply chain, finds the structural bottleneck or functional monopoly, and surfaces the public-market beneficiaries most likely to be mispriced.

Unlike generic financial skills, this one is built around a specific, repeatable method with clearly defined evidence standards. Every output distinguishes between confirmed facts (filed disclosures, official transcripts, government grants), strong inferences (multiple near-primary signals pointing the same direction), and speculative leads (plausible but still needing verification). The result is a research artifact you can actually act on — not a list of tickers.

## Where does it come from?

The method behind this skill is adapted from the Serenity research framework, a bottleneck-first approach to equity idea generation developed for technology, industrials, and infrastructure themes. The framework treats markets as systems of constraints: the entity that controls the narrowest, hardest-to-replace link in a demand chain typically captures disproportionate economics and is the most durable long position.

The skill packages that method into a set of structured instructions and reference documents that Claude can load on demand — covering the scoring framework, source protocols, OSINT customer-mapping techniques, thematic taxonomy, and output templates.

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

## What is it used for?

- Building a thematic watchlist when a macro event, policy announcement, or product launch has changed the supply-demand picture in a sector
- Vetting a stock idea you already have — checking whether it actually holds a bottleneck position and what the evidence quality is
- Synthesizing a large volume of market commentary or analyst notes into a short, high-signal research memo
- Generating the raw material for an investment pitch, portfolio review, or sector update
- Running a recurring market scan on a 6–24 month catalyst horizon to stay ahead of inflections before they are fully priced

## What value does it bring?

Most AI-assisted research tools produce output that looks like analysis but lacks a coherent method. This skill enforces a specific discipline: no ticker-first reasoning, no conclusions without stated evidence tier, no "undervalued" claims without an explicit explanation of what the market is missing and what needs to be verified next.

The result is research that is faster to produce than manual work, transparent about its own uncertainty, and structured in a way that a second reader can challenge, extend, or hand off without losing the thread.

> All outputs are research reference material only and do not constitute investment advice.

## Using Without Skill Support

If your AI client cannot load Skills (e.g., Claude project instructions, ChatGPT project instructions, or any single-session conversation), use the standalone prompt directly — it is functionally equivalent to the Skill:

- **[中文提示词](./serenity-market-scout/prompt/zh.md)** — For Chinese-language sessions
- **[English Prompt](./serenity-market-scout/prompt/en.md)** — For English-language sessions
