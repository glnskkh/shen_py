def test_poly_sum():
    assert poly_sum([1, 1, 1], [1, 1]) == [2, 2, 1]


def test_poly_shift():
    assert poly_shift([1, 1, 1], 2) == [0, 0, 1, 1, 1]


def test_fast_poly_mult():
    assert fast_poly_mult([1, 1], [1, 1]) == [1, 2, 1]


def poly_sum(a: list[float], b: list[float]) -> list[float]:
    k = max(len(a), len(b))

    r = [.0] * k

    l = k - 1
    while l >= 0:
        r[l] += a[l] if l < len(a) else 0
        r[l] += b[l] if l < len(b) else 0

        l -= 1

    return r


def poly_sub(a: list[float], b: list[float]) -> list[float]:
    r = [-i for i in b]

    return poly_sum(a, r)


def poly_shift(x: list[float], n: int) -> list[float]:
    return ([.0] * n) + x[:]


def poly_mult_const(x: list[float], c: float) -> list[float]:
    r = x[:]

    for i in range(len(r)):
        r[i] *= c

    return r


def fast_poly_mult(a: list[float], b: list[float]) -> list[float]:
    "Быстрый алгоритм умножения многочленов степеней 2^n"
    # По аналогии с 16a.py

    if len(a) <= 1:
        m = a[0] if len(a) == 1 else 0
        return poly_mult_const(b, m)

    if len(b) <= 1:
        m = b[0] if len(b) == 1 else 0
        return poly_mult_const(a, m)

    k = min(len(a), len(b)) // 2

    A = a[:k]
    B = a[k:]

    C = b[:k]
    D = b[k:]

    AC = fast_poly_mult(A, C)
    BD = fast_poly_mult(B, D)

    S1 = poly_sum(A, B)
    S2 = poly_sum(C, D)
    MID = fast_poly_mult(S1, S2)
    MID = poly_sub(MID, AC)
    MID = poly_sub(MID, BD)

    r = poly_shift(AC, k)
    r = poly_sum(r, MID)
    r = poly_shift(r, k)
    r = poly_sum(r, BD)

    return r
