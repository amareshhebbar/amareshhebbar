<div align="center">

# Amaresh Hebbar

**AI Infrastructure Engineer · Go · Python · LLM Systems**

*I work at the layer between the model and production — where things silently break.*

[![LeetCode](https://img.shields.io/badge/LeetCode-1100%2B_solved-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/u/GVAmaresh/)
[![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-AmareshHebbar-FFD21E?style=flat-square)](https://huggingface.co/AmareshHebbar)
[![W&B](https://img.shields.io/badge/W%26B-Public_Dashboards-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)](https://wandb.ai/amareshhebbar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/gvamaresh)

</div>

---

Not prompt engineering. Not wrappers.

I build the systems that sit underneath — GPU fault recovery, fine-tune version 
control, LoRA rank prediction, context memory hierarchies, inference routing, 
hallucination interception, model capability audits.

17 production tools. Each one exists because something broke and there was 
nothing to fix it.

**Training · Fine-Tuning · Inference · Agents · Edge**  
Go · Python · PyTorch · LangGraph · PEFT · QLoRA · Redis · VectorDB

---
---

## Open Source Projects

> Each project traces back to a single root cause: I needed the system to 
> not fail. Training, fine-tuning, inference, agents — if it ran in production, 
> I eventually had to instrument, patch, or rebuild it.


---

#### Distributed Compute & Telemetry

| Project | Type | What It Solves | Tech Stack |
| --- | --- | --- | --- |
| **[`outer-wall`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/outer-wall%5D(https://github.com/amareshhebbar/outer-wall))** | Runtime Infrastructure | Silent GPU faults kill overnight runs. This catches them in real-time, isolates the node, and auto-recovers. | Python · PyTorch · CUDA |
| **[`intent-lens`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/intent-lens%5D(https://github.com/amareshhebbar/intent-lens))** | Interpretability | Loss going down doesn't mean learning. Shows exactly which examples the model focuses on. | Python · PyTorch hooks · W&B |
| **[`truenorth`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/truenorth%5D(https://github.com/amareshhebbar/truenorth))** | Telemetry Pipeline | A highly reliable, immutable logging and telemetry pipeline to track absolute ground-truth states across distributed workflows. | Go · Time-Series DB |

#### Weights Engineering & Alignment

| Project | Type | What It Solves | Tech Stack |
| --- | --- | --- | --- |
| **[`lineage`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/lineage%5D(https://github.com/amareshhebbar/lineage))** | Fine-Tuning Ops | Version control for LoRA adapters—rollback, diff, and replay buffer auto-scheduling to prevent overwriting knowledge. | Python · PEFT · HuggingFace |
| **[`gearsecond`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/gearsecond%5D(https://github.com/amareshhebbar/gearsecond))** | Fine-Tuning Optimization | Runs 7B–13B models on 6–12GB by dynamically combining every memory trick to push hardware past natural limits. | Python · QLoRA · bitsandbytes |
| **[`signal-flare`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/signal-flare%5D(https://github.com/amareshhebbar/signal-flare))** | Training Diagnostics | 5-minute micro-probe that predicts optimal LoRA rank before committing to a full, expensive training run. | Python · PEFT · PyTorch |
| **[`wisteria`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/wisteria%5D(https://github.com/amareshhebbar/wisteria))** | Pre-Training Data Curation | Pre-training dataset scanner that filters out the 74% of web pages that are AI-generated to prevent model collapse. | Python · sentence-transformers |
| **[`first-form`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/first-form%5D(https://github.com/amareshhebbar/first-form))** | RLHF Training | A clean, unopinionated, model-agnostic GRPO trainer that isn't tied to deprecated APIs. | Python · PyTorch · trl |
| **[`coordinatemerge`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/coordinatemerge%5D(https://github.com/amareshhebbar/coordinatemerge))** | Model Merging | TIES/DARE/SLERP merge for LoRA adapters via SVD decomposition to combine multiple learned behaviors. | Python · PyTorch |

#### Autonomous Agents & Memory Architecture

| Project | Type | What It Solves | Tech Stack |
| --- | --- | --- | --- |
| **[`void-cache`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/void-cache%5D(https://github.com/amareshhebbar/void-cache))** | Agent Memory | L1/L2/L3 memory hierarchy with learned eviction scoring to prevent context degradation by turn 20. | Python · Redis · LangGraph |
| **[`hard-coat`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/hard-coat%5D(https://github.com/amareshhebbar/hard-coat))** | Inference Guardrails | Real-time semantic interceptor that deflects hallucinated values that would otherwise silently pass JSON validation. | Go · Python · sentence-transformers |
| **[`burn-rate`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/burn-rate%5D(https://github.com/amareshhebbar/burn-rate))** | Post-Training Eval | Pre/post audit that scores exactly how much of a model's general capabilities degrade during fine-tuning. | Python · lm-evaluation-harness |
| **[`shiftleft`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/shiftleft%5D(https://github.com/amareshhebbar/shiftleft))** | Agentic Framework | Autonomous bug-triaging and code-fixing system that maps the codebase to draft and test fixes before deployment. | LangGraph · Gemini |
| **[`logposesift`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/logposesift%5D(https://github.com/amareshhebbar/logposesift))** | Multi-Agent System | A multi-agent DFIR (Digital Forensics and Incident Response) crew for autonomous threat tracking and response. | Python · LangGraph |

#### Semantic Routing & Knowledge Engines

| Project | Type | What It Solves | Tech Stack |
| --- | --- | --- | --- |
| **[`axis-mapper`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/axis-mapper%5D(https://github.com/amareshhebbar/axis-mapper))** | Domain NLP / Routing | Traces scattered, messy, conversational patient symptoms directly to a single, exact ICD-10 medical code coordinate. | Python · NLP · LLM Routing |
| **[`eternalpose`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/eternalpose%5D(https://github.com/amareshhebbar/eternalpose))** | Inference Routing | Learned complexity classifier + Go proxy that ignores noise and routes queries to the exact, cheapest capable model. | Go · Python · Redis |
| **[`recall`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/recall%5D(https://github.com/amareshhebbar/recall))** | RAG Infrastructure | High-speed, localized context retrieval engine designed to prevent data decay across extensive multi-agent conversational sessions. | Python · VectorDB · Embeddings |

#### Ecosystem Utility & Edge Deployments

| Project | Type | What It Solves | Tech Stack |
| --- | --- | --- | --- |
| **[`allblue`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/allblue%5D(https://github.com/amareshhebbar/allblue))** | API Gateway | The unified convergence layer where multiple distinct data streams, APIs, and agent tools meet into a single, seamless hub. | Go · Next.js · Unified API |
| **[`pocketllm`](https://www.google.com/search?q=%5Bhttps://github.com/amareshhebbar/pocketllm%5D(https://github.com/amareshhebbar/pocketllm))** | Edge Deployment | Ultra-lightweight deployment wrapper to run hyper-quantized, localized reasoning models entirely on edge/mobile devices. | React Native · Expo · Local AI |

## Stack

```
Training:    PyTorch · QLoRA/LoRA · PEFT · Unsloth · HuggingFace TRL · Accelerate
Alignment:   SFT · DPO · GRPO · Model Merging (TIES · DARE · SLERP)
Inference:   vLLM · Flash Attention 2 · FastAPI · Redis
Agents:      LangGraph · MCP · Claude API
Systems:     Go · Docker · GitHub Actions · Linux
Evaluation:  Weights & Biases · lm-evaluation-harness · MMLU · HumanEval
```

---

## Proof Links

- 🤗 **HuggingFace** — [huggingface.co/AmareshHebbar](https://huggingface.co/AmareshHebbar) — fine-tuned model adapters, datasets
- 📊 **W&B Dashboards** — [wandb.ai/amareshhebbar](https://wandb.ai/amareshhebbar) — live training metrics, VRAM curves, eval scores
- 🏆 **LeetCode** — [1100+ problems solved](https://leetcode.com/u/GVAmaresh/)

```
```

<div align="center">

*If you hit a problem I've built a tool for — or want to talk infrastructure — reach out.*

</div>
