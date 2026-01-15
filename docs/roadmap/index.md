# monktensor Roadmap

The plan for building monktensor, in phases. Each phase has its own file with milestones, a definition
of done, and how we work on it. This index is the map; the phase files are the detail.

## The shape of the project

monktensor is built in two stages, beginner-first: build the simple, readable version to learn how
everything works, then climb to the version that is fast and genuinely original.

| Phase | What it is | Status |
|-------|-----------|--------|
| [v1 — Autograd Engine](./v1-autograd-engine.md) | A scalar automatic-differentiation engine plus a tiny neural-net library, trained on the two-moons dataset. Small in lines, deep in ideas. | In progress |
| [v2 — Tensor Framework](./v2-tensor-framework.md) | Climb from scalars to tensors, then to lazy evaluation and kernel fusion — the parts that make a real framework. | Planned |

## Packaging & structure

One repository, two Python packages in a [uv workspace](https://docs.astral.sh/uv/concepts/workspaces/),
with deliberately separate dependency sets:

- **`monktensor-scalar`** (`packages/scalar/`) — v1, pure Python, **zero runtime dependencies**. The
  readable learning engine, kept permanently.
- **`monktensor`** (`packages/monktensor/`, added at v2) — the production framework: numpy, then lazy
  evaluation and kernel fusion. This is what `pip install monktensor` will provide.

Keeping them as separate packages means v1 never has to install numpy and v2's dependencies never leak into
the learning engine. Example-only dependencies (scikit-learn, matplotlib) live in `examples/`. Version line:
`0.x` while v1 is in development, `1.0` for the first production (v2) release.

## Principles

1. **Beginner-first, then advanced.** v1 is the textbook version built to learn the fundamentals. v2 is
   the researched, senior angle layered on top. Build v1 first.
2. **Concepts are taught; code is written by hand.** The [knowledge course](../../knowledge) teaches every
   concept (see [AUTHORING.md](../../knowledge/AUTHORING.md) for how it's written). The implementation is
   written by Sameer, by hand — that is where the understanding sticks. See each phase's collaboration mode.
3. **Senior-repo bar.** A phase is not done at "it runs." It's done with tests (including a gradient check),
   a benchmark or plot that tells a story, a real README, and honest notes on what's left.
4. **No hallucinated facts.** Exact method names, paper claims, and numbers are verified against primary
   sources before they reach the README, docs, or the course.

## Status legend

`[ ]` not started · `[~]` in progress · `[x]` done

## Where this sits

monktensor is the first project in a larger from-scratch engineering portfolio. The deeper, paper-aimed
work (vector search, quantization) builds on the understanding earned here. The broader portfolio roadmap
lives outside this repo, in the workspace planning docs.
