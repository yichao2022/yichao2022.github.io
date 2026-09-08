# JBI 审计总报告：EFR for LLM Synthetic Agents

**论文：** "Empirical-Frontier Regularization for LLM Synthetic Agents: A Proof-of-Concept Framework and Case Study in Vaccination Timing"

**作者：** Yichao Jin (UT Dallas)

**目标期刊：** Journal of Biomedical Informatics (JBI)

**日期：** 2026-07-08

**审计管线：** 5 独立审稿人（Domain / Methodology / Devil's Advocate / Perspective / Editorial Synthesis）

---

## 最终 verdict

**MAJOR REVISION — 一个周期可修，但前提是选对叙事。**

---

## 加权审稿总结

| 审稿人 | Verdict | 最致命的 1-2 个问题 |
|---|---|---|
| Domain Review | MAJOR REVISION | Related work 缺 8-10 篇 JBI 域内引用；论文读起来是卫生经济不是信息学 |
| Methodology Review | MAJOR REVISION | Matched subset 偏倚（21.9%，SMD>0.61）；缺少 uniform-shrinkage 基线归因 |
| Devil's Advocate | REJECT（当前版本） | 核心结果是设计参数不是实证发现；不能打败简单基线 |
| Perspective Review | 增补（无明确 verdict） | 完全缺少伦理/公平/文化泛化/数据隐私讨论 |
| Editorial Synthesis | MAJOR REVISION（一周期可修） | 核心争议是"架构 vs 发现"的叙事选择 |

---

## 共识矩阵

### 全部审稿人同意

| # | 问题 | 严重程度 |
|---|---|---|
| C1 | Matched subset 不具代表性——21.9% 覆盖，SMD > 0.61，N=226 | HIGH |
| C2 | 单数据集/单人群——不足以支撑泛化 claim | HIGH |
| C3 | 贡献真实但温和——概念新颖，方法简单，简洁性是卖点 | MODERATE |
| C4 | 需要重构为信息学论文——当前看起来太像卫生经济 | HIGH |

### 两名审稿人同意

| # | 问题 | 严重程度 |
|---|---|---|
| P1 | 缺少 uniform-shrinkage 基线——无法归因 | MODERATE-HIGH |
| P2 | LLM out-of-design 解释不当——anchor 主导，理解力 claim 未验证 | HIGH |
| P3 | 校准问题存在但可修——slope>1，metrics 不一致 | MODERATE |
| P4 | Held-out 差距——提出方法不打败基线，CIs 重叠 | HIGH |

### 单独提出

| # | 问题 | 来源 | 严重程度 |
|---|---|---|---|
| U1 | 缺失 8-10 篇 JBI 域内引用 | Domain | CRITICAL |
| U2 | 无临床部署/工作流整合讨论 | Domain | HIGH |
| U3 | λ 未交叉验证——但 sweep 足够 | Methodology | LOW |
| U4 | PRC 部分机械——需承认继承性 | Methodology | MODERATE |
| U5 | AUC 方向正确处理 | Methodology | LOW |
| U6 | 聚类 bootstrap 正确 | Methodology | ✅ CORRECT |
| U7 | CashIncentive 不匹配——脚注承认 | Methodology | LOW |
| U8 | LLM 可复现性问题 | Devil's Advocate | LOW-MODERATE |
| U9 | 现实世界适用性（stated→revealed） | Devil's Advocate | MODERATE |

---

## Top-5 修订优先级（损伤 × 可修复性）

| 优先级 | 项目 | 损伤 | 可修复性 | 修复方式 |
|---|---|---|---|---|
| 1 | **重构叙事：shrinkage 是架构设计不是实证发现** | CRITICAL | HIGH | 改写 Introduction + Discussion，无新实验 |
| 2 | **增加 uniform-shrinkage 基线** | HIGH | HIGH | 计算基线，一个图 + ~3 段 |
| 3 | **重构目标读者为信息学家** | HIGH | HIGH | DCE 方法论移附录，前移 LLM 架构 |
| 4 | **所有 claim 约束到单数据集范围** | MODERATE | HIGH | Discussion 加明确限制 + future work 小节 |
| 5 | **诚实处理 matched-subset 偏差** | MODERATE | HIGH | 标注为 exploratory，full-sample 为主 |

---

## 完整修订清单

### MUST（不修不投）

| # | 项目 | 来源 | 修复方式 |
|---|---|---|---|
| M-1 | **重构叙事**：shrinkage 是架构设计不是发现。标题结果 = 特征。Methods + Discussion 加显性论证 | DA（Mechanical shrinkage, CRITICAL） | 改写叙事；~2-3 段 |
| M-2 | **增加 uniform-shrinkage 基线**——分离 LLM 异质性收益与 shrinkage 本身 | Methods (F10), DA（So what） | 计算基线；1 图 + ~3 段 |
| M-3 | **重构目标读者为信息学家**——前移 LLM 合成代理架构，DCE 方法论移附录。翻转 60/40 比例 | Domain（定位, HIGH） | 结构改写；无新实验 |
| M-4 | **明确单数据集限制**——所有 claim 约束。Discussion 加 "Future Work: Multi-Study Validation" 小节 | Methods (F7), DA（单数据集, HIGH） | ~2 段 |
| M-5 | **降低 matched-subset 权重**——限制段落标注 N=226 为 exploratory，full-sample 为主 | 三方共识 C1 | ~1 段 Discussion |
| M-6 | **Calibration slope > 1 加解释句**——承认轻微乐观偏差，讨论临床含义 | Methods (F4) | 1-2 句 Results |
| M-7 | **统一校准指标**——logistic vs linear 一致性 | Methods (F9) | 重跑一致指标；~30min |
| M-8 | **PRC 继承性注**——给 DCE 因素的 credit 是预期之中的 | Methods (F3) | 1-2 句 Discussion |
| M-9 | **伦理声明**——stated vs revealed 偏差；自动化偏差；不操作声明 | Perspective | ~1 段 |
| M-10 | **数据隐私声明**——individual data 未发布；同意范围；cloud API 风险 | Perspective | ~1 段 |

### SHOULD（建议）

| # | 项目 | 来源 | 修复方式 |
|---|---|---|---|
| S-1 | **完善 JBI 文献引用**——TWIN-GPT, Yamin 2025, Goli & Singh 2024, DR.KNOWS 等（需作者验证） | Domain（Related work, CRITICAL） | 文献检索；验证每条引用 |
| S-2 | **Out-of-design 加解释限制**——anchor 主导；LLM 叙事理解 claim 需限定 | Methods (F6), DA（Out-of-design, HIGH） | ~1 段 Discussion |
| S-3 | **文化泛化边界**——武汉 COVID-zero 环境 vs 其他环境 | Perspective | ~1 段 |
| S-4 | **利益相关者缺失**——临床医生、政策制定者参与作为 future work | Perspective | ~1 段 |
| S-5 | **LLM 可复现性**——模型版本依赖性显性标注 | Methods (F6), DA | 1-2 句 Methods |
| S-6 | **临床部署/工作流讨论**——如何整合到 CDS | Domain（临床部署, HIGH） | ~1 段 Discussion |
| S-7 | **价值主张**：明确说明"本方法允许分析师用一个中等 DCE + LLM 估算异质性偏好，无需新数据采集" | DA（So what, HIGH） | ~2 句 Intro + Discussion |
| S-8 | **CashIncentive 不匹配**——脚注确认 DCE 属性的假设性 | Methods (F11) | 1 脚注 |

### COULD（锦上添花）

| # | 项目 | 来源 | 修复方式 |
|---|---|---|---|
| C-1 | 交叉验证 λ | Methods (F2) | 低优先级 |

---

## 贡献评估

### 真正的贡献

论文贡献了一个**透明度驱动的架构**，用于结合 LLM 合成代理与参数化经验贝叶斯 shrinkage 来估计陈述性偏好数据中的异质性偏好。新颖点：

1. **整合**——LLM 生成代理 + 形式化 shrinkage 框架（两者各自存在但未被整合）
2. **论证透明度**——参数化 shrinkage 使个人 vs 群体的权衡显式化和可审计
3. **可行性证明**——该架构在一个真实的 DCE 数据集上产生一致且方向合理的估计

### 未经验证的贡献（不能 claim）

- Shrinkage 在统计学意义上 *改善* 预测（held-out gap, CIs 重叠, matched subset 偏倚）
- LLM 代理 *理解* 临床叙事（未经测试，被 anchor 主导）
- 泛化到一个数据集以外
- 比无 LLM 的简单替代方案 *更好*

### 最低可发表版本（MVP）

> "We propose an architecture that uses LLM synthetic agents to inform differential shrinkage in empirical-Bayes preference estimation. The architecture is deliberately transparent: the shrinkage parameter λ is a design choice, not a learned parameter, making the analyst's assumptions explicit. We demonstrate feasibility on a single real-world DCE (N=1,027) and compare against uniform shrinkage. This is a proof-of-concept; generalization remains to be established."

---

## 路径评估

### 一个周期能修吗？

**能。** 前提是接受"架构 + 可行性"叙事，拒绝"效果更好"叙事。

- 8/10 个 MUST 为纯文字/重构（无新数据，无新实验）
- 1 个计算性 MUST（uniform-shrinkage 基线）为现有数据的重分析
- 核心方法本身无问题——问题出在**叙述**

### 核心决策问题

> **你这篇论文是关于"证明 LLM-informed shrinkage 效果更好"（需要更强的证据），还是关于"提出一个透明、LLM-informed shrinkage 的架构并证明可行性"（你现有的证据支持后者）？**

- 选前者 → trajectory = REJECT（需要新数据 + 新基线 + 多人群验证）
- 选后者 → trajectory = MAJOR REVISION → ACCEPT（概率高）

---

## 审稿人详情

### Domain Review (deleg_fb6797d8)

**Verdict:** MAJOR REVISION

**关键发现：**
- Related work（🔴 CRITICAL）：缺失 TWIN-GPT, Yamin 2025, Goli & Singh 2024, DR.KNOWS, DAKI, SynthAgent, Agent Hospital, AI Patient——整条 JBI 学术对话
- 定位（🟠 HIGH）：当前 60% 卫生经济 / 40% 信息学，需重构为 70% 信息学
- 临床部署（🟠 HIGH）：缺少工作流整合、医疗人员参与
- 贡献显著性（🟡 MODERATE）：概念新颖但方法简单，简洁性是透明度特征

### Methodology Review (deleg_8eeb3938)

**Verdict:** MAJOR REVISION

**关键发现（严重排序）：**
- F1 Matched subset（🟠 HIGH）：21.9% 匹配率，SMD > 0.61，评估偏倚
- F10 归因基线不足（🟠 MODERATE-HIGH）：需 uniform-shrinkage
- F3 PRC 机械继承（🟡 MODERATE）
- F4 校准斜率 > 1（🟡 MODERATE）
- F6 Out-of-design 模型不匹配（🟡 MODERATE）
- F9 校准指标不一致（🟡 MODERATE）
- F7 单数据集（🟡 MODERATE）
- F8 聚类 bootstrap：✅ CORRECT
- F2 λ 未交叉验证：LOW（sweep 充分）

### Devil's Advocate (deleg_2d80a2c1)

**Verdict:** REJECT（当前版本）

**关键发现（严重排序）：**
- Mechanical shrinkage（🔴 CRITICAL）：核心结果是设计参数，统计学证据不支持非机械贡献
- Held-out gap（🟠 HIGH）：提出方法比基线差，CIs 重叠
- Out-of-design 解释（🟠 HIGH）：anchor 主导，LLM 理解力未测试
- 单数据集（🟠 HIGH）：N=1,027 一个城市不足
- So what（🟠 HIGH）：不比简单替代方案好

### Perspective Review (deleg_63338eaf)

**Verdict:** 增补

**关键发现：**
- 伦理（伦理声明缺失）：stated vs observed 偏差、自动化偏差、不操作声明
- 数据隐私（同意范围、cloud API 数据传输风险）
- 文化泛化（武汉 COVID-zero → 其他环境）
- 利益相关者缺失（临床医生、政策制定者）
