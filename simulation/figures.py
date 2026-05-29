"""Figures for the three personhood analyses."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from analyses import FORMATIONS, LAYERS, thinning, recognition


def plot_stratigraphy(path: str) -> None:
    forms = sorted(FORMATIONS, key=lambda x: x[1])
    names = [n for n, _, _ in forms]
    years = [y for _, y, _ in forms]
    fig, ax = plt.subplots(figsize=(9, 5))
    y = range(len(forms))
    ax.scatter(years, list(y), s=70, color="#542788", zorder=3)
    for i, yr in zip(y, years):
        ax.plot([min(years), yr], [i, i], color="#bbb", lw=0.8, zorder=1)
    ax.set_yticks(list(y)); ax.set_yticklabels(names)
    ax.set_xscale("symlog")
    ax.set_xlabel("year of emergence (symlog; BCE negative)")
    ax.set_title("Stratigraphy of personhood: the order of assembly")
    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)


def plot_thinning(path: str) -> None:
    t = thinning()
    cats = ["formal\n(legal category)", "full\nperson", "profiled\nhuman", "infrastructural\nhuman"]
    vals = [t["formal_index"], t["full_practical_index"],
            t["profiled_practical_index"], t["infrastructural_practical_index"]]
    colors = ["#999", "#1a9850", "#b2182b", "#2166ac"]
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.bar(cats, vals, color=colors)
    ax.axhline(t["formal_index"], ls="--", color="#999", lw=1)
    ax.set_ylim(0, 1.05); ax.set_ylabel("personhood index (geometric mean of layer supports)")
    ax.set_title("Formal personhood intact; practical personhood thinned and unequal")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.02, f"{v:.2f}", ha="center", fontsize=9)
    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)


def plot_recognition(path: str) -> None:
    r = recognition()
    labels = ["egalitarian\n(all)", "concentrated\nprofiled", "concentrated\ninfrastructural"]
    vals = [r["egalitarian_mean_mutual"], r["concentrated_mean_mutual_profiled"],
            r["concentrated_mean_mutual_infrastructural"]]
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.bar(labels, vals, color=["#1a9850", "#b2182b", "#2166ac"])
    ax.set_ylabel("mean reciprocated (mutual) recognition")
    ax.set_title("Concentrating who designs the field collapses reciprocity for the many")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.1, f"{v:.2f}", ha="center", fontsize=9)
    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)
