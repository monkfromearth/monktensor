# monktensor-scalar (v1)

The from-scratch scalar autograd engine behind monktensor — the **learning edition**.

Pure Python, **zero runtime dependencies**, on purpose: the whole point is that every
operation and every gradient is visible. This is the engine you build by hand while
working through the [knowledge course](../../knowledge). It is intentionally small and
inefficient; the fast, production engine is the separate `monktensor` (v2) package.

## What it will contain

A micrograd-style scalar `Value` with automatic differentiation, a tiny neural-net
library (Neuron / Layer / MLP) on top, and a training loop that separates the two-moons
dataset. Build order and definition of done: [docs/roadmap/v1-autograd-engine.md](../../docs/roadmap/v1-autograd-engine.md).

## Develop

From the repo root (uv workspace):

```bash
uv sync                 # create the env, install both the workspace and dev tools
uv run pytest           # run tests (the gradient check lives here once written)
uv run ruff check .     # lint
uv run ruff format .    # format
```

Runtime dependencies stay empty. The make_moons dataset and plotting (scikit-learn,
matplotlib) belong in the repo's `examples/`, never in this engine.
