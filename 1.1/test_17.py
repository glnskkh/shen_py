""" Нахождение НОД и НОК за O(logn) """


def test_gcd_deikstra():
    # 2 * LCD(12, 36) == 72
    assert gcd_deikstra(12, 36) == 72


def gcd_deikstra(a: int, b: int):
    m, n = a, b
    u, v = b, a

    # Инвариант:
    # GCD(a; b) = GCD(m; n)
    # m*u+n*v = 2*a*b is constant
    while not (m == 0 or n == 0):
        if m >= n:  # (m-n)*u+n*(u+v) = m*u-n*u+n*u+n*v = m*u+n*v
            m -= n
            v += u
        else:  # m*(u+v)+(n-m)*u = m*u+m*v+n*u-m*u = m*v+n*u
            n -= m
            u += v

    # 2й инвариант = > либо m*u либо n*v = 2*a*b
    # Но a*b = GCD(a; b)*LCD(a; b) |= >
    # либо u либо v = 2*LCD(a; b)

    # Последний ненулевой остаток
    if m != 0:
        return u
    else:
        return v
