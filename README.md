<h1 align="center">Amaresh Hebbar</h1>

<p align="center">
  <b>Founding AI Engineer @ <a href="https://www.linkedin.com/company/impossible-ai/">Impossible AI</a> · Applied AI Engineer @ <a href="https://anacodicai.org/get-started">AnacodicAI Labs</a></b><br>
  <b>Agentic LLM Systems · Model Auditing · Post Training & Alignment · Multi Agent Infrastructure · Medical AI</b><br>
  I design, fine tune, audit, and ship production grade AI systems end to end.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/gvamaresh/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:hebbar.gvamaresh@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/company/impossible-ai/"><img src="https://img.shields.io/badge/Impossible%20AI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Impossible AI"></a>
  <a href="https://github.com/anacodicAI-labs"><img src="https://img.shields.io/badge/AnacodicAI%20Labs-181717?style=for-the-badge&logo=github&logoColor=white" alt="AnacodicAI Labs"></a>
  <a href="https://huggingface.co/AmareshHebbar"><img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logoColor=black" alt="Hugging Face"></a>
  <a href="https://pypi.org/project/modeldiffr/"><img src="https://img.shields.io/badge/PyPI-3775A9?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://wandb.ai/amareshhebbar-/axiomapper"><img src="https://img.shields.io/badge/Weights%20%26%20Biases-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black" alt="W&B"></a>
  <a href="https://leetcode.com/u/GVAmaresh/"><img src="https://img.shields.io/badge/LeetCode%201000%2B-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode"></a>
  <a href="https://orcid.org/0009-0007-5020-8618"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<hr>

### About

I build agentic AI systems: multi agent pipelines, LLM infrastructure, model auditing and interpretability tooling, on device inference, and domain fine tuning, and I take them all the way to production.

* **Founding AI Engineer at [Impossible AI](https://www.linkedin.com/company/impossible-ai/).** Building the on device LLM inference layer with cloud fallback routing for an [agentic AI fitness platform](https://humanovaminds.com/impossible-ai), keeping 80% of sessions fully offline at 45ms baseline latency.
* **Applied AI Engineer at [AnacodicAI Labs](https://anacodicai.org/get-started)** (founded at Boston University). Self volunteered on ClinicalSearch, a multi agent clinical evidence retrieval system for plastic and reconstructive surgery.
* **Open source author.** Shipped **[Modeldiffr](https://pypi.org/project/modeldiffr/)** to PyPI: audits exactly what changed between a base LLM and any fine tune, quant, merge, or edit, with paired deltas and 95% bootstrap confidence intervals. Also shipped **[TrueNorth](https://pypi.org/project/truenorth-framework/)** (LLM infrastructure engine, 1,258 tests, 8 provider routing, about 90% cost reduction), **[BitNarrow](https://pypi.org/project/bitnarrow/)** (zero training weight surgery on 4 bit LLMs), and **[GitGrounded](https://pypi.org/project/gitgrounded/)** (AI regression testing).
* **Upstream contributor.** Fixed a critical Transformers 5.5+ import crash in [unslothai/unsloth zoo (PR #897)](https://github.com/unslothai/unsloth-zoo/pull/897).
* **Fine tuning at scale.** Published a **[16 model medical AI suite](https://huggingface.co/collections/AmareshHebbar/medical-ai-fine-tuned-model-suite)** (Qwen2.5) covering ICD 10, CPT, DRG coding, SNOMED mapping, clinical NLP, PM JAY classification, and Hindi medical. Every model is trained with a **QLoRA → DoRA → ORPO → merge** pipeline on a real, paired SFT dataset ([also published](https://huggingface.co/collections/AmareshHebbar/axismapper-medical-ai-suite)).
* **Led and mentored a 10 person engineering team** across frontend, backend, and mobile, delivering two concurrent AI product lines.
* **Hackathons.** SANS FIND EVIL! (DFIR Automation) · Google Cloud Rapid Agent (GitLab Partner) · INDIA RUNS (Redrob AI × Hack2Skill, Data & AI) · BITSoM Vertex Builders Pitch Fest (Top 150 of 2,300, Software Automation AI Track).
* **Research grade rigor.** Published benchmarks (100% precision on SANS DFIR triage), open SFT datasets, statistically grounded model diffs, and [W&B tracked training runs](https://wandb.ai/amareshhebbar-/axiomapper).
* Based in Bengaluru, India · **Open to remote first AI engineering roles** (IST, comfortable with US and EU overlap).

<hr>

### Experience

| Role | Organisation | What I do |
|------|--------------|-----------|
| **Founding AI Engineer**<br>Mar 2025 to Present | [Impossible AI](https://www.linkedin.com/company/impossible-ai/) · [Website](https://humanovaminds.com/impossible-ai)<br>Bengaluru, India (Remote) | Building the on device LLM inference layer with cloud fallback routing for the Impossible AI agentic fitness platform, keeping 80% of sessions fully offline at 45ms baseline latency. Orchestrating 16 specialised fine tuned models behind a unified domain classification layer, running the Supabase backend at zero errors under peak load, and mentoring 10 engineering interns |
| **Applied AI Engineer (Research & Development)**<br>Aug 2026 to Present | [AnacodicAI Labs](https://anacodicai.org/get-started) (founded at Boston University, nonprofit) · [GitHub](https://github.com/anacodicAI-labs) · [Agentic Cookbook](https://github.com/anacodicAI-labs/anacodic-agentic-cookbook)<br>Self volunteered, contributing under project lead [Rashan Kaur](https://www.linkedin.com/in/rashan-kaur/) | ClinicalSearch: multi agent clinical evidence retrieval for plastic and reconstructive surgery. 4 specialised agents (Search, Medical Fact Checker, Synthesizer, Evaluator) on the AWS Strands Agents SDK, Pinecone hybrid search over 2.5M+ clinical abstracts, a FastAPI backend, and a Vite and TypeScript frontend. Built a fully local Ollama inference stack that cut query latency by 38%, a critique loop that lifted Top K recall by 22%, and benchmark suites for extraction quality and LLM provider comparison |

Featured on LinkedIn: [view post](https://lnkd.in/p/dp_jS7S2)

<hr>

### Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
</p>
<p>
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white">
  <img src="https://img.shields.io/badge/Strands%20Agents-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white">
  <img src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white">
  <img src="https://img.shields.io/badge/RAG-5A4FCF?style=flat-square">
  <img src="https://img.shields.io/badge/Pinecone-000000?style=flat-square">
  <img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square">
  <img src="https://img.shields.io/badge/Multi%20Agent-6C63FF?style=flat-square">
</p>
<p>
  <img src="https://img.shields.io/badge/QLoRA-FF6F00?style=flat-square">
  <img src="https://img.shields.io/badge/DoRA-FF8C00?style=flat-square">
  <img src="https://img.shields.io/badge/ORPO-E65100?style=flat-square">
  <img src="https://img.shields.io/badge/Representation%20Engineering-8B0000?style=flat-square">
  <img src="https://img.shields.io/badge/Model%20Diffing-2E7D32?style=flat-square">
  <img src="https://img.shields.io/badge/Unsloth-6B4FBB?style=flat-square">
  <img src="https://img.shields.io/badge/bitsandbytes-444444?style=flat-square">
</p>
<p>
  <img src="https://img.shields.io/badge/Anthropic%20Claude-D97757?style=flat-square&logo=anthropic&logoColor=white">
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white">
  <img src="https://img.shields.io/badge/vLLM-FF4B4B?style=flat-square">
  <img src="https://img.shields.io/badge/llama.cpp%20GGUF-333333?style=flat-square">
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat-square">
</p>
<p>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/PEFT-FFD21E?style=flat-square&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/TRL-FFD21E?style=flat-square&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/Weights%20%26%20Biases-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black">
</p>
<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white">
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white">
</p>
<p>
  <img src="https://img.shields.io/badge/React%20Native-61DAFB?style=flat-square&logo=react&logoColor=black">
  <img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white">
  <img src="https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white">
</p>

<hr>

### Featured Projects

| Project | What it does | Stack | Highlights |
|---------|-------------|-------|-----------|
| **[Modeldiffr](https://github.com/amareshhebbar/modeldiffr)**<br>[PyPI](https://pypi.org/project/modeldiffr/) | Audits what changed between a base LLM and any fine tune, quant, merge, or edit. One command runs both models under identical conditions and reports what moved, by how much, and whether it beats evaluation noise | Python · PyTorch · Transformers | Flagship · paired deltas with 95% bootstrap CIs · token level KL divergence · CI gate mode · roadmap to crosscoder and causal diffing · [BitNarrow](https://github.com/amareshhebbar/bitnarrow) as layer 2 |
| **[BitNarrow](https://github.com/amareshhebbar/bitnarrow)**<br>[PyPI](https://pypi.org/project/bitnarrow/) · [Weights](https://huggingface.co/collections/AmareshHebbar/abliteration-weights) | Zero training, in place weight surgery on 4 bit quantized LLMs using Winsorized activation profiling and Gram Schmidt orthogonal projection across the residual stream | Python · PyTorch · bitsandbytes · Unsloth | Full spectrum projection across o, gate, up, down layers · 95th percentile outlier clamping · 386MB hot swap weight patch · 0% refusal with 100% logic retention · [Abliteration Weights collection](https://huggingface.co/collections/AmareshHebbar/abliteration-weights) |
| **[TrueNorth](https://github.com/amareshhebbar/TrueNorth)**<br>[PyPI](https://pypi.org/project/truenorth-framework/) | Developer first LLM infrastructure engine: declare the outcome in YAML, it owns the full multi turn conversation lifecycle through a 13 stage pipeline | Python · TS · Go · RN | 1,258 tests · 4 SDKs on PyPI + NPM · hallucination firewall (94%) · 8 provider routing · about 90% cost reduction |
| **[GitGrounded](https://github.com/amareshhebbar/gitgrounded)**<br>[PyPI](https://pypi.org/project/gitgrounded/) | Catches AI regressions before users do: diffs a prompt or model change, has an AI write targeted tests, judges old vs new, returns PASS, WARN, or FAIL | Python · Claude · Groq · Ollama · Streamlit | Git mode and live endpoint mode · version history per API · automatic PR comments · 22 tests in CI · BITSoM Vertex Builders Pitch Fest (Top 150 of 2,300) |
| **[Medical AI Suite](https://huggingface.co/collections/AmareshHebbar/medical-ai-fine-tuned-model-suite)**<br>[Datasets](https://huggingface.co/collections/AmareshHebbar/axismapper-medical-ai-suite) | 16 fine tuned Qwen2.5 specialist models for medical coding, billing and clinical NLP | QLoRA · DoRA · ORPO · Unsloth · HF | 13 published models + 16 open SFT datasets · <1% token hallucination · >99% structural format compliance · [live demo](https://huggingface.co/spaces/AmareshHebbar/icd10-coder-demo) · Apache 2.0 |
| **[LogPoseSIFT](https://github.com/amareshhebbar/logposesift)**<br>[Devpost](https://devpost.com/software/logpose-sift-autonomous-dfir) | Autonomous DFIR orchestrator: MCP server wraps 200+ SANS SIFT tools as typed Go endpoints | Go · Claude · Gemini · MCP · Volatility 3 | 100% precision · 92.8% recall · 0 hallucinations · SANS FIND EVIL! Hackathon · extended into [AllBlue](https://devpost.com/software/allblue) for Splunk |
| **[ShiftLeft](https://github.com/amareshhebbar/ShiftLeft)**<br>[Devpost](https://devpost.com/software/shiftleft) | Autonomous 5 agent bug fixing pipeline: reads repo → triages → generates fix → opens MR | Python · LangGraph · Gemini · GitLab MCP | End to end in about 60s, zero human steps · Google Cloud Rapid Agent Hackathon |
| **layerFourth** *(private repo)* | Fully local autonomous AI web agent: headed Chromium via raw CDP (no Playwright or Selenium), AI driven mouse and keyboard control, 4 layer extraction fallback (DOM → Accessibility Tree → Network sniff → Vision OCR) | Python · CDP · Vector DB | 134/134 tests passing across 12 build phases · dual layer vector memory (ephemeral + persistent) |

<details>
<summary><b>More projects</b></summary>
<br>

| Project | What it does | Stack | Highlights |
|---------|-------------|-------|-----------|
| **[HireSignal](https://github.com/amareshhebbar/hiresignal)**<br>[Live sandbox](https://huggingface.co/spaces/AmareshHebbar/hiresignal) | Ranks 100K candidates against a Senior AI Engineer JD in about 35s on CPU: multi signal scoring, honeypot detection, semantic embeddings | Python · sentence transformers · NumPy | No GPU, no API, no network during ranking · 85 honeypots caught · 10 tests · INDIA RUNS Hackathon |
| **[PocketLLM](https://github.com/amareshhebbar/PocketLLM)** | 100% offline Android AI chat running LLMs on device via a MediaPipe C++ bridge | React Native · Expo · MediaPipe C++ · AWS S3 | 9 open weight models (0.4 to 5.2 GB) · prompts never leave the device |
| **[raiseTicket / IssueLoop](https://github.com/amareshhebbar/raiseTicket)** | AI managed ticket queue for open source repos: test run failures become LLM triaged tickets, fix proposals, re tests, and escalations | Python · Supabase · Ollama | Local first embeddings and reasoning · pluggable provider config |
| **[OceanAI Website](https://github.com/amareshhebbar/oceanai_website)** | Investor grade 3D product site for the OceanAI health platform | Next.js · TypeScript | 65 files, 28 routes · live Claude API playground demos embedded |
| **[HatPet](https://github.com/amareshhebbar/hatpet)** | Custom Linux desktop pet: transparent, borderless, always on top window that wanders the screen in 8 directions, idles, and responds to drag | Godot 4 · GDScript | XWayland compatible movement (native Wayland blocks window repositioning) · built from scratch, no pet framework |

</details>

Fine tuned models live on **[Hugging Face](https://huggingface.co/AmareshHebbar)** · Packages on **PyPI** ([modeldiffr](https://pypi.org/project/modeldiffr/) · [truenorth-framework](https://pypi.org/project/truenorth-framework/) · [bitnarrow](https://pypi.org/project/bitnarrow/) · [gitgrounded](https://pypi.org/project/gitgrounded/)) · Training runs tracked on **[Weights & Biases](https://wandb.ai/amareshhebbar-/axiomapper)**

<hr>

### Open Source Contributions

| Repository | Contribution | Impact |
|-----------|--------------|--------|
| **[unslothai/unsloth zoo](https://github.com/unslothai/unsloth-zoo)** | [PR #897](https://github.com/unslothai/unsloth-zoo/pull/897): resolved a critical `ModuleNotFoundError` import crash | Restored runtime stability for LLM training workflows on Transformers 5.5+ |
| **[anacodicAI labs](https://github.com/anacodicAI-labs)** | ClinicalSearch multi agent retrieval, local Ollama inference stack, and the [Agentic Cookbook](https://github.com/anacodicAI-labs/anacodic-agentic-cookbook) | Nonprofit clinical AI research founded at Boston University |

<hr>

### Hugging Face: Medical AI Fine Tuned Model Suite

A suite of **Qwen2.5 specialist models**, one per clinical task. Each model is trained through a consistent **QLoRA → DoRA → ORPO → merge** pipeline (via [Unsloth](https://github.com/unslothai/unsloth) + TRL) on a **dedicated, published SFT dataset**, with no synthetic training data. Released under **Apache 2.0**; training tracked on [W&B](https://wandb.ai/amareshhebbar-/axiomapper).

> Collection: **[Medical AI Fine Tuned Model Suite](https://huggingface.co/collections/AmareshHebbar/medical-ai-fine-tuned-model-suite)** · Datasets: **[AxisMapper Medical AI Suite](https://huggingface.co/collections/AmareshHebbar/axismapper-medical-ai-suite)** · Code: **[AxisMapper](https://github.com/amareshhebbar/AxisMapper)**

| Model | Size | Task | Dataset (rows) | Method | GPU |
|-------|:----:|------|----------------|--------|-----|
| [icd10-coder-qwen25-7b](https://huggingface.co/AmareshHebbar/icd10-coder-qwen25-7b) | 7B | Clinical text → ICD 10 CM code + justification | [icd10-coder-sft](https://huggingface.co/datasets/AmareshHebbar/icd10-coder-sft) (74.7k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [icd10-coder-qwen25-7b-merged](https://huggingface.co/AmareshHebbar/icd10-coder-qwen25-7b-merged) | 8B | Merged full weights build of the ICD 10 coder (no adapter load) | [icd10-coder-sft](https://huggingface.co/datasets/AmareshHebbar/icd10-coder-sft) (74.7k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [snomed-mapper-qwen25-7b](https://huggingface.co/AmareshHebbar/snomed-mapper-qwen25-7b) | 7B | Clinical concept → SNOMED CT mapping | [snomed-mapper-sft](https://huggingface.co/datasets/AmareshHebbar/snomed-mapper-sft) (74.7k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [clinical-summarizer-qwen25-7b](https://huggingface.co/AmareshHebbar/clinical-summarizer-qwen25-7b) | 7B | Clinical note summarization | [clinical-summarizer-sft](https://huggingface.co/datasets/AmareshHebbar/clinical-summarizer-sft) (30k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [medical-billing-qwen25-3b](https://huggingface.co/AmareshHebbar/medical-billing-qwen25-3b) | 3B | Medical billing code generation | [medical-billing-sft](https://huggingface.co/datasets/AmareshHebbar/medical-billing-sft) (17k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [cpt-coder-qwen25-3b](https://huggingface.co/AmareshHebbar/cpt-coder-qwen25-3b) | 3B | Procedure text → CPT code | [cpt-coder-sft](https://huggingface.co/datasets/AmareshHebbar/cpt-coder-sft) (17k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [radiology-coder-qwen25-3b](https://huggingface.co/AmareshHebbar/radiology-coder-qwen25-3b) | 3B | Radiology report → diagnostic code | [radiology-coder-sft](https://huggingface.co/datasets/AmareshHebbar/radiology-coder-sft) (25.1k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [pmjay-classifier-qwen25-3b](https://huggingface.co/AmareshHebbar/pmjay-classifier-qwen25-3b) | 3B | India PM JAY scheme package classification | [pmjay-classifier-sft](https://huggingface.co/datasets/AmareshHebbar/pmjay-classifier-sft) (11.1k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [discharge-qa-qwen25-3b](https://huggingface.co/AmareshHebbar/discharge-qa-qwen25-3b) | 3B | QA over discharge summaries | [discharge-qa-sft](https://huggingface.co/datasets/AmareshHebbar/discharge-qa-sft) (30k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [medical-ner-qwen25-3b](https://huggingface.co/AmareshHebbar/medical-ner-qwen25-3b) | 3B | Clinical named entity recognition | [medical-ner-sft](https://huggingface.co/datasets/AmareshHebbar/medical-ner-sft) (16.7k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [hindi-medical-qwen25-3b](https://huggingface.co/AmareshHebbar/hindi-medical-qwen25-3b) | 3B | Hindi language medical assistant | [hindi-medical-sft](https://huggingface.co/datasets/AmareshHebbar/hindi-medical-sft) (19.7k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [icd10-to-drg-qwen25-1b](https://huggingface.co/AmareshHebbar/icd10-to-drg-qwen25-1b) | 1.5B | ICD 10 → DRG for reimbursement grouping | [icd10-to-drg-sft](https://huggingface.co/datasets/AmareshHebbar/icd10-to-drg-sft) (5.39k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [insurance-classifier-qwen25-1b](https://huggingface.co/AmareshHebbar/insurance-classifier-qwen25-1b) | 1.5B | CPT/HCPCS → Stark Law DHS classification | [insurance-classifier-sft](https://huggingface.co/datasets/AmareshHebbar/insurance-classifier-sft) (1.6k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [ayurveda-icd-qwen25-1b](https://huggingface.co/AmareshHebbar/ayurveda-icd-qwen25-1b) | 1.5B | Ayurveda term → ICD mapping | [ayurveda-icd-sft](https://huggingface.co/datasets/AmareshHebbar/ayurveda-icd-sft) (3k) | QLoRA → DoRA → ORPO → merge | A40 48GB |
| [pharmacy-ner-qwen25-1b](https://huggingface.co/AmareshHebbar/pharmacy-ner-qwen25-1b) | 1.5B | Pharmacy and drug entity recognition | [pharmacy-ner-sft](https://huggingface.co/datasets/AmareshHebbar/pharmacy-ner-sft) (3.5k) | QLoRA → DoRA → ORPO → merge | A40 48GB |

<sub>Pipeline (all models): Qwen2.5 Instruct base → <b>QLoRA</b> SFT (4 bit NF4, rank 16, α 32) → <b>DoRA</b> → <b>ORPO</b> preference alignment → adapter <b>merge</b>. Optimizer paged_adamw_8bit · cosine schedule, LR 0.0002 · trained on RunPod (NVIDIA A40 48GB) via Unsloth + TRL. Per model wall time ranges from about 0.4 h (1.5B configs) to about 1.9 h (7B configs). Training tracked at <a href="https://wandb.ai/amareshhebbar-/axiomapper">wandb.ai/amareshhebbar</a>. Datasets built from authoritative real world sources (for example CMS FY2026 ICD 10 CM and the HCPCS Stark Law DHS list), not LLM generated.</sub>

**Live demos (Spaces):** [icd10 coder demo](https://huggingface.co/spaces/AmareshHebbar/icd10-coder-demo) · [hiresignal](https://huggingface.co/spaces/AmareshHebbar/hiresignal)

<hr>

### Hackathons

| Submission | Hackathon | Track | What it does |
|-----------|-----------|-------|--------------|
| **[GitGrounded](https://github.com/amareshhebbar/gitgrounded)** · [PyPI](https://pypi.org/project/gitgrounded/) | BITSoM Vertex × H2S Builders Pitch Fest 2026 (Top 150 of 2,300) | Software Automation AI | Tests an AI app before and after a prompt or model change, AI written targeted tests, AI judge, PASS, WARN, or FAIL verdict |
| **[ShiftLeft](https://devpost.com/software/shiftleft)** · [Repo](https://github.com/amareshhebbar/ShiftLeft) | Google Cloud Rapid Agent | GitLab Partner | Label a GitLab issue → autonomous 5 agent pipeline reads the repo, triages the bug, writes the fix, and opens an MR in under 60 seconds |
| **[Poneglyphs: ShiftLeft](https://devpost.com/software/shiftleft-ml5aep)** | Google Cloud Rapid Agent | GitLab Partner | Label a GitLab issue `shiftleft` → 5 agent pipeline reads GitLab Orbit, triages, writes fix, opens MR |
| **[LogPoseSIFT](https://devpost.com/software/logpose-sift-autonomous-dfir)** · [Repo](https://github.com/amareshhebbar/logposesift) | SANS FIND EVIL! | DFIR Automation | Autonomous DFIR orchestrator: deploys an AI crew via strict MCP endpoints, runs SIFT diagnostics, triages and self corrects in seconds |
| **[AllBlue](https://devpost.com/software/allblue)** | SANS FIND EVIL! | DFIR Automation | Splunk alerts trigger autonomous AI forensic triage, with IOC findings pushed back as structured events. 100% precision, 0 hallucinations |
| **[HireSignal](https://github.com/amareshhebbar/hiresignal)** · [Live sandbox](https://huggingface.co/spaces/AmareshHebbar/hiresignal) | INDIA RUNS · Redrob AI × Hack2Skill | Data & AI Challenge | Ranks 100K candidates against a Senior AI Engineer JD in about 35s on CPU: multi signal scoring, 85 honeypots detected, per candidate reasoning |

<hr>

### GitHub Stats

<p align="center">
  <table>
    <tr>
      <td>

![GitHub Stats](https://github-stats-extended.vercel.app/api?username=amareshhebbar&rank_icon=github&show=reviews%2Cdiscussions_started%2Cdiscussions_answered%2Cprs_merged%2Cprs_merged_percentage%2Cprs_commented%2Cprs_reviewed%2Cissues_commented&show_icons=true&include_all_commits=true&theme=shadow_green)

      </td>
      <td>

![Top Languages](https://github-stats-extended.vercel.app/api/top-langs?username=amareshhebbar&layout=pie&langs_count=20&hide_values=true&theme=shadow_red)

      </td>
    </tr>
  </table>
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=amareshhebbar&theme=tokyonight&hide_border=true" alt="GitHub streak">
</p>

<hr>

### Activity

<p align="center">
  <img src="./assets/stats/month_summary.svg" alt="This month's commit summary">
</p>
<p align="center">
  <img src="./assets/stats/monthly_activity.svg" alt="Monthly commit and pull request activity">
</p>
<p align="center">
  <img src="./assets/stats/today_activity.svg" alt="Today vs yesterday commit and pull request activity">
</p>
<p align="center"><sub>Auto generated from live account data, refreshed every 6 hours · Last updated: <!--STATS-TIME-->2026-10-11 02:43 UTC<!--END--></sub></p>

<hr>

### Highlights

* Founding AI Engineer at **[Impossible AI](https://www.linkedin.com/company/impossible-ai/)** (Mar 2025 to Present)
* Applied AI Engineer on **ClinicalSearch** at **[AnacodicAI Labs](https://anacodicai.org/get-started)** (Aug 2026 to Present)
* Published **[Modeldiffr](https://pypi.org/project/modeldiffr/)**, **[TrueNorth](https://pypi.org/project/truenorth-framework/)**, **[BitNarrow](https://pypi.org/project/bitnarrow/)**, and **[GitGrounded](https://pypi.org/project/gitgrounded/)** to PyPI
* Upstream contribution to **[unslothai/unsloth zoo PR #897](https://github.com/unslothai/unsloth-zoo/pull/897)**
* Released a **[16 model medical AI suite](https://huggingface.co/collections/AmareshHebbar/medical-ai-fine-tuned-model-suite) + [16 open SFT datasets](https://huggingface.co/collections/AmareshHebbar/axismapper-medical-ai-suite)** on Hugging Face
* Released **[Abliteration Weights](https://huggingface.co/collections/AmareshHebbar/abliteration-weights)** produced by BitNarrow
* **1000+ problems solved** on [LeetCode](https://leetcode.com/u/GVAmaresh/)
* B.E. Computer Science & Engineering, Dayananda Sagar College of Engineering (2021 to 2025)

<hr>

<p align="center">
  <i>Open to remote first AI engineering roles: LLM infrastructure, agentic systems, model evaluation, fine tuning, or AI product engineering.</i><br>
  <a href="mailto:hebbar.gvamaresh@gmail.com">hebbar.gvamaresh@gmail.com</a> · <a href="https://www.linkedin.com/in/gvamaresh/">LinkedIn</a><br>
  <b>Let's build something intelligent.</b>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=amareshhebbar&style=flat-square&color=blue&base=0" alt="Profile views">
</p>
