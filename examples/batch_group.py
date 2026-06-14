"""Ingest a batch of files into a group, then ask one question across all of it.

This is where Polyvia earns its keep: retrieval over a whole corpus, where
file-by-file agentic search would stall.

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python batch_group.py q1.pdf q2.pdf q3.pdf q4.pdf
"""

import sys

from polyvia import Polyvia

client = Polyvia()


def main(paths: list[str]) -> None:
    # A group is a named collection — pass the name and the SDK resolves it.
    items = client.ingest.batch(paths, group="FY24 Earnings")
    for item in items:
        client.ingest.wait(item.task_id)

    # One question, answered jointly across every document in the group.
    answer = client.query(
        "How did revenue trend across the four quarters?",
        group="FY24 Earnings",
    ).answer
    print(answer)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python batch_group.py file1.pdf file2.pdf ...")
    main(sys.argv[1:])
