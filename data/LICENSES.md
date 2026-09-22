# Dataset licenses

Third-party datasets used in this project, with their source and license.

## Bitext Customer Support LLM Chatbot Training Dataset

- **Dataset:** `bitext/Bitext-customer-support-llm-chatbot-training-dataset`
- **Source:** https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset
- **License:** CDLA-Sharing-1.0 (Community Data License Agreement, Sharing, Version 1.0)
- **Used in:** `apps/support-agent/src/data/acquire_opensource.py` (raw train split, ~26,872 rows) and `apps/support-agent/src/data/transform_opensource.py` (order/refund seed).
- **Local copies:** `data/opensource/bitext_raw.parquet`, `data/opensource/tickets_seed.parquet`.
