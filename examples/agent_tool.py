"""Expose Polyvia retrieval as a tool your own agent can call.

The pattern is the same for any framework: wrap `client.query(...)` in a
function and hand its schema to the model. Here it's a plain function plus an
Anthropic tool definition — multimodal retrieval over 100K+ docs as one tool.

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python agent_tool.py
"""

from polyvia import Polyvia

client = Polyvia()


def search_documents(query: str, group: str | None = None) -> str:
    """Retrieve a grounded answer over the indexed corpus."""
    result = client.query(query, group=group) if group else client.query(query)
    return result.answer


# Tool definition you can drop into the Claude Messages API `tools=[...]`.
POLYVIA_TOOL = {
    "name": "search_documents",
    "description": (
        "Search the user's multimodal document corpus (charts, slides, tables, "
        "scans) and return a grounded, cited answer. Use for any question whose "
        "answer lives in the documents."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Natural-language question"},
            "group": {"type": "string", "description": "Optional group to scope to"},
        },
        "required": ["query"],
    },
}


if __name__ == "__main__":
    # Direct call (what your agent runs when the model picks the tool):
    print(search_documents("Which borrowers show a 10%+ YoY revenue decline?"))
