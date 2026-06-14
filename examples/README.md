# Polyvia examples

Runnable snippets for the [Polyvia API](https://docs.polyvia.ai) — the
Multimodal Document Retrieval API for developers of AI agents.

Grab a key in [Polyvia Platform](https://app.polyvia.ai) → **Settings → API**,
then export it:

```bash
export POLYVIA_API_KEY="poly_<your-key>"
```

| File | What it shows |
| --- | --- |
| [`python_quickstart.py`](./python_quickstart.py) | Ingest one file, wait, then query |
| [`batch_group.py`](./batch_group.py) | Ingest a batch into a group, then ask one question across all of it |
| [`typescript_quickstart.ts`](./typescript_quickstart.ts) | The same loop in TypeScript |
| [`agent_tool.py`](./agent_tool.py) | Expose Polyvia retrieval as a tool to your own agent |
| [`curl.sh`](./curl.sh) | Raw HTTP — no SDK |
| [`mcp/claude_desktop_config.json`](./mcp/claude_desktop_config.json) | Connect Polyvia to Claude Desktop / Cursor via MCP |

## Run them

```bash
# Python
pip install polyvia
python examples/python_quickstart.py path/to/report.pdf

# TypeScript
npm install polyvia
npx tsx examples/typescript_quickstart.ts path/to/report.pdf
```

Full reference: **[docs.polyvia.ai](https://docs.polyvia.ai)**.
