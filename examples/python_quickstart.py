"""Ingest one document, wait for it to index, then ask a question.

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python python_quickstart.py path/to/report.pdf
"""

import sys

from polyvia import Polyvia

# Reads POLYVIA_API_KEY from the environment if api_key is omitted.
client = Polyvia()


def main(path: str) -> None:
    # Ingestion is async: upload returns a task_id, then we block until indexed.
    task = client.ingest.file(path)
    client.ingest.wait(task.task_id)

    # Ask anything — the answer is grounded in the exact source page.
    result = client.query("What was Q4 revenue, and which chart shows it?")
    print(result.answer)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python python_quickstart.py path/to/report.pdf")
    main(sys.argv[1])
