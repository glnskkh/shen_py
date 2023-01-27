def test_gcd_euclid():
    assert gcd_euclid(12, 36) == 12
    assert gcd_euclid(132, 36) == 12
    assert gcd_euclid(5, 3) == 1


def gcd_euclid(a: int, b: int):
    # Ниже просто реализуется алгоритм Евклида для чисел a и b
    m = a
    n = b

    # Инвариант GCD(a;b)=GCD(m;n), m, n >= 0
    while not (m == 0 or n == 0):
        if m >= n:
            m -= n
        else:
            n -= m

    # Без ограничения общности m = 0, тогда n = GCD(a;b)
    # как последний ненулевой член при использовании алгоритма Евклида
    return m + n
