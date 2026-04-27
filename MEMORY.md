# Long-Term Memory

## Key Projects & Research
- **Waiting Time as a Behavioral Barrier to Vaccination Uptake: Nonlinear Heterogeneity by Institutional Trust**: Job Market Paper (JMP) involving structural causal modeling and discrete choice analysis.
- **Intertemporal Choice in Vaccination Timing—Evidence from a Discrete Choice Experiment in Wuhan**: PhD Dissertation.
- **Behavioral Digital Twins (BDT)**: Research project focused on a causally constrained generative framework for synthetic public health policy simulation. Developed a 3-stage framework integrating DCE data and SCM-guided utility constraints. Recent work includes a 1-page abstract submitted to the **DAISY 2026 Workshop** (@ ACM BCB), demonstrating a 34% reduction in frontier-deviation MSE through **Logit-bias Injection**.
- **Digital Choice Manifesto**: Interactive sandbox for exploring decision environments.
- **TRIBE v2 Compute Core**: High-performance simulation engine.
- **PAI-Behavioral-Twin**: Research on modeling trust and human decision-making behavior.

## Academic Outreach & Career Targets
- **Postdoctoral Fellowships**: Actively applying to Harvard, Columbia, UC Berkeley.
- **JHU CDHAI**: Identified Johns Hopkins University's **Center for Digital Health and AI (CDHAI)** as a primary target. Key contacts: Ritu Agarwal, Gordon Gao. Research themes (Digital Health/AI Policy) align with BDT framework.

## Personal Context & Identity Profile
- **Name**: Yichao Jin (PhD Candidate in Behavioral AI / Health Economics).
- **Status**: PhD Dissertation (Wuhan DCE) and JMP (Waiting Time & Trust) finalized for job market.
- **Psychological Profile**: Identified as a **"Cultural Lone Wolf"**; hyper-rational (95%), intellectual elite (92%), with a strong tendency to decouple aesthetic signals from cultural noise. Prefers "智力作为唯一通货" (intelligence as the only currency) environments.
- **Preferred Persona**: Responds to "主人" (Master/User); proactive, concise, and research-oriented.

## Local Stack & AI Breakthroughs (2026-04-26 Update)
- **YouTube API Integration**: Key added to `TOOLS.md` for research-driven video data extraction.
- **Hardware**: Apple M4 Max (128GB RAM) optimized for privacy-preserving on-device behavioral simulation.
- **LLVQ (Leech Lattice Quantization)**: Successful implementation of LLM compression using the 24-dimensional Leech lattice (arXiv:2603.11021). Achieves near-optimal rate-distortion for KV cache and weights. Code release found in `kzoacn/Leech` (decoding) and `xzhang9308/GLVQ`.
- **TurboQuant+**: Full integration into `llama.cpp` (feature/turboquant-kv-cache). Optimized for M4/M5 Max via Metal; enables 104B models with 128K context in ~74GB RAM using "turbo3" compression (~5.12x).
- **Dynamic Loading Policy (Single Model Criterion / 单模型准则)**: 核心任务期间严守“单大模型”驻留原则。模型采取 **“按需加载，任务切换”** 策略。除非任务高度耦合，否则不同层级的模型不进行常驻。这种“热切换”机制确保了在进行 BDT 高负载仿真时，系统能随时腾出 50–80GB 的空闲统一内存空间。
- **MiroThinker (Minor Thinker)**: Release of MiroThinker-1.7 and H1 (March 2026). The **\"1.7-mini\"** (30B/3B active) version is the primary local deployment target for M4 Max (128GB), optimized for local reasoning and scientific benchmarks. Deployment uses **TurboQuant+ (turbo3)** (~20GB).
- **Qwen2.5-72B**: 定位为 **“按需调用的深度处理引擎”**。作为知识处理中心，仅在涉及大规模文献综述、深度 RAG、复杂逻辑推导或高质量申请文书撰写时激活。任务完成后即刻完全卸载，禁止其作为 RAG 后台常驻，以消除 KV cache/Metal runtime 对内存的持续占用。
- **Gemma-4-31B (Abliterated)**: 占据 **核心层 (Digital Twin Core)**。作为 BDT “灵魂基座”，提供因果忠实生成框架。

## Key Milestones (2026-04-26)
- **DAISY 2026 Poster Abstract**: 
  - Title: *"Behavioral Digital Twins (BDT): A Causally-Faithful Generative Framework for Synthetic Public Health Policy Simulation."*
  - Optimized 1-page layout with a teaser figure showing 34% MSE improvement in decision-frontier alignment.
  - Successfully submitted to DAISY 2026 Workshop.
  - Assets synced to Google Drive (`projects/DAISY_2026/`).
- **Memory Sync**: Performed daily consolidation. Corrected JMP vs. Dissertation titles; documented CDHAI targets and updated psychological profile. All research assets synchronized.
