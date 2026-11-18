"""Compare lexical diversity across two arXiv abstracts."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Read results from the original and custom experiments.
original = pd.read_csv("data/processed/case_processed.csv")
aviation = pd.read_csv("data/processed/atc_conflict_processed.csv")

papers = ["Agents of Chaos", "ATC Conflict Resolution"]
scores = [
    original["abstract_lexical_diversity"].iloc[0],
    aviation["abstract_lexical_diversity"].iloc[0],
]

# Create the comparison chart.
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(papers, scores)

ax.set_title("Lexical Diversity of Academic Paper Abstracts")
ax.set_ylabel("Lexical Diversity Score")
ax.set_ylim(0, 1)
ax.bar_label(bars, fmt="%.3f", padding=4)

fig.tight_layout()

# Save the chart for GitHub Pages.
output = Path("docs/images/lexical_diversity_comparison.png")
output.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(output, dpi=150)
plt.close(fig)

print(f"Chart saved to {output}")
