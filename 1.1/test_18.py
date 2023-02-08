""" Нахождение НОД, но за более быстрый O(loglogn) """


def test_gcd_two_euclid():
    assert gcd_two_euclid(12, 36) == 12
    assert gcd_two_euclid(132, 36) == 12
    assert gcd_two_euclid(5, 3) == 1


def gcd_two_euclid(a: int, b: int):
    m, n = a, b

    d = 1

    # Инвариант: GCD(a; b) = d*GCD(m; n)
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            d *= 2
            m /= 2
            n /= 2
        elif m % 2 == 0 and n % 2 == 1:
            m /= 2
        elif m % 2 == 1 and n % 2 == 0:
            n /= 2
        elif m >= n:
            m -= n
        else:
            n -= m

    # Последний ненулевой остаток
    if m != 0:
        return d * m
    else:
        return d * n
