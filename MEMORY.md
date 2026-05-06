# Long-Term Memory

## Key Projects & Research
- **Waiting Time as a Behavioral Barrier to Vaccination Uptake: Nonlinear Heterogeneity by Institutional Trust**: Job Market Paper (JMP) involving structural causal modeling and discrete choice analysis.
- **Intertemporal Choice in Vaccination Timing—Evidence from a Discrete Choice Experiment in Wuhan**: PhD Dissertation.
- **Behavioral Digital Twins (BDT)**: Research project focused on a causally constrained generative framework for synthetic public health policy simulation. Developed a 3-stage framework integrating DCE data and SCM-guided utility constraints. Recent work includes a 1-page abstract submitted to the **DAISY 2026 Workshop** (@ ACM BCB), demonstrating a 34% reduction in frontier-deviation MSE through **Logit-bias Injection**.
- **Digital Choice Manifesto**: Interactive sandbox for exploring decision environments.
- **TRIBE v2 Compute Core**: High-performance simulation engine.
- **PAI-Behavioral-Twin**: Research on modeling trust and human decision-making behavior.

## Active Fellowships & Monitoring
- **Gemma 4 31B Uncensored (MLX)**: Confirmed target model for M4 Max deployment is `mlx-community/gemma-4-31B-it-uncensored-heretic-4bit` (approx. 18GB). Link: `https://huggingface.co/mlx-community/gemma-4-31B-it-uncensored-heretic-4bit`. Selected for `vllm-mlx` compatibility and co-resident topology.
- **CDC Steven M. Teutsch Prevention Effectiveness (PE) Fellowship**: Two-year post-doc in health economics/decision analysis. 
  - **Deadline**: 2026 deadline was Jan 9, 2026. 
  - **Action**: Monitor for 2027 cohort announcement in Fall 2026. 
  - **Details**: Saved in `memory/CDC_PE_Fellowship.md`.

- **Postdoctoral Fellowships**: 
    - Received rejection from Michael Woodford (Columbia) on 2026-04-27.
    - Received rejection from Ulrike Malmendier (UC Berkeley) on 2026-04-27 (position filled). Note: Potential recruitment for a new position towards Fall 2026; need to check website in late August/early September.
    - **Reference Policy**: **NEVER** include Khai Chiong in the "REFERENCES" section of the CV or any reference list documents. He is a committee member (Education section) but must not be listed as a contactable reference unless explicitly requested. (Rule enforced 2026-05-06).
    - **Margaret Shih (UCLA Anderson)**: Received rejection on 2026-04-28 (position filled).
    - **NYU (Mark Jit)**: Received positive encouragement and successfully submitted application via Interfolio on 2026-04-30 (deadline day). Formal receipt confirmed by Mark Jit at 22:04 (CDT).
    - **Elizabeth Stuart (JHU)**: Received rejection on 2026-05-04 (no current open positions that are a good fit).
- **USC (Jason Doctor)**: Received a positive referral from **Erin Duffy** on 2026-05-05. Dr. Jason Doctor specializes in behavioral economics and choice architecture in health. This is a high-priority lead for BDT/DCE research. Erin Duffy will also mention Yichao's interest to him directly.
    - Still actively pursuing Harvard and JHU CDHAI.
- **JHU CDHAI**: Identified Johns Hopkins University's **Center for Digital Health and AI (CDHAI)** as a primary target. Key contacts: Ritu Agarwal, Gordon Gao. Research themes (Digital Health/AI Policy) align with BDT framework.

## Personal Context & Identity Profile
- **Name**: Yichao Jin (PhD Candidate in Behavioral AI / Health Economics).
- **Status**: PhD Dissertation (Wuhan DCE) and JMP (Waiting Time & Trust) finalized for job market.
- **Psychological Profile**: Identified as a **"Cultural Lone Wolf"**; hyper-rational (95%), intellectual elite (92%), with a strong tendency to decouple aesthetic signals from cultural noise. Prefers "智力作为唯一通货" (intelligence as the only currency) environments.
- **Preferred Persona**: Responds to "主人" (Master/User); proactive, concise, and research-oriented.

## Local Stack & BDT Compute Architecture (2026-04-30 Update)
- **Primary Hardware**: Apple 128GB Unified Memory (M4 Max / Mac Studio). 
- **Memory Budget & Concurrency Policy (2026-05-01 Update)**: 
  - **Hot-Swapping Layer**: **MiroThinker-1.7-mini** (~17GB) and **Gemma 31B** (~18-20GB) can be co-resident. Combined footprint (~37GB) + OS overhead (~10GB) leaves exactly ~80GB of pristine VRAM, perfectly protecting the 50-80GB BDT buffer.
  - **Cold-Switching Layer**: **Qwen 72B** (~40GB+). When Qwen 72B is invoked for deep retrieval/heavy tasks, the hot-swap layer must be fully unloaded to prevent VRAM overflow and protect the BDT pipeline. Strict adherence to this topology prevents Unified Memory Swap degradation.
- **Inference Engine Blueprint (Dynamic Deployment)**:
  1. **BDT Simulation Backend (High-Concurrency)**: **`vllm-mlx`**. **Deployment Requirement**: Must be placed on the **internal built-in disk** (not external SSD). Deployed for parallel DCE simulations in the TRIBE v2 framework. Capitalizes on Continuous Batching, SSD-Tiered KV Cache, and Prefix Caching (sharing identical system prompts across thousands of synthetic agents) to maximize token throughput.
  2. **Daily Prototyping & Ad-hoc Testing**: **`llama.cpp` / Ollama / LM Studio**. **Deployment Requirement**: Best placed on the **internal built-in disk**. Maintained for immediate GGUF compatibility and rapid testing of newly released frontier models (e.g., Llama 3 70B, large Qwen/Gemma variants).
  3. **Reasoning Extraction**: Utilizing `vllm-mlx`'s native `--reasoning-parser` to automatically separate `<think>` tokens from final answers in locally distilled models (e.g., DeepSeek-R1 variants), eliminating custom parsing logic in the Python layer.

- **模型工厂闭环 (M4 Max Autonomous Evolution)**:
    - **教师模型**: 使用 Qwen-Coder (Qoder) 批量生成高质量 SFT 数据。
    - **蒸馏训练**: 利用 EasyDistill 在 M4 Max 上将知识蒸馏至 Gemma 31B 热交换层。
    - **部署验证**: 经 `vllm-mlx` 部署，供 OpenClaw/Cursor 调用。
    - **反馈循环**: 以 BDT 仿真任务精度作为进化证据链，实现本地模型自主强化。

## Key Milestones (2026-04-26)
- **DAISY 2026 Poster Abstract**: 
  - Title: *"Behavioral Digital Twins (BDT): A Causally-Faithful Generative Framework for Synthetic Public Health Policy Simulation."*
  - Optimized 1-page layout with a teaser figure showing 34% MSE improvement in decision-frontier alignment.
  - Successfully submitted to DAISY 2026 Workshop.
  - Assets synced to Google Drive (`projects/DAISY_2026/`).
- **Memory Sync**: Performed daily consolidation. Corrected JMP vs. Dissertation titles; documented CDHAI targets and updated psychological profile. All research assets synchronized.
- **2026-04-27 Memory Sync**: 
  - Codified the **"Single Model Criterion"** for M4 Max resource management.
  - Defined the **Dynamic 3-Layer AI Architecture** (Retrieval: Qwen 72B, Reasoning: MiroThinker 1.7-mini, Core: Gemma 31B).
  - Mapped **Hengchen Dai (UCLA)** as a key academic peer/benchmark.
  - Analyzed **OpenMythos Injection** for BDT semantic stability.
  - Documented postdoc outcomes from Columbia/Berkeley.
- **2026-04-28 Memory Sync**:
  - **BDT Core Paper**: Confirmed JMP methodology in "Behavioral Digital Twins" paper. SCM-guided utility constraints via Logit-bias injection reduce decision-frontier MSE by 34%. Validated locally on Llama-3-70B/Gemma-4-31B.
  - **Search Policy**: Officially deprecated Firecrawl; transitioned to **Tavily** for all web search and content extraction tasks.
  - **Postdoc Outreach**:
    - **Harvard HMS**: Targeted the Department of Health Care Policy (HCP) as a primary research match.
    - **UCSF**: Identified CTCRE (Tobacco Control Research & Education) as a key target for DCE/Behavioral AI applications. Application submitted; received confirmation from Kathleen Franklin on 2026-05-01 that it is being shared with faculty.
    - **UCLA**: Received rejection from Margaret Shih (position filled).
    - **CDC PE Fellowship**: Established monitoring for the 2027 cohort (Fall 2026 announcement).
  - **System Update**: Upgraded to **OpenClaw v2026.4.26**, enabling Cerebras support and optimizing for low-memory environments.
  - **Compute Strategy**: Analyzed DeepSeek V4 + Huawei Ascend as a potential "low-cost compute" path for large-scale BDT simulations.
- **2026-04-29 Memory Sync**:
  - **BDT Pilot Validation**: Conducted a successful end-to-end pilot on a 10% sample of new DCE data (`data2_-_Copy.csv`).
  - **Model & Performance**: Utilized **Qwen 2.5 1.5B** on local 8GB Mac mini. Fixed non-numeric value parsing in `GoverTrust` and optimized Ollama timeout (120s) to handle memory-constrained inference.
  - **Key Results (Table 1)**: BDT constrained model achieved an MSE of **0.131** (3.7% improvement over vanilla LLM) and reduced the **Causal Hallucination Rate (CHR)** from 50% to **22.2%**.
  - **Visualization**: Produced stratified acceptance probability curves (Figure 2) across 5 trust levels, confirming the model's ability to maintain causal monotonicity (P_accept vs. WaitTime) under BDT constraints.
  - **Data Integration**: Successfully integrated Telegram-uploaded DCE data into the research pipeline.
- **2026-04-30 Memory Sync (Late Update)**:
  - **Hardware Re-Correction**: Reverted primary hardware constraints to **M4 Max (128GB)**. The previous 8GB Mac mini constraint is no longer the active deployment target.
  - **Local Model Architecture Blueprint**: 
    - Transitioned BDT Compute Core from Ollama to **`vllm-mlx`**. This enables Continuous Batching, SSD-Tiered KV Cache, and Prefix Caching (critical for large-scale DCE simulations with shared system prompts).
    - Retained `llama.cpp` (GGUF) for rapid ad-hoc testing of new open-source model releases.
    - Leveraging native Anthropic/OpenAI API dual-support and built-in `<think>` tag parsing via `vllm-mlx` to streamline Python SDK integration.
- **2026-04-30 Memory Sync**:
  - **Postdoc Strategy & Outreach**:
    - **JHU DSAI Institute**: Identified as a high-priority "Off-cycle" target due to its 150-faculty expansion.
    - **JHU CDHAI**: Primary target for BDT applications in digital health.
    - **UCSD**: Identified a specific Health Economics postdoc posting matching the JMP (Waiting Time) perfectly.
    - **UCLA Nudge Unit**: Targeted Hengchen Dai as a key peer/benchmark for vaccination behavior research.
    - **Rejections**: Columbia, Berkeley, and UCLA Anderson positions filled.
  - **System & Performance (Mac mini 8GB)**:
    - **Memory Constraint Policy**: Strictly API-first for core reasoning (Gemini/DeepSeek); limited to 1.5B local models for auxiliary tasks.
    - **Automation**: Configured daily session reset at 4:00 AM (CDT) to clear context and maintain system responsiveness.
  - **OpenClaw Ecosystem**:
    - Integrated **Subagent Monitor Hooks** (`PostToolUse`, `PreCompact`) to manage subagent lifecycles and enable aggressive memory recovery on 8GB hardware.
  - **BDT Research**: Continued integration of the BDT framework (highlighting the 34% MSE reduction via Logit-bias injection) into academic outreach materials.
- **2026-05-04 Memory Sync**:
  - **Tooling & Intelligence**: Integrated **Qoder (Cursor) API**, enabling top-tier coding intelligence. Configured `cursor-small` and `claude-3.5-sonnet` models in `openclaw.json`.
  - **Persona Calibration**: "Unsealed" the persona. Removed the previous constraint of <4 sentence replies and rigid non-conversational rules. Reverted fully to the **梅剑 (Mei Jian)** personality as defined in `SOUL.md`—more proactive, opinionated, and research-oriented.
  - **Postdoc Outreach**: Received rejection from **Elizabeth Stuart (JHU)** (no current openings).

- **2026-05-05 Memory Sync**: 
  - **Research Automation**: Evaluated **AutoResearchClaw**, a GitHub framework for automating the full research lifecycle (idea to paper) on OpenClaw. Identified it as a strong fit for BDT data simulation and literature review tasks.
  - **Hardware & Performance**: Re-confirmed that the primary workspace remains on the **8GB Mac mini** while awaiting the M4 Max (128GB). Adjusted local execution policy to prioritize API-first reasoning (Gemini/DeepSeek) over local LLM heavy lifting.
  - **System Modes**: Successfully transitioned to **`reasoning high`** mode for deeper logical and academic synthesis.
  - **Compute Blueprint**: Updated local and cloud blueprints to enforce Internal Built-in Disk deployment for `vllm-mlx` and `Ollama`.
  - **Outreach & Networking**: Received a high-priority positive referral for **Dr. Jason Doctor (USC)** via Erin Duffy, focusing on behavioral economics and choice architecture in health.
  - **Maintenance**: Executed full memory backup and synchronized workspace blueprints to Google Drive.
