# Changelog

All notable changes to Polyvia are documented here. The full release notes live
at [docs.polyvia.ai/versions](https://docs.polyvia.ai/versions).

## [1.0.0] — 2026-06-15 · Polyvia-1.0 — Polyvia API

First public release. **Polyvia API** — a Multimodal Document Retrieval API, for
developers of AI agents.

- **REST API v1** — `ingest`, `documents`, `groups`, `query`, `usage`, `rate-limits`.
  Async ingestion with task polling; query workspace-wide, by group, or per document,
  with grounded citations.
- **Python SDK** (`pip install polyvia`) — typed sync **and** async clients, batch
  ingestion, idempotent groups, structured errors.
- **TypeScript SDK** (`npm install polyvia`) — fully typed, ESM/CJS, for Node and
  modern JS.
- **MCP server** — hosted at `app.polyvia.ai/mcp` (`claude mcp add --transport http
  polyvia …`) — connect Claude Code, Cursor and other MCP clients as a retrieval tool.
- **Agent Skills** — `npx skills add polyvia-ai/skills` for Claude Code, Cursor, and
  other agent clients.
- **Visual Document Modalities** — Visual Document Intelligence + Audio: charts,
  graphs & plots, infographics, complex multi-page tables, slides & decks, reports &
  filings, scanned & photographed pages, invoices & forms, handwriting & annotations,
  diagrams & flowcharts, photos & images, and audio.

## Up next

- **Polyvia-1.1 — Polyvia Platform** — Research & Automation Agent over 100K+
  multimodal docs, for knowledge workers in enterprises: chat with reliable
  citations, knowledge-graph view, faster ingestion (uploads up to 50 MB,
  Office/Google formats), usage/API settings, and integrations (Drive, Dropbox,
  OneDrive/SharePoint, S3, Notion, Slack).
- **More modalities** — healthcare scans / EHR, chemical & molecular data, CAD &
  technical drawings, video, geospatial.
- **Polyvia Agents** — build your own agent for automating processes on large
  volumes of multimodal documents.

[1.0.0]: https://github.com/polyvia-ai/polyvia/releases/tag/v1.0.0
