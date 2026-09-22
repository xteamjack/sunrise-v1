---
name: rag-ingest
description: Scaffold and run the full ingest path for a source: load, parse, chunk with metadata, embed with Voyage, and load into Qdrant, to the project defaults.
---
# rag-ingest

When asked to ingest a source into the knowledge index, do these steps in order,
following CLAUDE.md and the code in apps/support-agent/src/ingest and apps/support-agent/src/index:

1. Load and parse the source into clean text.
2. Chunk it: a few hundred tokens with a small overlap, and attach metadata
   (source, type, version, region) plus a one-line context per chunk.
3. Embed the chunks with Voyage.
4. Upsert into the Qdrant collection, and update the BM25 keyword index.
5. Run the retrieval validate step and report recall against the eval set.

Never invent policy facts; ingest only what the source says.
