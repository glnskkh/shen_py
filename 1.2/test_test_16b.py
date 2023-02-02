def test_fast_poly_mult():
    assert fast_poly_mult([1, 1], [1, 1]) == [1, 2, 1]
    assert fast_poly_mult([1, -1], [1, 1, 1]) == [1, 0, 0, -1]


def fast_poly_mult(a: list[float], b: list[float]) -> list[float]:
    pass
