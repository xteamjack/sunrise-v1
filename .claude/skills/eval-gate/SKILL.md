---
name: eval-gate
description: Run the golden eval set, score retrieval, generation, and agent behavior, print the scorecard, and pass or fail against the thresholds.
---
# eval-gate

When asked to run the eval gate:

1. Load the golden set from data/eval/golden.json.
2. Run the harness in data/eval/ to score retrieval (recall@k, precision@k),
   generation (faithfulness, answer relevance, citation), and agent behavior
   (task success, correct tool, correct escalation).
3. Print the scorecard as a table.
4. Compare against the thresholds in data/eval/thresholds (for example recall@10 >= 0.95,
   faithfulness >= 0.98, task success >= 0.9). Print PASS or FAIL for each and overall.
5. Do not change application code. If it fails, report which stage failed.
