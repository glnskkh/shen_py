""" Нахождение НОД и линейной формы НОД, сложность O(loglogn) """


def test_gcd_linear_mod_euclid():
    d, x, y = gcd_linear_mod_euclid(12, 36)
    assert d == 12
    assert 12*x+36*y == d

    d, x, y = gcd_linear_mod_euclid(132, 36)
    assert d == 12
    assert 132*x+36*y == d

    d, x, y = gcd_linear_mod_euclid(5, 3)
    assert d == 1
    assert 5*x+3*y == d


def gcd_linear_mod_euclid(a: int, b: int):
    m, n = a, b

    p, q = 1, 0
    s, t = 0, 1

    # Инвариант:
    # GCD(a; b) = GCD(m; n); m, n >= 0
    # m = pa + qb; n = sa + tb
    while not (m == 0 or n == 0):
        if m >= n:
            p -= (m // n) * s
            q -= (m // n) * t
            m %= n
        else:
            s -= (n // m) * p
            t -= (n // m) * q
            n %= m

    # Без ограничения общности:
    # если m = 0, то n = GCD(a; b) как ненулевой остаток
    # учитывая инвариант n = sa+tb

    if m != 0:
        return m, p, q
    else:
        return n, s, t
