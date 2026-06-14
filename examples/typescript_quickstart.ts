/**
 * Ingest one document, wait for it to index, then ask a question.
 *
 * Usage:
 *   export POLYVIA_API_KEY="poly_<your-key>"
 *   npx tsx typescript_quickstart.ts path/to/report.pdf
 */

import { Polyvia } from "polyvia";

// Reads POLYVIA_API_KEY from the environment if apiKey is omitted.
const client = new Polyvia();

async function main(path: string): Promise<void> {
  // Ingestion is async: upload returns a task_id, then we block until indexed.
  const { task_id } = await client.ingest.file(path);
  await client.ingest.wait(task_id);

  // Ask anything — the answer is grounded in the exact source page.
  const result = await client.query(
    "What was Q4 revenue, and which chart shows it?",
  );
  console.log(result.answer);
}

const path = process.argv[2];
if (!path) {
  console.error("usage: npx tsx typescript_quickstart.ts path/to/report.pdf");
  process.exit(1);
}
main(path).catch((err) => {
  console.error(err);
  process.exit(1);
});
