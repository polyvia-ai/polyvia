"""Manage groups and documents with the Python SDK.

Docs: https://docs.polyvia.ai/products/python-sdk

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python groups_and_documents.py
"""
from polyvia import Polyvia

client = Polyvia()  # reads POLYVIA_API_KEY

# --- Groups -------------------------------------------------------------
# Idempotent: returns the existing group or creates it (matched by name).
group = client.groups.get_or_create("FY24 Earnings")
print("group:", group.id, group.name)

client.groups.find("FY24 Earnings")          # None if it doesn't exist
for g in client.groups.list():
    print("  -", g.name, g.id)

# --- Documents ----------------------------------------------------------
# List (filter by status and/or group), then read one.
docs = client.documents.list(status="completed", group_id=group.id)
print(f"{len(docs)} completed docs in group")

if docs:
    doc_id = docs[0].id
    client.documents.get(doc_id)                       # metadata + summary
    client.documents.update(doc_id, group_id=group.id)  # move into a group
    client.documents.update(doc_id, group_id=None)      # remove from any group
    # client.documents.delete(doc_id)                   # permanent — uncomment to run

# --- Clean up a whole group --------------------------------------------
# Deletes the group's documents first, then the group itself.
# client.groups.delete(group.id, delete_documents=True)
