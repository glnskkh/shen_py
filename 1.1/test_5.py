def test_mult():
    assert mult(2, 2) == 4
    assert mult(3, 2) == 6
    assert mult(2, 3) == 6
    assert mult(0, 2) == 0


def mult(a: int, b: int):
    r = 0

    # Инвариант: r = a*k
    for k in range(b):
        r += a

    # r = a*k, k = b => r = a*b
    return r
