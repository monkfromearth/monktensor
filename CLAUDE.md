# monktensor

A deep learning framework built from scratch: automatic differentiation, neural networks, and training,
from first principles. Built in two stages — a readable scalar engine (v1), then a fast tensor framework
(v2). This file is the entry point for any new session working in this repo.

## Reading order for a new session

1. **This file** — what monktensor is and how we work on it.
2. **[docs/roadmap/index.md](./docs/roadmap/index.md)** — the phased plan; start with the current phase
   ([v1](./docs/roadmap/v1-autograd-engine.md)).
3. **[knowledge/](./knowledge)** — the course that teaches every concept the framework is built on. If
   writing or editing course content, read **[knowledge/AUTHORING.md](./knowledge/AUTHORING.md)** first.

## Collaboration mode (the rule that overrides convenience)

- **v1 is learn-by-building.** The implementation is written by hand, by Sameer. The assistant is a teacher
  and reviewer: guide the theory and the stack, explain plain-English-first then the precise term, scaffold,
  ask Socratic questions, review code, unblock. **The assistant does not write the engine's implementation
  in v1.**
- **The course teaches concepts, never the implementation.** `knowledge/` explains how backprop works (the
  algorithm, the math, worked examples) but never ships the `Value` class or engine code. Knowledge, not
  documentation. See `knowledge/AUTHORING.md` rule 1.
- **v2 is pairing.** Once v1 is done, the research-heavy v2 work is collaborative, code included.

## Repository layout

```
monktensor/                a uv workspace; root pyproject holds shared dev tooling
├── packages/
│   ├── scalar/            monktensor-scalar — v1 engine, pure Python, ZERO runtime deps
│   │   └── src/monktensor_scalar/   (written by hand; starts empty)
│   └── monktensor/        monktensor — v2 production framework (numpy; added later)
├── examples/              demos using the engines (make_moons); example-only deps live here
├── knowledge/             the learning course — Astro site, deployed to GitHub Pages
├── docs/roadmap/          phased plan: index + per-phase files
└── public/                brand assets (logo, wordmark)
```

Two engines, two packages, one repo: v1 (`monktensor-scalar`) stays dependency-free so
every step is visible; v2 (`monktensor`) carries numpy. The make_moons dataset and plots
(scikit-learn, matplotlib) live only in `examples/`, never in either engine.

## Quality bars

- **No hallucinated facts.** Verify method names, paper claims, and numbers against primary sources before
  they reach the README, docs, or course.
- **Senior-repo bar.** A phase is done with tests (including the gradient check), a benchmark or plot that
  tells a story, a real README, and honest notes on what's left — not just "it runs."
- **The gradient check is the key test.** Backprop must match finite-difference nudges within tolerance.

## Working with the knowledge site

```bash
cd knowledge
bun install
bun run dev      # local dev at /monktensor/
bun run build    # static build into knowledge/dist (what Pages deploys)
```

The site is served under the `/monktensor/` base path. Brand assets live in `knowledge/public/` (Astro
serves that directory). The landing page links to the course (`/learn`) and the docs (`/docs`); all 23
lessons live under the unit folders. Animations follow the policy in `knowledge/AUTHORING.md` (meaningful,
interactive, reduced-motion safe).

## Stack

- **Knowledge site:** Astro + Tailwind + GSAP, built with bun.
- **Framework:** Python, managed as a uv workspace. v1 (`monktensor-scalar`) is pure Python with zero
  runtime dependencies; v2 (`monktensor`) will use numpy. Dev tooling: uv, pytest, ruff. Run from the
  repo root: `uv sync`, `uv run pytest`, `uv run ruff check`.
- **Examples:** scikit-learn (`make_moons`) and matplotlib, isolated in `examples/`.
