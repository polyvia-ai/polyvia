<div align="center">

# Polyvia

### Multimodal Document Agents over 100K+ files

We build enterprise agents for large-scale retrieval, research and automation over multimodal docs.

[![Docs](https://img.shields.io/badge/docs-docs.polyvia.ai-3b82f6)](https://docs.polyvia.ai)
[![PyPI](https://img.shields.io/pypi/v/polyvia?color=3b82f6&label=pip%20install%20polyvia)](https://pypi.org/project/polyvia)
[![npm](https://img.shields.io/npm/v/polyvia?color=3b82f6&label=npm%20i%20polyvia)](https://www.npmjs.com/package/polyvia)

[Docs](https://docs.polyvia.ai) · [Quickstart](https://docs.polyvia.ai/quickstart) · [Python SDK](https://github.com/polyvia-ai/polyvia-sdk-python) · [TypeScript SDK](https://github.com/polyvia-ai/polyvia-sdk-typescript) · [Platform](https://app.polyvia.ai)

</div>

---

We released our first product as **Polyvia-1.0**: **Polyvia API** — a Multimodal Document Retrieval API, for developers of AI agents. 

Soon we'll be releasing **Polyvia-1.1**: **Polyvia Platform** - Research and Automation Agent over 100K+ multimodal docs.

## Why Polyvia

**1. Fast over 100K+ multimodal docs.** Agentic, file-by-file search (Claude Code,
Claude Cowork, Codex) works only up to ~100 multimodal files — past that it's too
slow, and at scale you still need **retrieval**. Polyvia does **sub-200ms** search
over 100K+ files, every answer grounded in a cited source page.

**2. End-to-end — no extractors or PDF parsers to stitch together.** When you build
large-scale multimodal RAG over a company's files, the only infra available today
is visual extractors / PDF parsers (Reducto, LlamaIndex). There's no **end-to-end**
infra for large-scale multimodal document retrieval — until Polyvia: **Visual
Extractor → Multimodal Knowledge Ontology (mapping all your company's data and
processes) → Agentic Retrieval with Memory**, one pipeline, not a stack of vendors.

### What people build with it
- **Data-room / due-diligence search** — query 100+ visual-heavy PDFs jointly (PE, IB, M&A).
- **Counterparty & credit monitoring** — EBITDA, opex, revenue across hundreds of borrower reports.
- **Multimodal RAG inside your own agent** — retrieval-as-a-tool over large doc sets.
- **Image-based claim processing** — describe claim photos in the context of a policy.
- **Cross-engagement knowledge search** — find answers buried in thousands of slides.

## Install

```bash
pip install polyvia        # Python 3.9+
npm  install polyvia       # Node 18+
```

## Quickstart

Grab a key in [Polyvia Platform](https://app.polyvia.ai) → **Settings → API**.
Ingest a batch into a **group**, then ask one question across the whole corpus —
answers cite the exact page in each document.

```python
from polyvia import Polyvia

client = Polyvia(api_key="poly_<key>")  # or set POLYVIA_API_KEY

# Ingest a batch into a group, then ask one question across all of it.
items = client.ingest.batch(
    ["q1.pdf", "q2.pdf", "q3.pdf", "q4.pdf"],
    group="FY24 Earnings",
)
for item in items:
    client.ingest.wait(item.task_id)

print(client.query("How did revenue trend across the four quarters?",
                   group="FY24 Earnings").answer)
```

```ts
import { Polyvia } from "polyvia";

const client = new Polyvia({ apiKey: "poly_<key>" });

const items = await client.ingest.batch(
  ["q1.pdf", "q2.pdf", "q3.pdf", "q4.pdf"],
  { group: "FY24 Earnings" },
);
await Promise.all(items.map((i) => client.ingest.wait(i.task_id)));

const answer = await client.query(
  "How did revenue trend across the four quarters?",
  { group: "FY24 Earnings" },
);
console.log(answer.answer);
```

Scope a query three ways: a single `document_id` (fastest), a `group` /
`group_ids`, or the whole workspace (no scope).

<details>
<summary>…or raw HTTP (no SDK)</summary>

```bash
curl -X POST https://app.polyvia.ai/api/v1/ingest \
  -H "Authorization: Bearer poly_<key>" \
  -F "file=@q4-report.pdf"

curl -X POST https://app.polyvia.ai/api/v1/query \
  -H "Authorization: Bearer poly_<key>" -H "Content-Type: application/json" \
  -d '{"query": "What was Q4 revenue, and which chart shows it?"}'
```
</details>

## Use it from an agent

**MCP** — connect Claude Code (or any MCP client) to the hosted Polyvia MCP server
in one line, so your agent can retrieve over your documents as a tool:

```bash
claude mcp add --transport http polyvia https://app.polyvia.ai/mcp \
  --header "Authorization: Bearer poly_<your-key>"
```

**Agent Skills** — install Polyvia skills into Claude Code, Cursor, and other agent
clients:

```bash
npx skills add polyvia-ai/skills
```

→ [MCP docs](https://docs.polyvia.ai/products/mcp) · [Agent Skills](https://docs.polyvia.ai/products/skills)

## Roadmap

| | Product | For | Status |
| --- | --- | --- | --- |
| **Polyvia-1.0** | **Polyvia API** — Multimodal Document Retrieval API | Developers of AI agents | **Available now** |
| **Polyvia-1.1** | **Polyvia Platform** — Research & Automation Agent over 100K+ multimodal docs | Knowledge workers in enterprises | **Coming soon** |
| **Later** | **Polyvia Agents** — build your own agent for automating processes on large volumes of multimodal docs | Builders & teams | **Planned** |

## Release log

We update this as we ship — latest first. Full notes at [docs.polyvia.ai/versions](https://docs.polyvia.ai/versions).

### Polyvia-1.0 — Polyvia API · _available now_

- **REST API v1** — `ingest`, `documents`, `groups`, `query`, `usage`, `rate-limits`; async ingestion with task polling and grounded citations.
- **Python SDK** — `pip install polyvia`; typed sync **and** async clients, batch ingestion, idempotent groups, structured errors.
- **TypeScript SDK** — `npm install polyvia`; fully typed, ESM/CJS, Node 18+.
- **MCP server** — hosted at `app.polyvia.ai/mcp` (`claude mcp add --transport http polyvia …`).
- **Agent Skills** — `npx skills add polyvia-ai/skills` for Claude Code, Cursor, and other agent clients.
- **Visual Document Modalities** — Visual Document Intelligence + Audio: charts, graphs & plots, infographics, complex multi-page tables, slides & decks, reports & filings, scanned & photographed pages, invoices & forms, handwriting & annotations, diagrams & flowcharts, photos & images, and audio (calls, meetings, recordings).

### Up next

- **Polyvia-1.1 — Polyvia Platform** — Research & Automation Agent over 100K+ multimodal docs, for knowledge workers in enterprises.
- **More modalities (coming soon)** — healthcare scans / EHR, chemical & molecular data, CAD & technical drawings, video, geospatial.
- **Polyvia Agents** — build your own agent for automating processes on large volumes of multimodal documents.

## SDKs & reference

| | Install | Source |
| --- | --- | --- |
| Python | `pip install polyvia` | [polyvia-sdk-python](https://github.com/polyvia-ai/polyvia-sdk-python) |
| TypeScript | `npm install polyvia` | [polyvia-sdk-typescript](https://github.com/polyvia-ai/polyvia-sdk-typescript) |
| REST API | — | [docs.polyvia.ai/api-reference](https://docs.polyvia.ai/api-reference/introduction) |
| MCP | hosted · `app.polyvia.ai/mcp` | [docs.polyvia.ai/products/mcp](https://docs.polyvia.ai/products/mcp) |
| Agent Skills | `npx skills add polyvia-ai/skills` | [docs.polyvia.ai/products/skills](https://docs.polyvia.ai/products/skills) |

Supported inputs: PDFs · Word/PowerPoint/Excel (DOCX/PPTX/XLSX) · Markdown · text
· images · audio. Charts, infographics, complex multi-page tables, slides, scans
and handwriting are first-class.

## Resources

Runnable snippets (Python, TypeScript, raw HTTP, MCP, agent-tool) live in
[`examples/`](./examples). See also [`CHANGELOG`](./CHANGELOG.md) ·
[`CONTRIBUTING`](./CONTRIBUTING.md) · [`SECURITY`](./SECURITY.md).

📚 [Docs](https://docs.polyvia.ai) · 🖥️ [Platform](https://app.polyvia.ai) · ✉️ senyao@polyvia.ai

## License

© 2026 Polyvia. All rights reserved.
