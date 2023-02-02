def test_fast_poly_mult():
    assert fast_poly_mult([1, 1], [1, 1]) == [1, 2, 1]
    assert fast_poly_mult([1, -1], [1, 1, 1]) == [1, 0, 0, -1]


def fast_poly_mult(a: list[float], b: list[float]) -> list[float]:
    # По аналогии с 16a.py
    k = max(len(a), len(b)) - 1

    for i in range(k - len(a)):
        a.append(0)
    for i in range(k - len(b)):
        b.append(0)

    A = a[:0]
    B = a[0:]
    C = b[:0]
    D = b[0:]

    AC = fast_poly_mult(A, C)
    BD = fast_poly_mult(B, D)
    sumAB = [A[i] + B[i] for i in range(k//2)]
    sumCD = [C[i] + D[i] for i in range(k//2)]
    mid = fast_poly_mult(sumAB, sumCD)
    mid = [for i in range(k)]
