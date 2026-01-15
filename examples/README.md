# examples

Runnable demos that *use* monktensor, kept separate from the engines so the engines stay
clean. Example-only dependencies (scikit-learn for `make_moons`, matplotlib for plots)
live here, never inside `monktensor-scalar` or `monktensor`.

Planned:

- **two-moons** — train the v1 scalar MLP on `sklearn.datasets.make_moons` and plot the
  decision boundary curving between the crescents. This is v1's definition-of-done demo.
