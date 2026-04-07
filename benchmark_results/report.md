# codectx Benchmark Report

Methodology: Naive tokens count all source files excluding tests, docs, and examples using the same file set codectx analyzes.

Caveat: Reduction varies by repository size and structure.

CONTEXT.md artifacts are preserved in `benchmark_results/contexts/` for manual inspection.

Average token reduction vs naive: **76.19%**

| Repo | LOC | Naive Tokens | codectx Tokens | vs Naive | Coverage |
|------|-----|--------------|---------------|----------|----------|
| fastapi | 32283 | 223936 | 88813 | 60.34% | 0.0% (0/527) |
| requests | 5637 | 41412 | 6862 | 83.43% | 0.0% (0/19) |
| typer | 12759 | 79994 | 36429 | 54.46% | 0.0% (0/323) |
| rich | 39002 | 353919 | 28001 | 92.09% | 0.0% (0/109) |
| httpx | 8827 | 63731 | 5976 | 90.62% | 0.0% (0/23) |

## Chart

![Token Comparison](token_comparison.png)
