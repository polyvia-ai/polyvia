#!/usr/bin/env bash
# Raw HTTP — ingest a document, poll until indexed, then query. No SDK.
#
# Usage:
#   export POLYVIA_API_KEY="poly_<your-key>"
#   ./curl.sh path/to/report.pdf
set -euo pipefail

BASE="https://app.polyvia.ai"
AUTH="Authorization: Bearer ${POLYVIA_API_KEY:?set POLYVIA_API_KEY}"
FILE="${1:?usage: ./curl.sh path/to/report.pdf}"

# 1. Ingest
task_id=$(curl -sS -X POST "$BASE/api/v1/ingest" \
  -H "$AUTH" \
  -F "file=@$FILE" | jq -r .task_id)
echo "task: $task_id"

# 2. Poll until ingestion completes
while :; do
  status=$(curl -sS "$BASE/api/v1/ingest/$task_id" -H "$AUTH" | jq -r .status)
  echo "status: $status"
  [[ "$status" == "completed" || "$status" == "failed" ]] && break
  sleep 5
done

# 3. Query
curl -sS -X POST "$BASE/api/v1/query" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"query": "What was Q4 revenue, and which chart shows it?"}' | jq -r .answer
