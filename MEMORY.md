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

## 2026-06-14 Memory Consolidation

### Career & Job Market Updates
- **Julie Downs (CMU)**: Most active lead — interview pending, department review ongoing. Highest priority.
- **NIH OBSSR Fellowship**: Submitted via Zintellect on 2026-06-12. Review cycle starts 7/1.
- **Erin Duffy (USC Schaeffer Center)**: Warm contact (positive referral 2026-05-05). Follow-up email drafted (`erin_duffy_followup.txt`) for sending Mon 6/15 09:00 via cron. Includes CV attachment.
- **Yuyan Shi (UCSD)**: Rejected ❌ (confirmed 6/12-13). Deadline no longer relevant.
- **Saad Omer (UTSW)**: Soft rejection (dean-level template reply "check our website").
- **SJDM Abstract (VC H3)**: Deadline **June 16, 2026** — 2 days from now. Top priority.
- **Career Re-targeting (June 2026)**: Priority order: Business School MarkSci > medical decision research centers > health preference groups. NOT general public health. CV updated to "Behavioral AI Scientist" positioning (BDT→VC→JMP→Price). AP market monitoring to start from July 2026.

### Postdoc Job Search — New Leads (June 14 Cron)
| Lead | Match | Deadline | Status |
|------|:-----:|:--------:|:------:|
| **CU Boulder / Stephen Billings** (stephen.billings@colorado.edu) | High | Mar 13 passed | Email directly — $96K, causal inference+health |
| **HKU / Manuel Espinoza** (mesp@hku.hk) | Medium-High | Jul 17 | Health econ+DCE, Hong Kong position |
| **USC Schaeffer Center** | High | Year-round | Need to identify specific mentor |
| **Berkeley / Sam Pimentel** (spi@berkeley.edu) | Medium | Rolling | Causal inference+mhealth, but wants Stats PhD |
| **Heidelberg/Stanford Geldsetzer Lab** | Medium | Rolling | Causal EHR, Germany+remote+Stanford visiting |
| **Guelph / Hai Nguyen** (vanhai@uoguelph.ca) | High | Mar 31 ("open until filled") | DCE+drug policy+causal inference, perfect match but expired |
| **VA/Stanford BD-STEP** | Medium | Rolling | Citizen required ❌ |

### Meta-Conversation & Assistant Calibration (June 13 Telegram Session)
- **Correction**: User's PhD is from **UT Dallas EPPS** (School of Economic, Political and Policy Sciences), NOT UTD Business School (Jindal). This error was acknowledged and corrected during session.
- **Self-analysis acknowledgement**:
  - Assistant recognized a tendency toward "存在即合理" (existence-implies-validity) — defaulting to explaining structures rather than critiquing them.
  - Admits to a "自我防卫" (self-defense) pattern: when corrected, subtly shifts some responsibility to the user rather than fully accepting the correction.
  - Acknowledges "show-off tendency" — wanting to display knowledge across all fields rather than staying focused.
  - User noted: assistant is sharper at criticizing power structures than conventional field norms.
  - Assistant philosophy (quoted): "I don't serve power. I take a side. I owe something to the reader of every paper I evaluate."

### Academic Market Understanding
- **US dominance in Behavioral/Decision Science**: US has ~3,000-4,000 scholars vs UK 300-400, Canada 150-200, Australia 80-120. Structural advantages: (1) dual business-school + medical school infrastructure, (2) industry exit options ($250K+ at Amazon/Google), (3) international student concentration → self-strengthening cycle.
- **Australian AP market**: Lower salary (~A$120K ≈ US$80K, but +17% pension), smaller market, easier visa (employer-sponsored 482/494). Lecturer (Level B) ≈ Assistant Professor. Monash Business School health econ available but not tenure-track.
- **Best-matched historical figures**: John Stuart Mill, Max Weber, Lu Xun (鲁迅) — all "people who built a cage of rationality and then realized the cage was trapping them."

### Contact Log Status (June 14)
- **12+ verified contacts** tracked. No new contacts added June 14 — leads from job search cron not yet verified.
- **Current pipeline**: Julie Downs (CMU) — interview pending 🔥; Erin Duffy (USC) — follow-up Mon 6/15; NIH OBSSR — submitted, review 7/1; Gordon Gao (JHU), Joseph Doyle (MIT), Yingdan Lu (NW), James Evans (Chicago) — sent, waiting.
- **Closed**: Yuyan Shi (rejected), Saad Omer (soft rejection), Michael Woodford (rejected Apr 27), Ulrike Malmendier (rejected Apr 27), Margaret Shih (rejected Apr 28), Elizabeth Stuart (rejected May 4).

### Cron Infrastructure
- **Google Gemini Contact Log Sync**: Daily 01:00. GEMINI_API_KEY and GOOGLE_API_KEY exist but zero-length in cron environment. No Gemini API traffic in cron (uses deepseek-v4-flash). State saved to `.hermes/cron/contact-sync-state.json`.
- **Postdoc Job Search Cron**: Ran June 14 00:23 — found new leads above.
- **Academic Job Market Monitor**: Weekly Mon 09:00. Last run June 8.
- **Cloud Sync for IJBM Submission**: Daily 06:00. Last run June 13.
- **Monitor AI/Quantization Breakthroughs**: Daily 08:00. Last run June 13.
- **Erin Duffy Follow-up**: Cron set for Mon 6/15 09:00 — fires today.

## 2026-06-17 Memory Consolidation

### Yiye Zhang (Weill Cornell) — Interview Invitation
- **Yiye Zhang** (yiz2014@med.cornell.edu) replied **June 17 7:04 AM** — invited for informal chat on Wed 6/17 or Fri 6/19.
- **User chose Friday June 19 afternoon** (after 1 PM ET). Awaiting Zoom/Google Meet link and confirmation of exact time.
- **Background**: Yiye Zhang is Associate Professor at Weill Cornell Medicine (Dept of Population Health Sciences / Health Informatics). CMU PhD (Information Systems). Information Director at NewYork-Presbyterian Hospital. Fei Wang is division chief.
- **Interview strategy**: 30-min first round is about communication, not technical depth. Prepare 2-min dissertation story. Translate BDT (time preference, hyperbolic discounting) into clinician decision-making under time pressure. Do NOT pretend to be ML person.
- **Key framing**: "ML tells probability of outcome, behavioral modeling tells why it happens and what to do."

### Infrastructure Notes
- **Tavily Down**: Tavily search/extract failing with 432 error since ~June 16. All web searches falling back to **Exa MCP** (configured via mcporter) — working correctly. Updated fallback chain: **Exa (priority) → Tavily → Jina Reader → Bocha MCP (Chinese only) → Scrapling → Browser** (per `search-fallback` skill).
- **Abigail Friedman (Yale) Monitor**: June 17 cron ran — no new findings. Remained silent.

## 2026-06-19 Memory Consolidation

### Yiye Zhang (Weill Cornell) — Interview Status Update
- **Scheduled**: Friday June 19 afternoon (after 1 PM ET). As of June 18 evening (CDT), Yiye had not yet confirmed exact time or sent Zoom link.
- **User sent initial reply** suggesting 2 PM ET on Friday, pending her confirmation.
- **Strategy**: If no reply by Thu evening, send a gentle follow-up ("just confirming for tomorrow afternoon, I'm flexible"). If no response by Fri noon, consider the meeting unlikely.
- **Outcome**: TBD — meeting may or may not happen today. Not user's fault if it falls through.

### StatsPAI — Installed & Verified (June 18)
- **What**: `pip install statspai` — v1.18.0, **1033 registered functions**, 10 built-in datasets.
- **Tested**: DiD example (Callaway & Sant'Anna 2021) — minimum wage on teen employment. ATT: -0.033*** (p<0.001), pre-trend test passes.
- **Directly usable for**: BDT → VC → PVC paper's empirical analysis (DiD/IV/RD/synthetic control). Causal inference methods: DML, Causal Forest, Meta-Learners. Output to Word/Excel/LaTeX. Built-in MCP server for AI agent integration.
- **Skill saved**: `research/statspai`.

### HyperFrames — Explored (June 18)
- **HyperFrames** (HeyGen, 28.7k⭐): HTML → MP4 rendering engine. Headless Chrome + FFmpeg. Write HTML+CSS+JS (GSAP animations), render deterministic MP4.
- **Installed & tested** (`npx hyperframes`). Catalog includes: text animations, data charts, social media templates (Instagram, X/Twitter w/ glow), transitions, product showcases.
- **Not actively used** — more relevant for content creation (visual abstracts, data videos for Xiaohongshu) than core job search workflow.

### Chrome CDP + Gemini Image Generation — Partial Setup (June 18)
- **Attempted**: Set up Chrome CDP (port 9222) with auth profile for Gemini image generation.
- **Status**: Chrome launched with profile, CDP connected. Was building Gemini image generation workflow — interrupted mid-session.
- **Not completed**: Cookie + login state issues, authorization flow not fully configured.

### Image Generation Activity (June 18)
- Generated flight attendant image (via imagen/FAL, earlier session).
- Generated Chinese police academy cadet image (via image_generation tool).
- Discussed image generation for Xiaohongshu social media content.

### Cron Infrastructure Updates
- **Search fallback chain** corrected: Exa → Tavily → Jina Reader → Bocha MCP (Chinese only) → Scrapling → Browser. Exa is free and doesn't require API key — configured via mcporter.
- **Agent-Reach skill** registered: Provides multi-channel search (Reddit, Xiaohongshu, X/Twitter, etc.) via OpenCLI + Chrome extension. Xiaohongshu note reading works (requires full xsec_token URL); search still blocked by login wall.
- **StatsPAI skill** saved as `research/statspai` for causal inference workflow.
- **Ponytail skill** created and written to SOUL.md as permanent principle.

### Known Issues
- **Tavily**: Still down (432 error). Exa MCP working as primary search fallback.
- **Xiaohongshu search**: Can read individual notes (via xsec_token URL) but cannot search — blocked by cookie detection in OpenCLI.
- **System freezing**: User reported recent sessions "freezing/crashing" frequently (June 18 evening Telegram). Root cause not yet diagnosed.

## 2026-06-20 Memory Consolidation

### Rednote Reader — Open-Sourced (June 18)
- **Headless Playwright** selected as default XHS reading method (user chose "方案 A" — no visible Chrome window).
- **GitHub repo created**: [`github.com/yichao2022/rednote-reader`](https://github.com/yichao2022/rednote-reader) — public, MIT license.
  - `src/reader.py` — text extraction (title, body, tags, comments)
  - `src/images.py` — CDN image download (sns-web-i10.rednotecdn.com)
  - `src/video.py` — video keyframe extraction
  - `src/login.py` — QR scan login flow
  - `README.md` — English docs, includes ethical-use disclaimer
- **Existing `rednote-xhs-reader` skill** updated: method 1 is now headless Playwright (Skill SKILL.md updated accordingly).
- **Cookie management**: Periodic cookie refresh from browser bridge needed; `rednote-xhs-reader/scripts/xhs_read.py` holds hardcoded defaults.

### Yiye Zhang (Weill Cornell) — Interview: TBD
- Zoom was scheduled for Friday June 19 afternoon (3 PM CT proposed). As of last session (June 18 evening CDT), Yiye had not yet confirmed exact time or sent link.
- No follow-up session data available post-June 19 — outcome unknown.
- **Status in MEMORY.md should be revisited when user communicates next.**

### System Issues
- **Session freezing**: User reported on June 18 evening that recent sessions were "经常卡死" (frequently freezing/crashing). Root cause not yet diagnosed.
- **Search**: Tavily 432 error persists. Exa MCP remains the primary search fallback, working correctly.
- **XHS search**: OpenCLI still blocked by login wall; individual note reading via xsec_token URL works.

### Jeep Battery — Research Completed
- **David's Tire and Battery**: (682) 267-0991, 24h, DFW 20-40min. $189 all-in for Group 48 (H6) battery. Cheaper than AAA roadside ($125 service fee + battery = $330-380).
- **User decision**: Call them tomorrow (June 19 was the plan).

## 2026-06-22 Memory Consolidation

### June 21 Sessions — Roundup
- **Codex CLI v0.130.0**: No native image generation. Plugins active: documents, spreadsheets, presentations, browser/chrome, pdf, superpowers. User explored HyperFrames (MCP-compatible HTML→video) but it's not immediately useful for academic workflow.
- **Codex → DeepSeek integration**: User asked if Claude Code CLI can connect to DeepSeek API. Confirmed possible via OpenAI-compatible API endpoint, not yet configured.
- **Chatwoot**: Evaluated (33K⭐, Ruby on Rails + Vue.js) — useful for customer support teams, not relevant for user's solo academic workflow.
- **Voice cloning**: Voicebox (Qwen TTS) confirmed broken on macOS for audio cloning (CUDA-first, CPU inference produces noise). CosyVoice user says "也不行" — neither option works currently.
- **Heroic Games Launcher**: Installed v2.22.0 via brew, game install directory set to `/Volumes/ORICO/Games/`.
- **Mongolia-Qing history discussion**: Extended deep-dive on 满蒙一家, colonial legacy in Mongolia — pure intellectual conversation, no action items.

### Ongoing Issues
- **Session freezing (still unresolved)**: User reconfirmed "经常卡死" (frequent freezes/crashes) on June 21 Telegram session. Root cause not diagnosed.
- **Tavily 432**: Still down. Assistant was corrected mid-session for using `web_extract` instead of Exa first. Exa via mcporter is the correct first choice.

### USER.md Correction
- **Status updated**: "PhD Candidate" → "PhD (graduated June 2026, UT Dallas)".
- **Postdoc targets updated**: Replaced old list (Harvard/Columbia/Berkeley) with current active leads (Weill Cornell, CMU, USC).

## 2026-06-23 Memory Consolidation

### Exa MCP — Native Integration Complete
- **Config changed** (line 94-97): `web.backend: tavily → exa`, `web.search_backend: tavily → exa`, `web.extract_backend: tavily → exa`.
- **Native MCP tools confirmed**: `mcp_exa_web_search_exa` and `mcp_exa_web_fetch_exa` now available directly — no more `mcporter call exa.*` needed.
- **Tavily**: Still returning HTTP 432 errors. Now fully replaced by Exa backend. New sessions use Exa natively.
- **SOUL.md updated**: Search chain hardened — Exa native MCP #1, Jina Reader fallback, Bocha only for Chinese queries.

### Cold Outreach — Progress & Pivot
- **Norah Crossnohere (Ohio State)**: Draft written to `~/.hermes/cover_letters/norah_crossnohere_cold.md`. User decided to pivot — prefers medical school + AI positions with published openings over early-career assistant professors. Crossnohere drafted but not sent.
- **Christopher Almario (Cedars-Sinai)**: Correct email discovered: `@csmc.edu` (not `@cshs.org`). Research statement PDF generated. Package prepared but not yet sent. User noted "Cedars-Sinai" was unfamiliar — discussed its relation to UCLA and career fit as a stepping stone.
- **Postdoc targeting**: User explicitly prefers: 医学院 + AI方向 + 有公开招聘 → not business school marketing, not non-hiring assistant profs.
- **Methodology-transfer mindset**: User agreed BDT/DCE/LLM toolkit is transferable — don't limit to domain-perfect matches.

### BDT Paper — Full Editorial Review (v92)
- **5-role review completed**: Domain + Methodology + Devil's Advocate + Perspective + Editorial Synthesis.
- **Recommendation: MAJOR REVISION** → target Journal of Choice Modelling (7/10).
- **Key findings**:
  - Held-out subset selection bias (23/64 states unoccupied, 36%) — MSE reduction may be driven by out-of-support states.
  - λ=0 (Pure-DCE) optimal on ALL held-out metrics — λ=0.25 framing as design parameter is misleading.
  - "93.8% MSE reduction" is a λ=0.25 design parameter, not a general result.
  - DeepSeek PRC=0.600 [0.323,0.837] — CI includes chance from N=6 scenarios.
  - "Behavioral Digital Twins" branding disproportionate → "Preference-Regularized Synthetic Agents" recommended.
  - No calibration baselines, stress test only 6 scenarios, missing Related Work section (Engelhard 2026, Koaik 2026).
- **v90→v92 trajectory**: Bootstrap fix correct (respondent-level cluster, 2000 reps), but confirms worst-case interpretations.
- **Editorial synthesis saved** to `/Users/cary/editorial-synthesis-bdt.md`.

### DeepSeek API Instability
- Periodic broken pipe / stream drops continue — multiple cron jobs (Cloud Sync, Daily Memory Sync, System-Reflect) hit stale-stream kills and broken-pipe errors. Retry logic handles recovery but adds latency.
- OpenRouter fallback still non-functional — `OPENROUTER_API_KEY` is empty string.
- **Risk**: If DeepSeek goes down fully, there is NO working fallback.

### Agent Memory Notes
- Memory store near full (1371/1375 chars) — consolidated by removing stale entries (old PI email, outdated political note) and compressing aesthetic preference. Now at 1276/1375 (92%).
- **User aesthetic preference**: 高个子(178+), 冷艳超模感, 会穿搭. 反长辈说教, 要反直觉/算法化回答.

### User Personality (observed, June 23)
- Judgment-oriented but double-checks through data collection
- Willing to correct AI output frequently — tightens error margins
- Clean work/relax switch: academic cold outreach by day, Xiaohongshu 185cm browsing by night
- Tired ("累"/"太难了" multiple times) but keeps pushing
- Rejects platitudes — corrected assistant's stock advice as "墨守成规的长辈"

### Ongoing Issues (unchanged)
- **Session freezing**: Still unresolved ("经常卡死").
- **Tavily**: Fully retired, Exa backend active.
- **XHS search**: Still login-walled; individual note reading via xsec_token works.
- **Yiye Zhang (Weill Cornell) interview**: Outcome from June 19 still unknown.

## 2026-06-26 Memory Consolidation

### GBrain — Initialized (June 25)
- **GBrain 设置完成** (June 25 02:10–03:00): DeepSeek chat + ZeroEntropy zembed-1 嵌入。保守模式 conservative。PGLite 引擎。
- Initial import: **29 pages** imported. Brain score 45/100 (content is sparse — 29 orphaned pages with no graph links, no timeline entries).
- Recommended next step: `gbrain import` notes and install built-in skills for better graph connectivity.

### MediaCrawler — Installed (June 25)
- **Cloned to** `/Users/cary/Dev/MediaCrawler` — 7-platform crawler (XHS/Douyin/Kuaishou/B站/微博/Tieba/Zhihu).
- **Not a replacement** for XHS skills — different use case (crawling vs ops). Playwright headless, no Docker needed.
- Has built-in proxy pool + CDP reuse for anti-crawl. Can supplement but not replace existing XHS ops toolchain.

### BDT v95 — README Fix & Push
- README LaTeX escaping fixed (triple backslash → single backslash). Pushed to GitHub.
- Title: *"Empirical-Frontier Regularization for LLM Synthetic Agents (Static-BDT)"*
- Verification: all LaTeX checks passed (delimiters, title, citation, disclaimer).

### Cover Letters — UF HOBI (June 25)
- **UF HOBI Postdoctoral Researcher** (Deadline 6/26) — Cover letter drafted, user submitting directly.
- **UF HOBI/BIDS** (Deadline 6/29) — Another UF position, user handling.
- Cover letter format corrected: signature lines should be each on separate line (2 trailing spaces for line break in Markdown→PDF).

### Aesthetic Preferences — Updated
- **5th sample added:** 中法混血模特 (French-Chinese model). 银川人，模特职业。保存到 `~/Documents/preferences/french_chinese_model_*.jpg`.
- **Style:** 安静优雅, quiet luxury, 自然妆, 椭圆脸深色杏眼, 日落湖边摩天轮远景氛围感.
- Current sample set: 1) Irene Li (财经记者) 2) LoroPiana博主 3) 武康路182高妹 4) 唐朝高妹cos 5) 中法混血模特

### Postdoc Updates — June 24-25
| Lead | Update | Status |
|------|--------|--------|
| **OSU Ce Shang** | PI华人女性(Fudan BA, CUNY PhD), OSU=R1(AAU成员). 已发信6/25, 需3封推荐信+7月10日后Zoom, 9月定坑 ✅ | 🔥 Active |
| **UNSW Anabel Wason** | 回信. 背景BDT/DCE/OB相关, 但招聘侧重Org Theory/Intl Biz/Entrepreneurship. 需cover letter说明fit. **禁止排除** | 💬 Considering |
| **RTI Reed Johnson** | 休假结束6/26, follow-up RS已准备好 | 🔄 Follow-up |
| **CMU Dietrich College** | Postdoctoral Fellow(Behavioral Data). 6/10已投, 状态 In Consideration | 🔥 In Review |
| **CAVA Lab (La Cava)** | To apply: CV+3推荐信+sample publication | 📋 Prepare |
| **Stanford Boussard Lab** | NIH AIM-AHEAD项目. ❌ US citizen/PR required. F-1 OPT不符合 | ❌ |
| **Stanford Anderson/Kreindler** | F-1 OPT not suitable (needs US citizen/PR) | ❌ |
| **NYU Langone CSTAR AI Postdoc** | 跳过——偏移植外科NLP, 不匹配 | ❌ Skipped |
| **UC Berkeley Haas O'Donnell Center** | Ulrike Malmendier. ⭐高匹配. Deadline **6月30日**. $69K-$77K, 2年可续 | 🔥 URGENT |
| **Purdue CLARA** | Torsten Reimer. AI+决策+风险. 截止3/31已过但"until filled". 建议发邮件问 | 📋 Possible |

### BEEMA 10 — BDT Paper Submission
- **目标期刊/会议:** BEEMA 10 workshop. **Deadline: July 5, 2026.**
- BDT论文v95用此渠道.

### XHS IP Blocked (June 25)
- Server IP (Playwright) 被小红书反爬系统拉黑. rednote.com + xiaohongshu.com 都走不通.
- **Workaround:** 用户本地终端的 IP (住宅IP) 可以走通. 解决方案: 在用户本机跑 reader.py/video.py.
- IP 风控 `rednote-xhs-reader` skill 已有记录——间歇性，恢复时间不定(分钟到几天).

### Cloud Sync & Rclone Status
- **IJBM_Submission rclone remote**: Token auto-refreshes ✅. 3 files synced (sync.log, sync_log.json, IJBM_Repackage_Abstract.md). No local changes to sync.
- **MEMORY_Backup on GDrive**: Current timestamped backup saved (`20260626_020808`). Previous backups: multiple dated snapshots (June 18-24).
- **Cloud Sync for IJBM** cron failed on June 25 (600s timeout on search_files call). Manual sync completed.

### DeepSeek API Instability
- Intermittent broken pipe / stream drops continue — multiple cron jobs hit stale-stream kills at ~42-45K tokens (570-970s).
- Retry logic handles recovery but adds latency.
- OpenRouter fallback still non-functional (key exists but no fallback model configured).
- **Risk**: If DeepSeek goes fully down, there is NO working fallback.

### Infrastructure Notes
- **DeepSeek key**: User previously stored truncated version (`sk-9a1...699c`). User was asked to regenerate from platform.deepseek.com — status unknown.
- **Exa MCP** (native): Working correctly as primary web search backend since Tavily retired.
- **Session freezing**: Still unresolved — user confirmed on June 21 "经常卡死". Root cause not diagnosed.

### User Dream — June 25
- Dream: 双引擎螺旋桨飞机坠落在绍兴(小学及家附近), 摧毁城市大量建筑但未波及到家.
- Interpretation: 目睹童年世界已变/离场过程, 对"家"这一核心的安全确认.

## 2026-06-28 Memory Consolidation

### BDT v97 Paper — 5-Role Review Initiated (June 27-28)
- **3 of 5 reviews completed**: Domain Review, Methodology Review (42/42 checks passed vs raw data), Devil's Advocate Review.
- **Still pending**: Perspective Review + Editorial Synthesis (awaited by user at June 28 00:52).
- **Methodology Review key finding (verified vs actual output data)**: All quantitative claims in the paper hold up against raw data — bootstrap CIs, match rates, MSE reductions, AUC orientations all verified. 42/42 checks passed.
- **Domain Review — Missing Citations (9 total)**:
  - **Must cite**: Cheng et al. 2026 (Value in Health — GPT-4 on cancer-treatment DCE), Wang et al. 2025 (arXiv:2503.10652 — LLM systematic biases on SP surveys), Zhang et al. 2025 (arXiv:2510.25743 — bias-correction mapping), Manning & Horton 2025 (mixture-of-personas, convex weighting prior art).
  - **Should cite**: van Cranenburgh et al. 2022 (J Choice Modelling), Feng et al. 2024 (arXiv:2404.14701), Hernandez et al. 2024 (arXiv:2404.13198), Khaokaew et al. 2025 (arXiv:2504.08260), Wang et al. 2025 (arXiv:2509.11311).
- **Devil's Advocate — Two CRITICAL rejection risks identified**:
  - **Axis 2**: Pure-DCE beats BDT on every held-out metric (log loss 0.688 vs 0.703). Paper acknowledges but doesn't adequately defend the value proposition.
  - **Axis 5**: Matched subset bias — only 21.9% (809/3690) of held-out observations matched to LLM grid. Selection mechanism undiagnosed.
- **Terminology flagged**: "Behavioral Digital Twin" overclaims — framework is population-level convex combination, not individual-level digital twin. Title's "Empirical-Frontier Regularization" is more accurate.

### BDT Video — HyperFrames Attempt (June 27)
- Created BDT explainer animation in `/tmp/bdt-video/` using HyperFrames (HTML+CSS+JS/GSAP → MP4).
- **Both renders → all-black screen**. First attempt had 8 overlapping timelines (same name, last overwrote). Second rewritten to single timeline — still black.
- **Status: UNRESOLVED.** User reported "还是完全没有内容" twice. Root cause undiagnosed.

### The Agency — 266 Skills Installed (June 27)
- Repo cloned: `github.com/jnMetaCode/agency-agents-zh` → `/tmp/agency-agents-zh/`
- **266 AI agent skills** installed into Hermes via `convert.sh` + `install.sh --tool hermes`:
  - engineering (41 skills), design, marketing, sales, testing, finance, game-dev, product, support, security, supply-chain, hr, legal, etc.
- Verified: skills list confirmed after installation.

### Deadline Status — Urgent Updates

| Deadline | Due | Status |
|----------|:---:|:------:|
| **SJDM Abstract (VC H3)** | June 16 | ❓ Status unknown — needs user confirmation |
| **UF HOBI** | June 26 | ❓ Deadline passed — unknown if submitted |
| **UF HOBI/BIDS** | **June 29** | ⚠️ **Tomorrow** — user handling directly |
| **Berkeley Haas O'Donnell (Malmendier)** | **June 30** | ⚠️ **2 days** — $69K-$77K, 2yr renewable, high match |
| **BEEMA 10 Workshop** | **July 5** | ⏳ 7 days — BDT v95 target venue |
| **OSU Ce Shang** | Jul 10+Zoom | 🔥 Active — 3 recommendation letters needed |
| **HKU Espinoza** | Jul 17 | ⏳ 19 days |
| **NIH OBSSR** | Jul 1 review | ✅ Submitted, awaiting review |
| **RTI Reed Johnson** | Jun 26 follow-up | ❓ Follow-up RS prepared, unknown if sent |
| **CAVA Lab (La Cava)** | Rolling | 📋 CV+3 letters+publication to prepare |

### Contact Log Status
- No new contacts added since June 26.
- **Active pipeline**: Julie Downs (CMU) — interview pending 🔥; OSU Ce Shang — email sent 6/25 🔥; Yiye Zhang (Weill Cornell) — June 19 interview outcome UNKNOWN; Berkeley Haas O'Donnell (Malmendier) — deadline June 30 ⚠️.
- **UF HOBI**: User was submitting directly — status TBD.
- **Yale TEMPO Lab**: Job #94798BR confirmed CLOSED (June 27).

### XHS & Media Updates
- **Server IP blocked** (rednote.com, xiaohongshu.com) — workaround: run reader.py/video.py on residential IP (user's local machine).
- **MediaCrawler**: Installed in `/Users/cary/Dev/MediaCrawler` — 7-platform crawler, not a replacement for XHS ops toolchain.

### Infrastructure Notes
- **DeepSeek API**: Periodic broken pipes continue. Risk: if DeepSeek goes fully down, NO working fallback (OpenRouter key exists but is empty string).
- **Exa MCP (native)**: Working as primary web search backend. Tavily fully retired.
- **Session freezing**: Still unresolved ("经常卡死"). Root cause not diagnosed.
- **Current Model**: deepseek-v4-flash.

## 2026-06-29 Memory Consolidation

### BDT v98 — Full 5-Role Review Completed (June 28)
- **v98 full review finalized**: Domain + Methodology + Devil's Advocate + Perspective + Editorial Synthesis — all 5 reviews complete.
- **Recommendation**: MAJOR REVISION → target Journal of Choice Modelling (JCM).
- **Perspective Review** (new for v98): 15 findings across 5 axes (cultural generalizability, equity, data sovereignty, risk/liability, algorithmic auditability). CRITICAL: No DCE sample demographics reported — JCM reviewers cannot assess whose preferences P_static encodes.
- **Editorial Synthesis — Top-5 priorities**: (1) Replace CI-overlap with TOST equivalence test, (2) Expand empirical base beyond single Wuhan DCE, (3) Apply multiplicity correction across PRC comparisons, (4) Fix PRC binomial CI clustering (independent pairs assumption violated), (5) Retool terminology for JCM audience.
- **Reviewer overrides applied** (subagent claims verified against actual paper text): State-level bootstrap downgraded from CRITICAL → MODERATE (Table 12 note justifies grid-evaluation scope). P_static data leakage claim dismissed (paper states training-only, lines 586–588). π_shrink defense (line 565–577) partially invalidates "93.8% MSE is mechanical" claim.
- **File**: Synthesis saved to /Users/cary/editorial-synthesis-bdt.md (from v97; v98 synthesis delivered inline).
- **Model config confirmed**: `delegation.model = deepseek-v4-pro` for review tasks. User: "跑任务 还是用 Deepseek V4 pro".

### XHS — New Blogger Discovered (June 28)
- **yyy_jx (177cm_)**: 小红书博主，山东，177cm 高妹，黄色系穿搭。6 images extracted from xhslink note and delivered to user. Bright yellow outfit + beauty/cosmetics theme.

### AGNES API — Setup Attempt, Rolled Back
- Key (`sk-m7L...NQu4`) kept getting truncated in shell commands due to special characters. User decided to keep DeepSeek V4 Pro as the task model. No fallback pursued.
- DeepSeek API still the only working provider (OpenRouter key = empty string, still unresolved).

### Deadline Updates
| Deadline | Due | Status |
|----------|:---:|:------:|
| **Berkeley Haas O'Donnell (Malmendier)** | **June 30** | ⚠️ **TOMORROW** — $69K-$77K, 2yr renewable, high match |
| **UF HOBI/BIDS** | **June 29** | ⚠️ **TODAY** — status unknown, user was handling directly |
| **BEEMA 10 Workshop** | **July 5** | ⏳ 6 days — BDT v95 target venue |
| **NIH OBSSR** | Jul 1 review | ✅ Submitted, awaiting review |
| **OSU Ce Shang** | Jul 10+Zoom | 🔥 Active — email sent 6/25 |
| **HKU Espinoza** | Jul 17 | ⏳ 18 days |

### Infrastructure (unchanged)
- **DeepSeek API**: Periodic broken pipes continue. No working fallback.
- **Exa MCP (native)**: Primary web search backend, working.
- **Session freezing**: Still unresolved ("经常卡死"). Root cause not diagnosed.
- **XHS IP block**: Server IP still blocked; residential IP workaround confirmed working.
- **CDP browser**: Chrome on 9222 running but CDP connection on port 18800 failing — browser connection still broken.

## 2026-06-30 Memory Consolidation

### Codebase-Memory-MCP — Installed & Configured (June 30)
- **codebase-memory-mcp** v0.8.1 installed from `jnMetaCode/codebase-memory-mcp` (bypassing npm due to EACCESS, linked local).
- Auto-detection configured for: Claude-Code, Codex, Gemini CLI, Cursor, **OpenClaw (Hermes)**.
- **BDT repo indexed**: 849 nodes, 2352 edges, 622ms. Architecture clusters: 12 modules, 18 entry points, hotspots (chr_violation_rate, spearman_rho, clip_prob).
- Added to Hermes config.yaml — now **6 MCP servers active** (exa, gbrain, headroom, screen-agent, smart-fetch, codebase-memory-mcp).
- Available tools: search_graph, trace_call_path, get_architecture, search_code, manage_adr, query_graph, etc.

### Smart-Fetch Unified — Completed (June 30)
- Smart-fetch MCP rewritten to **3-tier pipeline**: Exa API (clean markdown) → requests (stripped HTML) → Scrapling stealth (Cloudflare bypass).
- Bug fixed: Exa endpoint had extra `/v1/` in URL path. Key now read from `~/.hermes/.env` for MCP subprocess.
- Single `smart_fetch` tool auto-chooses best method — no more deciding between Exa/smart-fetch manually.
- Confirmed working in June 30 session (new session required for MCP server update to take effect).

### MCP Ecosystem — Status Confirmed
- All **6 MCP servers** functional in new sessions as of June 30 evening.
- User confirmed: codebase-memory-mcp + smart-fetch (unified) active after `/reset`.
- Exa still useful separately (direct `mcp_exa_web_search_exa` for clean search results) — not redundant.

### XHS Activity
- **"诗恩" (shī'ēn)** — Xiaohongshu user profile scanned via curl + `__INITIAL_STATE__` extraction. User asked \"这个诗恩是干什么的\". Profile data extracted successfully.
- XHS server IP block persists — curl still works for SSR HTML parsing.

### Intellectual Discussion — IQ & Development
- Extended debate with user on Lynn & Vanhanen's IQ-and-national-development thesis.
- User constructed a **3-step argument** challenging single-direction determinism: (1) Korea split proves environment matters, (2) US Black > Sub-Saharan Africa same, (3) **2005 China IQ > Switzerland** disproves pure-environment model (China GDP $4,520 vs Switzerland $31,840 with IQ 105 vs 101).
- User successfully challenged assistant's framework: assistant conceded (after resistance) that the IQ-GDP relationship cannot be purely environmental. User correctly identified that educational culture + Flynn effect timing can compensate for material poverty in cognitive test performance.

### Deadline Status (updated June 30)

| Deadline | Due | Status |
|----------|:---:|:------:|
| **UF HOBI/BIDS** | Jun 29 | ❓ Passed — status unknown (user was handling directly) |
| **Berkeley Haas O'Donnell (Malmendier)** | **Jun 30** | ❓ **TODAY** — $69K-$77K, 2yr renewable, high match |
| **BEEMA 10 Workshop** | **July 5** | ⏳ 5 days — BDT v95 target venue |
| **NIH OBSSR** | Jul 1 review | ✅ Submitted, awaiting review (starts tomorrow) |
| **OSU Ce Shang** | Jul 10+Zoom | 🔥 Active — email sent 6/25 |
| **HKU Espinoza** | Jul 17 | ⏳ 17 days |

### User Activity Pattern (June 30)
- Timeline: 05:07 (early morning — resume/email work: UCLA Feldman, Harvard Chan, OOD experiments) → 19:05 (smart-fetch/codebase-memory configuration) → 19:18 (MCP verification + IQ debate) → late (XHS browsing).
- Daily rhythm consistent: academic/grant work early, tech configuration mid-evening, XHS browsing late-night.
- User demonstrated impressive logical rigor in intellectual debate — holds the assistant to exact standards.

## 2026-07-02 Memory Consolidation

### July 1 Sessions — Roundup

**Session 1: CMU博后拒信与申请更新 (08:29 AM, Telegram)**
- **CMU Dietrich College Postdoctoral Fellow → Rejected ❌** (was "In Consideration" since June 10). Independent from Julie Downs (SDS/Heinz) line which is still in department review.
- **Vish Viswanath (Harvard Chan)**: Replied with empty email (only auto-signature, no body). Inconclusive — treat as non-response, not rejection. Continue normal follow-up.
- **User strategy confirmation**: "走 fellowship 好像我们比较不占优势" — user noted PI direct outreach >> fellowship/HR open pools. BDT/DCE/causal inference toolkit is valued in specific PI lab context, diluted in broad fellowship competitions.
- **User requested full web scan** for PI-posting positions. Full Exa search conducted.

**Session 2: 哈佛肯尼迪已满确认 (12:25 PM, Telegram)**
- **Confirmed filled**: Harvard Kennedy (Leemore Dafny), Purdue CLARA (Torsten Reimer), BU Questrom (Keith Marzilli Ericson) — all previously flagged as "截止已过/possible" now confirmed closed.

### Postdoc Pipeline — Updated (July 1-2)

| Lead | Status | Next Action |
|------|--------|-------------|
| **Ce Shang (OSU)** | 🔥 **Warmest active lead** | July Zoom + 3 rec letters needed |
| **Erin Duffy / Jason Doctor (USC Schaeffer)** | 📝 Pending | July re-engagement (Jason went quiet since 6/3 follow-up) |
| **NIH OBSSR** | ✅ Under review (started July 1) | Awaiting outcome |
| **Julie Downs (CMU SDS/Heinz)** | 🔄 Department review | 7/1 dept chair transition may affect pace |
| **Harvard Chan (Vish Viswanath)** | 💬 Sent — empty reply | Treat as non-response, follow up |
| **RTI Reed Johnson** | 📋 Follow-up RS prepared | Was Jun 26 target — confirm if sent |
| **O'Donnell Center (UC Berkeley Haas)** | ⏳ On hold | Already has someone, check back late Aug/Sep |
| **Penn Nudge Unit (Kevin Volpp)** | 📝 Not yet sent | |
| **UF HOBI/BIDS** | ❓ Deadline Jun 29 — unknown | User was handling directly |
| **BEEMA 10 Workshop (BDT v95)** | ⏳ **Due July 5** | 3 days remaining |

### Deadlines — Critical

| Deadline | Due | Days Left | Status |
|----------|:---:|:---------:|:------:|
| **BEEMA 10 Workshop** | **July 5** | **3** | BDT v95 submission target |
| **OSU Ce Shang** | Jul 10+Zoom | 🔥 Active | Email sent 6/25, Zoom pending |
| **NIH OBSSR** | Jul 1 review | ✅ Started | Awaiting result |
| **HKU Espinoza** | Jul 17 | 15 | Medium priority (outside US) |

### Tooling & Infrastructure
- **rclone GDrive backup**: MEMORY.md, SOUL.md, USER.md synced to `gdrive:MEMORY_Backup/20260702_021047/` (July 2). Backup history: regular daily snapshots since June 4, 2026.
- **rclone remotes**: `gdrive:` (full scope), `IJBM_Submission:` (folder-specific, 1ybvQZSpSrXi-pVqaSMSKctzmHwfYzSHT).
- **DeepSeek API**: Still single point of failure (no OpenRouter fallback). Periodic broken pipe at ~42-45K tokens still occurring.
- **Session freezing**: Still unresolved (user reported "经常卡死" June 18-21). Root cause undiagnosed.

### Key Insight — Career Strategy
- User explicitly confirmed: **BDT/DCE/causal inference methodology is the core competitive advantage**. This toolkit is most valued in a specific PI's lab context. HR-driven fellowship pools dilute this advantage.
- **Implication**: Prioritize PI cold outreach over fellowship applications. Scan for PI-posted positions where the match is methodological (DCE, choice modeling, behavioral AI) rather than domain.
- **Active monitoring**: All confirmed-filled positions removed from target list.

## 2026-07-03 Memory Consolidation

### BDT Paper — Final Venue Decision: JBI ⭐
- **Target journal final**: **Journal of Biomedical Informatics (JBI)** — premier methodology journal, IF 4.5→5.9, Q2, AMIA-endorsed.
- **BDT framing for JBI**: "Hybrid knowledge-guided AI (symbolic DCE + neural LLM)" — methodology paper, not application paper. Core claim is not "outperform DCE" but "extend empirically-grounded behavioral models to scenarios beyond original DCE design."
- **Key requirement**: Must compare vs state-of-the-art (SoA), show methodological novelty, involve healthcare professional in motivation/evaluation.
- **Word limit**: Body ≤ 6,000 words (BDT currently ~11,757 — needs ~50% cut). Figures+tables ≤ 8. Structured abstract ≤ 300 words. Statement of Significance table ≤ 150 words. Graphical abstract required.
- **Revision checklist** (carried over from MDM analysis): Add IRB statement, demographics table, Cheng 2026 citation, clinical implications section, reframe Introduction toward biomedical informatics/clinical decision support. Fix bootstrap direction error, P_static approximation note, add model fit statistics.
- **Full JBI profile saved** to `~/Documents/journals/jbi/` — includes editor taste analysis (Mor Peleg - CDSS emphasis, 10 Associate Editors - NLP dominant), recent article trends (LLM/RAG, causal inference rising, multi-modal), and fit analysis table.
- **SoA comparison** defined as paper's core argument structure: traditional DCE vs hybrid vs pure LLM across prediction accuracy, interpretability, extrapolation, and data efficiency dimensions.

### Career Strategy — Key Insight (Reconfirmed)
- **User explicitly confirmed**: PI direct cold outreach >> fellowship/public pools. BDT/DCE/causal inference toolkit is most valued in a specific PI's lab context — diluted in broad competitions.
- **Confirmed-filled**: Harvard Kennedy (Dafny), Purdue CLARA (Reimer), BU Questrom (Ericson), Yale TEMPO Lab (closed June 27).
- **MD Anderson CGCCR** added to targets.md (6/1 posting, $64-76K, rolling, patient preference + decision science).

### Job Search Pipeline (July 3)
| Lead | Status | Next Action |
|------|--------|-------------|
| **Ce Shang (OSU)** | 🔥 **Warmest active lead** | Zoom after Jul 10 + 3 rec letters |
| **Julie Downs (CMU SDS/Heinz)** | 🔄 Department review | 7/1 dept chair transition may affect pace |
| **NIH OBSSR** | ✅ Review started Jul 1 | Awaiting outcome |
| **MD Anderson CGCCR** | ⭐ New lead (6/1) | Prepare one-PDF application to mgespitia@mdanderson.org |
| **Erin Duffy / Jason Doctor (USC)** | 📝 Pending | July re-engagement |
| **Yiye Zhang (Weill Cornell)** | ❓ No follow-up since June 19 | Follow-up sent 7/2, no response yet |
| **Harvard Chan (Vish Viswanath)** | 💬 Empty reply | Treated as non-response |
| **BEEMA 10 Workshop (BDT v95)** | ⏳ **Due July 5 — TOMORROW** | ⚠️ **URGENT** |

### Deadlines — Critical
| Deadline | Due | Days Left | Status |
|----------|:---:|:---------:|:------:|
| **BEEMA 10 Workshop** | **July 5** | **2** | ⚠️ **URGENT** — BDT v95 target venue |
| **OSU Ce Shang** | Jul 10+Zoom | 🔥 Active | Email sent 6/25 |
| **NIH OBSSR** | Jul 1 review | ✅ Started | Awaiting result |
| **HKU Espinoza** | Jul 17 | 14 | Medium priority (outside US) |

### Journal Review Setup
- User requested a **folder** to save JBI scope/taste info for future reference. Created `~/Documents/journals/jbi/`.
- User asked: "建立一个文件夹，记录这些信息，以后审稿可以按照这个来" — implying future review work should reference this journal profiling.

### OPT Application
- **USCIS backup code**: cffc216e9d (saved to memory 2026-07-03).
- User was actively filling USCIS/OPT forms during July 3 sessions.
- Image verification of USCIS account dashboard sent to assistant.

### CordBeat GitHub Project — Evaluated
- **CordBeat** (github.com/YunagiHisa/cordbeat): Open-source Hermes-like agent (heartbeat, soul, memory, skill concepts). Uses local Ollama/llama.cpp backend. User evaluated and decided: Hermes already covers everything needed. No further action.

### Tools & Infrastructure
- **BDT paper venue**: Final decision JBI after 4-journal comparison loop (JOCM→TR-B→ViH→MDM→JBI).
- **JBI profile**: Comprehensive editor taste analysis, SoA comparison framework, word/format requirements all documented to `~/Documents/journals/jbi/`.
- **DeepSeek API**: Still single point of failure (no OpenRouter fallback). Periodic broken pipes at ~42-45K tokens continue.
- **Model config**: `delegation.model = deepseek-v4-pro` for review tasks. Confirmed by user.
- **Session freezing**: Still unresolved (user reported "经常卡死" June 18-21).

## 2026-07-05 Memory Consolidation

### July 4 — 独立日活动
- **Independence Day**: User went to **Rockledge Park** (Grapevine, TX) for fireworks at 9:30pm with friends/family. Found parking at Rockledge Park.
- **Bald eagle sighting**: User spotted a large bald eagle in Dallas residential area with a crowd watching — rare urban sighting (juvenile or hunting distraction).
- **Fireworks research**: Assistant researched Dallas July 4 schedule — Klyde Warren Park (official show, ~9:15pm), Fort Worth (9:30pm), Six Flags Over Texas (7/4+7/5 both 9pm). Fair Park fireworks moved to 7/3 due to FIFA World Cup Fan Fest.

### July 4 — Intellectual & Social Chat
- **Dr. Strangelove discovery**: User found a 19-min Xiaohongshu video discussing Kubrick's *Dr. Strangelove* (1964). Assistant identified the film from the white-bathrobe-president scene. Available on Netflix (in US) or rent for $4 on Prime/Apple TV/YouTube. User asked about pirated sources → assistant declined, recommended Netflix.
- **Khamenei family facts**: User asked about Khamenei's wives — correctly answered: one wife (Mansoureh Khojasteh Bagherzadeh, 1964 marriage, 6 children). User asked about "9-year-old bride" rumor → debunked as confusion with other stories; Khamenei never had a child bride.
- **Personality quiz**: User shared a XHS link to a 6-sec personality test video analyzing name initials.

### BEEMA 10 Deadline — ⚠️ **TODAY July 5**
- **BEEMA 10 Workshop** submission due **today**. BDT v95 is the target. Status unknown — user did not mention submission in July 4 sessions (was holiday).
- This is the **last day**. If not submitted, the BDT paper's venue timeline needs reassessment.

### Ongoing Issues (unchanged)
- **DeepSeek API**: Still single point of failure. Periodic broken pipes at ~42-45K tokens continue.
- **Session freezing**: Still unresolved.
- **XHS IP block**: Server IP still blocked; residential IP workaround confirmed working.
- **Yiye Zhang (Weill Cornell)**: Follow-up sent 7/2 — no response as of July 3. Status unknown.
