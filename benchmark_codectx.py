import os
import subprocess
import tempfile
from pathlib import Path

import tiktoken
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, colors


REPOS = {
    "fastapi": "https://github.com/fastapi/fastapi",
    "requests": "https://github.com/psf/requests",
    "typer": "https://github.com/tiangolo/typer",
    "rich": "https://github.com/Textualize/rich",
    "httpx": "https://github.com/encode/httpx",
}


ENC = tiktoken.get_encoding("cl100k_base")

OUTPUT_DIR = Path("benchmark_results")
CONTEXTS_DIR = OUTPUT_DIR / "contexts"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True, stdout=subprocess.DEVNULL)


def clone_repo(url, dest):
    run(f"git clone --depth 1 {url} {dest}")


def collect_files(repo):
    files = []

    skip_dirs = [
        ".git",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".codectx_cache",
        "node_modules",
        "dist",
        "build",
        "coverage",
        "tests",
        "test",
        "docs",
        "doc",
        "examples",
        "venv",
        ".venv",
        "node_modules",
    ]

    for root, dirs, names in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for f in names:
            if f.endswith((".py", ".ts", ".js", ".go", ".rs", ".java")):
                files.append(Path(root) / f)

    files.sort()
    return files


def read_file(path):
    try:
        return path.read_text(errors="ignore")
    except (OSError, UnicodeDecodeError):
        return ""


def token_count(text):
    return len(ENC.encode(text, disallowed_special=()))


def naive_baseline(repo):
    text = ""
    loc = 0
    files = collect_files(repo)

    for f in files:
        content = read_file(f)
        text += content
        loc += len(content.splitlines())

    return text, loc, len(files)

def run_codectx(repo):
    run("codectx analyze . --no-git", cwd=repo)


def read_context(repo):
    ctx = Path(repo) / "CONTEXT.md"
    if ctx.exists():
        return ctx.read_text(errors="ignore")
    return ""


def parse_ranked_files(context_text):
    in_ranked = False
    represented = 0

    for line in context_text.splitlines():
        stripped = line.strip()
        upper = stripped.upper()

        if upper.startswith("##") and "RANKED_FILES" in upper:
            in_ranked = True
            continue

        if in_ranked and upper.startswith("##") and "RANKED_FILES" not in upper:
            break

        if not in_ranked or not stripped:
            continue

        if stripped.startswith(("```", "|", "---")):
            continue

        is_bullet = stripped.startswith(("-", "*"))
        is_numbered = stripped[0].isdigit() if stripped else False
        if not (is_bullet or is_numbered):
            continue

        if "periphery" not in stripped.lower():
            represented += 1

    return represented

def benchmark_repo(name, url, workspace):
    repo_path = workspace / name
    clone_repo(url, repo_path)

    naive_text, loc, total_files = naive_baseline(repo_path)
    naive_tokens = token_count(naive_text)

    run_codectx(repo_path)

    ctx_text = read_context(repo_path)
    if len(ctx_text) <= 500:
        raise RuntimeError(
            f"Invalid CONTEXT.md for {name}: missing or too short ({len(ctx_text)} chars)"
        )

    CONTEXTS_DIR.mkdir(parents=True, exist_ok=True)
    (CONTEXTS_DIR / f"{name}_CONTEXT.md").write_text(ctx_text)

    ctx_tokens = token_count(ctx_text)
    files_represented = parse_ranked_files(ctx_text)

    reduction = (
        (naive_tokens - ctx_tokens) / naive_tokens * 100
        if naive_tokens else 0
    )

    coverage_percent = (files_represented / total_files * 100) if total_files else 0

    return {
        "repo": name,
        "loc": loc,
        "baseline_naive": naive_tokens,
        "codectx_tokens": ctx_tokens,
        "files_represented": files_represented,
        "total_files": total_files,
        "coverage_percent": coverage_percent,
        "tokens_per_loc_naive": naive_tokens / loc if loc else 0,
        "tokens_per_loc_codectx": ctx_tokens / loc if loc else 0,
        "reduction_percent": reduction,
    }


def generate_charts(df):
    repos = df["repo"]
    naive = df["baseline_naive"]
    codectx = df["codectx_tokens"]
    reduction = df["reduction_percent"]

    x = np.arange(len(repos))
    width = 0.35

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={"width_ratios": [1.35, 1]})

    bars_naive = ax_left.bar(
        x - width / 2,
        naive,
        width,
        label="Naive baseline",
        color="#4C78A8",
    )

    bars_ctx = ax_left.bar(
        x + width / 2,
        codectx,
        width,
        label="codectx",
        color="#54A24B",
    )

    ax_left.set_xticks(x, repos)
    ax_left.set_ylabel("Tokens")
    ax_left.grid(axis="y", linestyle="--", alpha=0.35)

    context_limit = 128000
    max_val = max(float(naive.max()), float(codectx.max()), context_limit)
    ax_left.set_ylim(0, max_val * 1.2)
    ax_left.axhline(context_limit, linestyle="--", alpha=0.8, color="red")
    ax_left.axhspan(context_limit, ax_left.get_ylim()[1], color="red", alpha=0.09)

    y_min, y_max = ax_left.get_ylim()
    y_range = y_max - y_min
    pct_label_offset = y_range * 0.035

    def fmt_tokens(n):
        if n >= 1000:
            return f"{int(n/1000)}k"
        return str(int(n))

    for bars in [bars_naive, bars_ctx]:
        for bar in bars:
            height = bar.get_height()
            ax_left.text(
                bar.get_x() + bar.get_width()/2,
                height,
                fmt_tokens(height),
                ha="center",
                va="bottom",
                fontsize=9,
            )

    for i, bar in enumerate(bars_ctx):
        ax_left.text(
            bar.get_x() + bar.get_width()/2,
            min(bar.get_height() + pct_label_offset, y_max * 0.98),
            f"{reduction.iloc[i]:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            color="#1b7f3a",
        )

    ax_left.legend(loc="upper right")

    red_vals = reduction.to_numpy(dtype=float)
    vmin = float(red_vals.min()) if len(red_vals) else 0.0
    vmax = float(red_vals.max()) if len(red_vals) else 1.0
    if np.isclose(vmin, vmax):
        vmax = vmin + 1.0
    norm = colors.Normalize(vmin=vmin, vmax=vmax)
    right_colors = cm.get_cmap("Greens")(norm(red_vals))

    bars_right = ax_right.barh(repos, red_vals, color=right_colors)
    ax_right.set_xlabel("Reduction vs Naive (%)")
    ax_right.grid(axis="x", linestyle="--", alpha=0.35)
    ax_right.set_xlim(min(0.0, vmin - 5), max(100.0, vmax + 5))

    for bar, val in zip(bars_right, red_vals):
        ax_right.text(
            bar.get_width() + 1.2,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%",
            va="center",
            fontsize=9,
            fontweight="bold",
        )

    title_min = int(np.rint(red_vals.min())) if len(red_vals) else 0
    title_max = int(np.rint(red_vals.max())) if len(red_vals) else 0
    fig.suptitle(
        f"codectx reduces repository context by {title_min}–{title_max}% vs raw source",
        fontsize=14,
        fontweight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95))

    fig.savefig(OUTPUT_DIR / "token_comparison.png", dpi=300)
    plt.close(fig)


def generate_markdown(df):
    avg_reduction = df["reduction_percent"].mean()

    md = "# codectx Benchmark Report\n\n"

    md += "Methodology: Naive tokens count all source files excluding tests, docs, and examples using the same file set codectx analyzes.\n\n"
    md += "Caveat: Reduction varies by repository size and structure.\n\n"
    md += "CONTEXT.md artifacts are preserved in `benchmark_results/contexts/` for manual inspection.\n\n"
    md += f"Average token reduction vs naive: **{avg_reduction:.2f}%**\n\n"

    md += "| Repo | LOC | Naive Tokens | codectx Tokens | vs Naive | Coverage |\n"
    md += "|------|-----|--------------|---------------|----------|----------|\n"

    for _, r in df.iterrows():
        coverage_display = f"{r['coverage_percent']:.1f}% ({int(r['files_represented'])}/{int(r['total_files'])})"
        md += (
            f"| {r['repo']} | {int(r['loc'])} | {int(r['baseline_naive'])} | "
            f"{int(r['codectx_tokens'])} | {r['reduction_percent']:.2f}% | "
            f"{coverage_display} |\n"
        )

    md += "\n## Chart\n\n"
    md += "![Token Comparison](token_comparison.png)\n"

    (OUTPUT_DIR / "report.md").write_text(md)


def main():
    workspace = Path(tempfile.mkdtemp(prefix="codectx_bench_"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CONTEXTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for name, url in REPOS.items():

        print(f"Benchmarking {name}")

        try:

            r = benchmark_repo(name, url, workspace)
            results.append(r)

        except Exception as e:
            print("Failed:", name, e)

    if not results:
        raise RuntimeError("No benchmark results were collected.")

    df = pd.DataFrame(results)

    df.to_csv(OUTPUT_DIR / "results.csv", index=False)
    df.to_json(OUTPUT_DIR / "results.json", orient="records", indent=2)

    generate_charts(df)
    generate_markdown(df)

    print("\nBenchmark complete.")
    print(f"Results saved in: {OUTPUT_DIR}")
    print(f"Workspace preserved at: {workspace}")


if __name__ == "__main__":
    main()