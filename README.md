# Sunrise (sunrise-v1)

A multi-agent customer-support system for Sunrise Electronics, built as a monorepo.
Each agent or service is an app under apps/; shared data, synthesizers, and pipelines
live under data/; project memory and docs live under _memory/ and docs/.

First app: apps/support-agent, a support-deflection agent for order status, returns,
and simple warranty. It answers from Sunrise's own content and escalates anything
out of scope. Refunds above Rs 5,000 need human approval. Data stays in Bharat.

Build order: see the cookbook modules 1 to 15.
