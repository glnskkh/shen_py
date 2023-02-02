def test_slow_power():
    assert slow_power(2, 2) == 4
    assert slow_power(12, 2) == 144
    assert slow_power(4, 0) == 1


def slow_power(a: int, n: int):
    p = 1

    # Инвариант: p = a^k
    for k in range(n):
        p *= a

    # p = a^k, k = n => p = a^n
    return p
