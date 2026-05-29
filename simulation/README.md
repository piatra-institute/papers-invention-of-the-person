# Computational layer — *The Invention of the Person*

Three small models that instrument the paper's structural claims. None is a
historical measurement; each turns one argument into something reproducible.

```
cd simulation
uv run run_all.py        # writes output/results.json + output/figures/*.png
```

- **`stratigraphy()`** — the nine formations dated and ordered by emergence
  (relational personhood in deep prehistory through Foucault, 1975). Computes the
  span and the largest gap. Backs §9.1.
- **`thinning()`** — the §8 thesis. Five layers, each with a *formal* and a
  *practical* support in [0,1]; the personhood index is their geometric mean, so
  one drained layer thins the whole. Holding formal support at 1.0 (the legal
  category intact) while draining practical support reproduces the "formally a
  person, practically thinned" claim, and contrasts the **profiled** and
  **infrastructural** support vectors. Backs §9.2.
- **`recognition()`** — the §7 Hegelian claim. A field of agents whose personhood
  is realised through *mutual* recognition; concentrating who designs the field
  (a small infrastructural minority that receives recognition without
  reciprocating) collapses reciprocated recognition for the many and raises its
  inequality. Backs §9.3.

Every number cited in §9 is a key in `output/results.json`. The recognition model
is seeded (`seed=0`); the other two are deterministic.
