"""Smoke test: the package is importable. Real tests (the gradient check against
finite differences, training convergence) get written by hand as the engine is built."""


def test_package_imports():
    import monktensor_scalar

    assert monktensor_scalar.__version__
