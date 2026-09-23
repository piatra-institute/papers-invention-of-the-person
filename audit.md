# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 23 CSL entries. 5 with DOIs resolved through doi.org content negotiation (abusch2015, fowler2004, mauss1938, russo1968, strathern1988); 18 entered by hand. Crossref's automatic match for pariser2011 was a book review and was replaced by the Penguin Press book. sources.md created to hold the provenance note.
- Classical works previously listed as "(Various translations)" and cited by name only now carry citations to standard translations at the passages discussed: aristotle1999 (Irwin), augustine1991 (Chadwick), boethius1973 (Loeb, Contra Eutychen ch. 3), gaius1988 (Gordon and Robinson, Institutes 1.8 and 1.9, attached to the two quotations), aquinas1920 (English Dominican translation, ST I q. 29 a. 1). Descartes, Locke, Hume, Kant and Hegel stay cited by original year without an edition.
- Correction: Foucault 1975/1976/1984 had English titles paired with Gallimard and the French dates; now cited as the Gallimard originals under their French titles (Surveiller et punir; Histoire de la sexualité 1 and 3).
- Correction: abusch2015 chapter "The development of the Epic of Gilgamesh" does not exist under that title; the book (Male and Female in the Epic of Gilgamesh: Encounters, Literary History, and Interpretation, Eisenbrauns 2015) is cited.
- Correction (prose): "Russo (2012), Re-thinking Homeric psychology, in Montanari (ed.), Homeric Contexts" could not be confirmed (no Russo chapter in the Crossref table of contents of Homeric Contexts; no matching 2012 item in Crossref or OpenAlex). The sentence "Joseph Russo called Snell's contention 'fundamentally misguided,' while acknowledging that Homeric psychology differs from later Greek thought (Russo, 2012)" -> "Joseph Russo and Bennett Simon explained the distinctive Homeric representation of mental life as a product of oral epic composition, without concluding from it that Homeric people lacked a unified mind [@russo1968]" (Journal of the History of Ideas 29(4), DOI 10.2307/2708290).
- Removed uncited entries with no supporting passage: kahan2017, friston2013, assmann1997.
- Mauss (1938) page range completed (263-281).
- claims.yaml: 27 claims (20 computation, 1 source, 1 definition, 2 assumption, 3 interpretation), bound to simulation/output/results.json run model.
- Source statements not bound: Fowler (2004) and Abusch (2015) quotations (abstracts support the paraphrase, not the wording); Mauss (1938), Taylor (1989), Strathern (1988), Turner (1969), Pariser (2011) and the classical and early-modern works (no retrievable abstract, or primary texts).
- Execution receipt: run id model (uv run python run_all.py); results.json reproduced byte-identically.
- metadata claims_target: claim-ledger.

## 2026-09-23 — prose revision

Prose rewritten against the house standards. Headings: Abstract; 1 Introduction; 2-6 the five layers (subsections Contribution of the Relational/Epic/Juridical/Interior/Rational Layer; Enkidu and Social Integration; Odysseus and Recognition Tokens; Kant: Transcendental Unity and Autonomy); 7 Socialization and Historicization (Hegel and Mutual Recognition; Foucault and the Production of the Subject; Summary of the Sequence); 8 The Contemporary Thinning (Formal Personhood and Practical Agency, ...); 9 Computational Models (Dated Stratigraphy; Composite Personhood Index; Recognition Network; new 9.4 Limitations); 10 Conclusion.
Tic counts before -> after: "rather than" 13 -> 0; "the paper/this paper" 6 -> 0; "what follows" 1 -> 0; sentence-initial "This is/That is" 5 -> 0; merely/simply 6 -> 1 (Kant's "never merely as a means").
Corrections and changes:
  - Removed the citation of a companion PIATRA paper in section 8.3 and its bibliography entry; the section now states the mediation argument on its own terms and cites Pariser (2011), already in the bibliography.
  - Quotations of Fowler, Strathern, Abusch, Russo, Locke, Hume, Descartes, Kant, Hegel and Foucault now carry author-year citations to entries already in the bibliography; one unattributed "as one scholar puts it" quotation paraphrased without quotation marks.
  - Uncited bibliography entries (Assmann 1997, Friston 2013, Kahan 2017) left in place for later reconciliation.
Grid/number audit: no grid-derived thresholds in the three models (dates are stipulated, the index is a closed-form geometric mean, the network is a single seeded draw). All prose numbers match results.json (4,075; 1,650; 0.39; 0.61; 0.93; 2.4 = 2.381; 14.0; 0.36; 9.5; >25 = 26.41; Gini 0.13 -> 0.61). The second-largest gap (1,169 years, Boethius -> Locke) was stated in prose without a results key; added stratigraphy.second_largest_gap_years and _between, with an assertion that the literate gaps sum to the literate span. Existing results.json values unchanged.
Figure titles replaced with descriptive ones.

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
