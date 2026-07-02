# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-06-13 — voice reform

Voice-reform pass to remove AI-writing tells, per `tooling/docs/voice.md`. No numbers, dates, simulation values, or citations changed.

- Reduced voice review-candidates 6 → 1 (0 errors throughout). Rewrote the inline-contrastive / negate-pivot constructions as positive declaratives: the Turner rite passage (§2.1), the Roman *persona* "defined by capacity, not by inner life" (§4.1), the doubled Boethius parenthetical glosses (§5.3), the two-grades "difference in kind, not degree" (§8.2), and the §9.2 "the model does not discover this asymmetry" (now "inherits this asymmetry... rather than discovering it"). The one remaining warn (§8.2) now reads as a developed positive contrast.
- Pet-vocabulary: thinned metaphorical "carries" (signature carries/carry 6 → 4) by swapping in "holds" (§7.3) and "rests on" (§9.2); left literal uses ("carry initiates", "works that carry them", "carried out").
- Density: deleted reflexive "exactly" in the Conclusion and "precisely" in §7.1 (both scope-hedges, now 0).
- Structure unchanged (10 numbered sections, no structure advisory). Tricolon proxy 63 (advisory; residual is the genealogy's layer enumerations, which are load-bearing).

Verify: `voice` 0 errors; `refs` unchanged (Turner 1969 in-text citation confirmed resolving; the "missing/unused" report is the pre-existing narrative author-year detection advisory, no citations altered); `build` clean (0 missing-char); `check` => PASS.

## 2026-05-29 (later) — added a computational layer (§9)

The user asked for a computational analysis "of sorts" and, offered three
options, chose all three. Built `simulation/` (numpy + matplotlib, PEP-723) with
three models, each instrumenting one structural claim already argued in prose. No
model measures history; each is a check that a claim composes.

- **stratigraphy** — the nine formations dated by their source works and sorted
  by emergence. Sorting by date reproduces the narrative order of §§2–7 exactly.
  Literate span (Gilgamesh → Foucault) 4,075 yr; full span past 100,000 yr with
  the deep-prehistory relational layer. Largest literate gap 1,650 yr (epic →
  Roman juridical); second 1,169 yr (Boethius → Locke, the medieval interval).
  Backs §9.1.
- **thinning** — the §8 thesis as an index. Five layers, each with a formal and a
  practical support in [0,1]; personhood index = geometric mean (so one drained
  layer thins the whole, matching §7.3). Formal held at 1.00 (legal category
  intact); profiled practical index 0.39 (gap 0.61 from formal), infrastructural
  0.93; the two grades differ ~2.4× in practical personhood at identical formal
  personhood. Backs §9.2.
- **recognition** — the §7 Hegelian claim. 120 agents, 6 infrastructural. Mutual
  (reciprocated) recognition is the realised personhood. Egalitarian field ~14
  mutual ties each, Gini 0.13. Concentrated field: profiled 0.36 vs
  infrastructural 9.5 mutual ties (>25×), Gini rises to 0.61. Backs §9.3.

Integration: new §9 "The Stratification, Modelled" (three subsections) inserted
before the Conclusion (renumbered §10). Abstract gained one sentence naming the
three models; metadata flipped `has_simulation: true`, `claims_target:
results.json`. `simulation/output/results.json` + three figures committed; every
number in §9 is a key in that file.

Verification: voice 0 errors (6 warns: 5 pre-existing inline-contrastive, 1 new
negate-pivot at §9.2 "the model does not discover … it is built from", a
load-bearing epistemic-status contrast, kept); refs advisory (humanities
author-year, as before); claims => 8 prose decimals, 0 unmatched to the sim;
build clean 16 → 18 pp; check => PASS. PDF synced to the web public dir and the
`app/papers` abstract updated locally (web deploy is the user's).

## 2026-05-29 — upgrade pass (Group D)

Baseline: voice 0 errors, refs advisory (primary-source title-year), 16 pages.
A strong genealogy; the pass is surgical voice + two named citations.

Scope contract:
1. Voice tells: §1 "There is a figure" opener; §2.2 negate-then-pivot ("impossible
   to determine … What seems more plausible"); §4.1 "This sounds blunt, and it is";
   §5.1 "may be the most consequential" equivocation; §6.2 "The word 'forensic' is
   crucial" meta-announcement; §6.3 theatrical "blew a hole".
2. Research (named gaps): add ritual anthropology (Turner 1969) where §2 treats
   ritual integration as conferring personhood; cite the companion *Epistemic
   Lensing* paper that §8.3 explicitly builds on.

Next-pass candidates (logged): expand §7 (Hegel, Foucault) — currently compact
relative to their weight; concrete worked example for "optimize without producing
agents" (§8); deepen the rivers/AI legal-personhood analysis (§8.4).

Verification: voice 0 errors; refs advisory; build clean; check => PASS.

## 2026-07-02 — Corpus reform, Phase 0 (integrity)
Removed a fabricated bibliography entry: Sunstein, C. R. (2001), *Echo Chambers:
Bush v. Gore, Impeachment, and Beyond* — no such book exists (the 2001 Sunstein
title is *Republic.com*). It was orphaned (cited nowhere in text) and appeared
identically in this paper and one other, evidence of a shared uncurated
bibliography. Also removed the orphan signSGD (Bernstein et al. 2018) entry
where present. Rebuilt + synced. Remaining uncited refs to be reconciled in the
Phase 2 rewrite of this paper.
