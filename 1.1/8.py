def test_fact():
    assert fact(3) == 6
    assert fact(0) == 1
    assert fact(5) == 120


def fact(n: int):
    p = 1

    # Инвариант: p = k!
    for k in range(n):
        p *= k + 1

    # p = k!, k = n => p = n!
    return p
