"""monktensor-scalar — the from-scratch scalar autograd engine (v1, learning edition).

Pure Python, zero runtime dependencies, so every operation and every gradient is
visible. The implementation is written by hand while working through the knowledge
course (see ../../knowledge); this package starts intentionally empty.

Build order (see docs/roadmap/v1-autograd-engine.md):
    1. the scalar Value type
    2. forward operations (+, *, **, an activation) with local gradients
    3. backward(): topological sort + chain rule + accumulation
    4. the gradient check against finite differences
    5. Neuron / Layer / MLP
    6. a loss + the SGD training loop
    7. train make_moons and plot the decision boundary
"""

__version__ = "0.1.0"
