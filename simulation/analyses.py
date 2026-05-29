"""Three computational analyses instrumenting the stratified-personhood thesis.

The paper argues the modern Person is a stratification: layers assembled over
millennia, held together by institutional supports, and thinning when those
supports are withdrawn while the legal category stays intact. None of the three
analyses below measures history; each makes one structural claim auditable.

  1. stratigraphy  — the assembly is dated and ordered; the span and the gaps
                     are computed from the emergence dates the paper cites.
  2. thinning      — the §8 claim: with the formal layer held at full support,
                     draining practical support collapses a personhood index even
                     though the legal category is intact; profiled and
                     infrastructural humans are two support vectors.
  3. recognition   — the §7 Hegelian claim: personhood is realised through mutual
                     recognition; concentrating who designs the field collapses
                     reciprocated recognition for the many.
"""
from __future__ import annotations

import numpy as np

# ----------------------------------------------------------------------------
# 1. Stratigraphy: dated emergence of the nine formations (year; BCE negative).
# Dates are representative onsets from the works the paper cites, not precise
# measurements; relational personhood is placed in deep prehistory.
# ----------------------------------------------------------------------------
FORMATIONS = [
    ("relational personhood", -100000, "kinship, ritual, burial"),
    ("epic singularization", -2100, "Gilgamesh"),
    ("juridical personhood", -450, "Roman law (Twelve Tables); codified by Gaius, 2c CE"),
    ("interior conscience", 55, "Paul, Epistle to the Romans"),
    ("metaphysical substance", 520, "Boethius"),
    ("self-conscious continuity", 1689, "Locke"),
    ("transcendental autonomy", 1785, "Kant"),
    ("social recognition", 1807, "Hegel"),
    ("historical production", 1975, "Foucault, Discipline and Punish"),
]


def stratigraphy() -> dict:
    dates = [d for _, d, _ in FORMATIONS]
    ordered = [n for n, _, _ in sorted(FORMATIONS, key=lambda x: x[1])]
    full_span = max(dates) - min(dates)
    literate = [d for d in dates if d > -10000]  # post-deep-prehistory
    literate_span = max(literate) - min(literate)
    # largest gap between consecutive formations (after the deep-prehistory jump)
    seq = sorted(literate)
    gaps = [(seq[i + 1] - seq[i]) for i in range(len(seq) - 1)]
    max_gap = max(gaps)
    gi = gaps.index(max_gap)
    return {
        "n_formations": len(FORMATIONS),
        "order_by_date": ordered,
        "full_span_years": full_span,
        "literate_span_years": literate_span,
        "largest_gap_years": max_gap,
        "largest_gap_between": [round(seq[gi]), round(seq[gi + 1])],
        "formations": [{"layer": n, "year": y, "source": s} for n, y, s in FORMATIONS],
    }


# ----------------------------------------------------------------------------
# 2. Composite-thinning model (the §8 thesis).
# Five layers, each with a formal and a practical support in [0,1]. The
# personhood index is the geometric mean across layers, so a single drained
# layer thins the whole composite (the paper: "remove the support for any single
# layer and the composite begins to thin"). The legal category = the formal
# index; lived agency = the practical index.
# ----------------------------------------------------------------------------
LAYERS = ["relational", "epic", "juridical", "interior", "rational"]


def _geomean(xs) -> float:
    xs = np.asarray(xs, float)
    return float(np.exp(np.mean(np.log(xs))))


def thinning() -> dict:
    # formal support is intact for everyone (the legal category persists)
    formal = {L: 1.0 for L in LAYERS}
    # practical support vectors
    full = {L: 1.0 for L in LAYERS}
    profiled = {  # subject of systems: belonging, narratable identity, contestation,
                  # inner privacy, and attention/agency all eroded
        "relational": 0.40, "epic": 0.50, "juridical": 0.30,
        "interior": 0.50, "rational": 0.30}
    infrastructural = {  # author of systems: agency amplified by the same systems
        "relational": 0.90, "epic": 0.85, "juridical": 1.00,
        "interior": 0.90, "rational": 1.00}

    def idx(v):
        return round(_geomean([v[L] for L in LAYERS]), 4)

    formal_index = idx(formal)
    return {
        "formal_index": formal_index,                       # legal category, all scenarios
        "full_practical_index": idx(full),
        "profiled_practical_index": idx(profiled),
        "infrastructural_practical_index": idx(infrastructural),
        "profiled_formal_practical_gap": round(formal_index - idx(profiled), 4),
        "infrastructural_over_profiled": round(idx(infrastructural) / idx(profiled), 4),
        "profiled_supports": profiled,
        "infrastructural_supports": infrastructural,
    }


# ----------------------------------------------------------------------------
# 3. Recognition network (the §7 Hegelian claim).
# N agents; a small infrastructural minority. Realised personhood = reciprocated
# (mutual) recognition. In the egalitarian field recognition is symmetric; in the
# concentrated field everyone recognises the infrastructural nodes, who reciprocate
# mainly to each other. We measure mutual recognition and its inequality.
# ----------------------------------------------------------------------------
def _gini(x) -> float:
    x = np.sort(np.asarray(x, float))
    n = len(x)
    if x.sum() == 0:
        return 0.0
    return float((2 * np.sum((np.arange(1, n + 1)) * x) - (n + 1) * x.sum()) / (n * x.sum()))


def recognition(n: int = 120, k_infra: int = 6, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    infra = np.zeros(n, bool)
    infra[:k_infra] = True

    # egalitarian field: symmetric recognition, density p
    p = 0.12
    U = rng.random((n, n)) < p
    egal = np.triu(U, 1)
    egal = egal | egal.T
    np.fill_diagonal(egal, False)

    # concentrated field: directed recognition
    A = np.zeros((n, n), bool)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if infra[j]:                         # everyone recognises infrastructural nodes
                A[i, j] = True
            elif infra[i] and not infra[j]:      # infra reciprocate to few of the profiled
                A[i, j] = rng.random() < 0.05
            else:                                # profiled recognise each other sparsely
                A[i, j] = rng.random() < 0.04

    def mutual(M):
        MM = M & M.T
        return MM.sum(axis=1)

    egal_m = mutual(egal)
    conc_m = mutual(A)
    in_deg = A.sum(axis=0)  # recognition received (concentrated field)

    return {
        "n_agents": n, "k_infrastructural": k_infra,
        "egalitarian_mean_mutual": round(float(egal_m.mean()), 3),
        "concentrated_mean_mutual_profiled": round(float(conc_m[~infra].mean()), 3),
        "concentrated_mean_mutual_infrastructural": round(float(conc_m[infra].mean()), 3),
        "infra_over_profiled_mutual": round(float(conc_m[infra].mean() / max(conc_m[~infra].mean(), 1e-9)), 2),
        "recognition_gini_egalitarian": round(_gini(egal.sum(axis=0)), 4),
        "recognition_gini_concentrated": round(_gini(in_deg), 4),
    }


def run() -> dict:
    return {"stratigraphy": stratigraphy(), "thinning": thinning(), "recognition": recognition()}
