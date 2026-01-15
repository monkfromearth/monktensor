<div align="center">
  <img src="./public/logo-wordmark.svg" alt="monktensor" width="420" />

  <p><strong>A deep learning framework built from scratch.</strong></p>

  <p>Automatic differentiation, neural networks, and training — from first principles, one number at a time.</p>

  <p>
    <a href="https://monkfromearth.github.io/monktensor/learn">Course</a> ·
    <a href="https://monkfromearth.github.io/monktensor/docs">Docs</a> ·
    <a href="./docs/roadmap/index.md">Roadmap</a>
  </p>
</div>

---

## What this is

monktensor is a deep learning framework built from the ground up to make one thing concrete: how learning
actually works. Under the branding, every framework (PyTorch, TensorFlow, JAX, tinygrad) is the same
machine — it represents a computation as a graph, runs it forward, computes gradients automatically, and
updates the numbers. monktensor builds that machine on plain scalars first, so every operation and every
gradient is visible, then climbs toward tensors and a compiler.

## What's different

- **No black boxes.** The autograd engine starts on single numbers. You can read every operation and watch
  every gradient, instead of trusting a library.
- **Taught, not just shipped.** A full interactive course ships *with* the code. It teaches the concepts —
  derivatives, the computation graph, backpropagation, training — and leaves the implementation to you,
  which is where the understanding sticks. It deliberately never hands you the engine's source.
- **A real path to a real framework.** v1 is a scalar engine that trains a network. v2 climbs to tensors,
  then lazy evaluation and kernel fusion — the parts that make a framework fast and not just a clone.
- **Built to a senior bar.** Tests (including a gradient check against numerical derivatives), a
  decision-boundary plot, and honest docs — not a notebook that runs once.

## The two stages

| Stage | What it is | Status |
|-------|-----------|--------|
| **v1 — Autograd Engine** | A scalar automatic-differentiation engine + a tiny neural-net library, trained on the two-moons dataset. Small in lines, deep in ideas. | In progress |
| **v2 — Tensor Framework** | Tensors and broadcasting, then lazy evaluation and kernel fusion. | Planned |

Full detail: [docs/roadmap/](./docs/roadmap/index.md).

## Tech stack

| Part | Stack |
|------|-------|
| **Framework (v1)** | Python. The scalar autograd engine is pure Python so every step is visible; numpy is used only for the toy dataset and plotting. *(Implementation stack is being finalized before v1 coding begins.)* |
| **Framework (v2)** | Python with numpy for tensors; later a lazy graph and a fusing compiler backend. |
| **Knowledge course** | [Astro](https://astro.build) + [Tailwind CSS](https://tailwindcss.com) + [GSAP](https://gsap.com) for the interactive demos, built with [bun](https://bun.sh). Deployed to GitHub Pages. |

## Learn it: the course

The [`knowledge/`](./knowledge) folder is a full interactive course — 23 lessons across 6 units, with
animated demos — that teaches the concepts behind monktensor. It is live at
**[monkfromearth.github.io/monktensor](https://monkfromearth.github.io/monktensor/)**.

Run it locally:

```bash
cd knowledge
bun install
bun run dev      # http://localhost:4321/monktensor/
```

Authoring the course follows [`knowledge/AUTHORING.md`](./knowledge/AUTHORING.md) (voice, structure, and the
animation policy).

## Repository layout

```
monktensor/
├── knowledge/     the interactive course (Astro site) — concepts, not implementation
├── src/           the framework source
├── tests/         tests, including the gradient check against numerical derivatives
├── docs/          roadmap, and later the hosted documentation
│   └── roadmap/   phased plan: index + per-phase files
└── public/        brand assets (logo, wordmark)
```

## Status

Early. v1 is in active development; the interactive course is complete. Structure and docs grow with the
project.

## License

MIT (see [`LICENSE`](./LICENSE)).

---

<div align="center">
  <sub>Built by <a href="https://github.com/monkfromearth">Sameer</a> · part of the monk family of projects</sub>
</div>
