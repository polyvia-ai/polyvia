"""Query across the four scopes Polyvia supports.

Whole workspace · a single document (fastest) · one group · many groups.
Docs: https://docs.polyvia.ai/products/python-sdk

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python query_scopes.py
"""
from polyvia import Polyvia

client = Polyvia()  # reads POLYVIA_API_KEY

# 1. Whole workspace — every completed document you've indexed.
print(client.query("What risks are mentioned across all reports?").answer)

# 2. A single group, by name (the SDK resolves the name to an id).
print(client.query("How did revenue trend this year?", group="FY24 Earnings").answer)

# 3. A single document — fastest and most precise.
print(client.query("What is the executive summary?", document_id="doc_<id>").answer)

# 4. Multiple groups, by id.
print(client.query("Compare the two deals.", group_ids=["g_<id>", "g_<id>"]).answer)
