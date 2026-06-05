
<div align="center">

# Amaresh Hebbar

**AI Infrastructure Engineer · Go + Python · LLM Training & Inference**

*Building the tooling that makes LLM training and deployment production-ready.*

[![LeetCode](https://img.shields.io/badge/LeetCode-1100%2B_solved-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/u/GVAmaresh/)
[![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-AmareshHebbar-FFD21E?style=flat-square)](https://huggingface.co/AmareshHebbar)
[![W&B](https://img.shields.io/badge/W%26B-Public_Dashboards-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)](https://wandb.ai/amareshhebbar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/gvamaresh)

</div>

---

## What I Work On

I build AI systems at the infrastructure layer — not just calling APIs, but understanding what breaks in production and building tools that prevent it.

Currently engineering a multi-agent health and fitness platform in Bengaluru using Go, Python, LangGraph, and Claude. Every tool I've open-sourced came from a real problem I hit on this platform.

---

## Open Source Projects

> **The problem chain:** I was building a continual fine-tuning system → training died overnight → built a watchdog → couldn't tell what the model was learning → built an interpretability layer → replay data was poisoning the fine-tune → built a data scanner. Each project is the answer to a question the previous one raised.

### Training Infrastructure

| Project | What It Solves | Stack |
|---|---|---|
| [sentinel-train](https://github.com/amareshhebbar/sentinel-train) | Silent GPU faults kill overnight training runs with no error logs. This catches them in real-time, identifies the bad node, and auto-recovers. | Python · PyTorch · CUDA |
| [training-microscope](https://github.com/amareshhebbar/training-microscope) | Loss going down doesn't mean the model is learning the right things. This shows which examples the model focuses on and which behaviors change at each step. | Python · PyTorch hooks · W&B |

### Fine-Tuning & Alignment

| Project | What It Solves | Stack |
|---|---|---|
| [continual-ft](https://github.com/amareshhebbar/continual-ft) | Sequential fine-tuning overwrites previous knowledge. Version control for LoRA adapters — rollback, diff, and replay buffer auto-scheduling. | Python · PEFT · HuggingFace |
| [extreme-qlora](https://github.com/amareshhebbar/extreme-qlora) | Every QLoRA guide assumes a 16GB+ GPU. This runs 7B–13B models on 6–12GB by combining every memory trick simultaneously. | Python · QLoRA · bitsandbytes |
| [lora-scout](https://github.com/amareshhebbar/lora-scout) | LoRA rank is guesswork — wrong rank can make the model worse than baseline. 5-minute micro-probe that predicts optimal rank before a full training run. | Python · PEFT · PyTorch |
| [dataset-doctor](https://github.com/amareshhebbar/dataset-doctor) | 74% of web pages are now AI-generated. Fine-tuning on this data causes reward hacking and model collapse. Pre-training dataset scanner. | Python · sentence-transformers |
| [clean-grpo](https://github.com/amareshhebbar/clean-grpo) | DeepSeek used GRPO for reasoning. Clean implementations don't exist — all are tied to specific models or deprecated APIs. Model-agnostic GRPO trainer. | Python · PyTorch · trl |
| [adapter-merge](https://github.com/amareshhebbar/adapter-merge) | mergekit handles full model merging. Nobody handles LoRA adapter merging. TIES/DARE/SLERP merge for adapters via SVD decomposition. | Python · PyTorch |

### Inference & Agent Systems

| Project | What It Solves | Stack |
|---|---|---|
| [query-router](https://github.com/amareshhebbar/query-router) | 90% of LLM queries don't need GPT-4o. Learned complexity classifier + Go proxy that routes to the cheapest capable model. | Go · Python · Redis |
| [context-engine](https://github.com/amareshhebbar/context-engine) | Long conversations degrade — even frontier models lose 30%+ accuracy by turn 20. L1/L2/L3 memory hierarchy with learned eviction scoring. | Python · Redis · LangGraph |
| [tool-guard](https://github.com/amareshhebbar/tool-guard) | JSON schema validates format, not meaning. Agents hallucinate parameter values that pass validation silently. Real-time semantic interceptor. | Go · Python · sentence-transformers |
| [forgetting-radar](https://github.com/amareshhebbar/forgetting-radar) | Fine-tuning a model for a domain kills its general capabilities. Pre/post audit that scores exactly what was retained vs forgotten. | Python · lm-evaluation-harness |

---

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

---

## Currently

- Building multi-agent health platform · Go + Python + Claude API · Bengaluru
- Open to: remote B2B contract · LLM training infra / fine-tuning / inference
- Rate: $10,000 USD/month

---

<div align="center">

*If you hit a problem I've built a tool for — or want to talk infrastructure — reach out.*

</div>