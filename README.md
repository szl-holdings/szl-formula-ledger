# szl-formula-ledger

**An honest, machine-checked ledger of the SZL formula corpus.**

This repository publishes the formula corpus, a deterministic proof-harness, and
the harness's honest output ledger. CI re-runs the harness on every push/PR so
each math claim carries a receipt — and so no claim can quietly drift.

---

## Doctrine (non-negotiable)

Every claim in this repo is labelled:

| Label | Meaning |
|-------|---------|
| **MEASURED** | Verified live by running the harness this pass. |
| **REPORTED** | An external/internal source asserts it — the source is cited. |
| **UNKNOWN** | Could not be verified here. |
| **CONJECTURE** | Speculation / open problem (an honest label, not an insult). |

And the harness assigns each formula a **status**:

| Status | Meaning |
|--------|---------|
| **CHECKED** | The stated *algebra / units* were machine-verified **this pass**. It does **not** mean the governance semantics or metaphysics are proven, and it **never** upgrades a conjecture. |
| **FAILED** | A check ran and the stated identity/inequality is **false**. |
| **UNCHECKABLE** | No honest machine check exists for this item in this harness (EMPIRICAL needs live data; DEFINITIONAL is true by construction; CONJECTURE is open). A pass is never fabricated. |

### Λ (Lambda) = Conjecture-1, NEVER proven

Λ is the weighted geometric-mean trust aggregator (with Egyptian weights). Its
**uniqueness** (`TH_L1-lambda-uniqueness`) is **Conjecture-1** and stays
`UNCHECKABLE [CONJECTURE]` forever in this harness. Unconditional uniqueness is
machine-checked **false** (a `maxAgg` counterexample exists); only a *conditional*
theorem U holds. `lambda-score-dimensionless` being `CHECKED` is a **units** check
(the Λ score is dimensionless) — it is **not** a proof of the uniqueness conjecture.

**Banned claims:** no perpetual-motion, zero-cost-energy, or "free energy works"
claims appear here — they are prohibited by the estate G3 doctrine. Where energy
is discussed elsewhere in the estate, "free energy" is honestly reframed as REAL
dumped / curtailed / stranded / waste energy.

---

## What is in the ledger

- **`formulas/corpus.json`** — 30 formula items harvested from REAL estate sources
  (no invented formulas). Each item is `{id, source, statement, class}` with
  `class ∈ SYMBOLIC / DIMENSIONAL / EMPIRICAL / DEFINITIONAL / CONJECTURE`.
  Provenance (REPORTED, per the corpus `meta`): `canonical-formulas-v1`,
  a11oy `knowledge.json` (F1–F23 + axioms + theorems), lutar-lean
  `PROVEN_FORMULAS.md` (locked-8) + `Thesis/` + `Thresholds/` + Wave5/6, and
  `ANCIENT_TEXTS_FORMULA_LINEAGE.md`.
- **`harness/harness.py`** — deterministic (seeded) sympy harness. SYMBOLIC items
  are checked with `sympy`; DIMENSIONAL items with `sympy.physics.units`;
  EMPIRICAL / DEFINITIONAL / CONJECTURE items are honestly recorded as
  `UNCHECKABLE`.
- **`ledger.json`** — the harness's honest output (the committed, CI-verified state).

## Current honest tallies (MEASURED — 30 formulas)

| Status | Count |
|--------|-------|
| **CHECKED** | **18** (15 SYMBOLIC + 3 DIMENSIONAL) |
| **UNCHECKABLE** | **12** (4 EMPIRICAL + 4 DEFINITIONAL + 4 CONJECTURE) |
| **FAILED** | **0** |

All four conjectures — `TH_L1-lambda-uniqueness` (Λ = Conjecture-1),
`conjecture-2-khipu-safety`, `conjecture-3-khipu-liveness`,
`code-of-reality-lineage` — are `UNCHECKABLE` and are never upgraded.

Representative CHECKED items (see `ledger.json` for the `method` string of each):
weighted-GM homogeneity (A2), AM-GM slack identity (A4), Reed–Solomon Singleton
bound RS(10,6), Euler χ on the Platonic solids, Horus-Eye unit-fraction sum,
Kraft inequality, quadratic completion, Cauchy–Schwarz (Lagrange identity),
Madhava–Leibniz series, Fisher–Rao self-distance, Byzantine n=3f+1 counting,
Shor `[[9,1,3]]` distance, Pinsker (numeric sampling — **not** a symbolic proof),
and the Bekenstein / Landauer / Λ-score dimensional (units) checks.

## What this is NOT

- **Not** a Lean proof. `lutar-lean` remains the formal track; a sympy check ≠ a
  Lean proof. The ledger records the `method` honestly either way.
- **Not** a claim that any governance semantics are "proven".
- **CHECKED never upgrades a CONJECTURE.**

---

## How to run the harness

Requires Python 3.12 and `sympy`.

```bash
python -m pip install sympy

# regenerate ledger.json from formulas/corpus.json
python harness/harness.py

# CI mode: recompute and compare against the committed ledger.json
# (timestamps ignored). Exits non-zero on any FAILED status or any disagreement.
python harness/harness.py --check
```

## Continuous integration

`.github/workflows/ledger-check.yml` runs on every push and pull request
(Python 3.12). It executes `python harness/harness.py --check`, which **fails the
build** if any formula regresses to `FAILED` or if the freshly computed ledger
disagrees with the committed `ledger.json`. This makes the committed ledger a
receipt that must stay true.

## Retained Kernel Hub compatibility contract

The immutable loading contract for `SZLHOLDINGS/szl-blocked` is maintained in
[`hf-kernels/szl-blocked/README.md`](hf-kernels/szl-blocked/README.md). Its
machine-checked API table intentionally omits exports that the retained artifact
does not implement.

---

*Corpus & harness built Wave-8 R5; published Wave-9 C4. Honesty over hype.*
