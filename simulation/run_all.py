"""Orchestrator: reproduces every numerical claim in the paper's modelled section.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the modelled section is a key in the JSON file.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_stratigraphy, plot_thinning, plot_recognition

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_stratigraphy(str(OUT / "figures" / "stratigraphy.png"))
    plot_thinning(str(OUT / "figures" / "thinning.png"))
    plot_recognition(str(OUT / "figures" / "recognition.png"))
    s, t, r = results["stratigraphy"], results["thinning"], results["recognition"]
    print(f"stratigraphy: {s['n_formations']} formations, literate span {s['literate_span_years']} yr, "
          f"largest gap {s['largest_gap_years']} yr {s['largest_gap_between']}")
    print(f"thinning: formal {t['formal_index']}; practical profiled {t['profiled_practical_index']} "
          f"vs infrastructural {t['infrastructural_practical_index']} ({t['infrastructural_over_profiled']}x)")
    print(f"recognition: profiled {r['concentrated_mean_mutual_profiled']} vs infrastructural "
          f"{r['concentrated_mean_mutual_infrastructural']} ({r['infra_over_profiled_mutual']}x); "
          f"Gini {r['recognition_gini_egalitarian']} -> {r['recognition_gini_concentrated']}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
