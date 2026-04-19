# codectx Benchmark Report

Methodology: Naive tokens count all source files excluding tests, docs, and examples using the same file set codectx analyzes.

Caveat: Reduction varies by repository size and structure.

CONTEXT.md artifacts are preserved in `benchmark_results/contexts/` for manual inspection.

Average token reduction vs naive: **77.32%**

| Repo | LOC | Naive Tokens | codectx Tokens | vs Naive | Coverage |
|------|-----|--------------|---------------|----------|----------|
| fastapi | 32351 | 224451 | 78708 | 64.93% | 0.0% (0/528) |
| requests | 5639 | 41427 | 6336 | 84.71% | 0.0% (0/19) |
| typer | 12798 | 80204 | 35731 | 55.45% | 0.0% (0/324) |
| rich | 39043 | 354111 | 28193 | 92.04% | 0.0% (0/109) |
| httpx | 8827 | 63731 | 6716 | 89.46% | 0.0% (0/23) |

## Chart

![Token Comparison](token_comparison.png)
