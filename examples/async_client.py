"""AsyncPolyvia — the same API surface as the sync client, awaitable.

Docs: https://docs.polyvia.ai/products/python-sdk

Usage:
    export POLYVIA_API_KEY="poly_<your-key>"
    python async_client.py path/to/report.pdf
"""
import asyncio
import sys

from polyvia import AsyncPolyvia


async def main(path: str) -> None:
    async with AsyncPolyvia() as client:  # reads POLYVIA_API_KEY
        task = await client.ingest.file(path, group="Finance")
        await client.ingest.wait(task.task_id)
        answer = await client.query("What are the key findings?", group="Finance")
        print(answer.answer)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python async_client.py path/to/report.pdf")
    asyncio.run(main(sys.argv[1]))
