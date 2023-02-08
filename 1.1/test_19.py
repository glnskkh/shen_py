""" Нахождение НОД и линейной формы, но за более быстрый O(loglogn) """


def test_gcd_linear_two_euclid():
    d, x, y = gcd_linear_two_euclid(12, 36)
    assert d == 12
    assert 12*x+36*y == d

    d, x, y = gcd_linear_two_euclid(132, 36)
    assert d == 12
    assert 132*x+36*y == d

    d, x, y = gcd_linear_two_euclid(5, 3)
    assert d == 1
    assert 5*x+3*y == d


class BinRational:
    def __init__(self, a: int, div: int):
        self.a = a
        self.div = div

    def div_two(self):
        self.div *= 2

    def add(self, other):
        if self.div >= other.div:
            return BinRational(self.a + (self.div/other.div)*other.a, self.div)
        else:
            return other.add(self)

    def sub(self, other):
        return self.add(BinRational(-other.a, other.div))


def gcd_linear_two_euclid(a: int, b: int):
    m, n = a, b

    p = BinRational(1, 1)
    q = BinRational(0, 1)
    s = BinRational(0, 1)
    t = BinRational(1, 1)

    d = 1

    # Инвариант:
    # GCD(a;b) = d*GCD(m; n)
    # m = ma*p+mb*q, n = na*s+nb*t
    # d*m = a*p+b*q, d*n = a*s+b*t, так что a = d*ma, b = d*mb и так далее.
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            d *= 2

            m //= 2
            p.div_two()
            q.div_two()

            n //= 2
            s.div_two()
            t.div_two()
        elif m % 2 == 0:
            m //= 2
            p.div_two()
            q.div_two()
        elif n % 2 == 0:
            n //= 2
            s.div_two()
            t.div_two()
        elif m >= n:
            m -= n

            p = p.sub(s)
            q = q.sub(t)
        else:
            n -= m

            s = s.sub(p)
            t = t.sub(q)

    # Последний ненулевой остаток
    if m != 0:
        a //= d
        b //= d

        rem = max(p.div, q.div)

        x = (rem // p.div) * p.a
        y = (rem // q.div) * q.a

        while rem > d:
            if x % 2 == 0 and y % 2 == 0:
                x //= 2
                y //= 2
                rem //= 2
            else:
                x += b
                y -= a

        return d * m, x, y
    else:
        a //= d
        b //= d

        rem = max(s.div, t.div)

        x = (rem // s.div) * s.a
        y = (rem // t.div) * t.a

        while rem > d:
            if x % 2 == 0 and y % 2 == 0:
                x //= 2
                y //= 2
                rem //= 2
            else:
                x += b
                y -= a

        return d * n, x, y
