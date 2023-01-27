def test_gcd_mod_euclid():
    assert gcd_mod_euclid(12, 36) == 12
    assert gcd_mod_euclid(132, 36) == 12
    assert gcd_mod_euclid(5, 3) == 1


def gcd_mod_euclid(a: int, b: int):
    # Реализация алгоритма Евклида, как для многочленов:
    m = a
    n = b

    # Инвариант GCD(a;b)=GCD(m;n), m, n >= 0
    while not (m == 0 or n == 0):
        if m >= n:
            m %= n
        else:
            n %= m

    # Без ограничения общности: m = 0 => n = GCD(a;b)
    # как последний ненулевой остаток
    return m + n
