def test_fast_mult():
    assert fast_mult(12, 12) == 144
    assert fast_mult(11, 11) == 121
    assert fast_mult(3, 4) == 12


def bin_len(a: int):
    length = 0

    while a > 0:
        a >>= 1
        length += 1

    return length


def fast_mult(a: int, b: int) -> int:
    # a = A*2^k + B
    # b = C*2^k + D
    # ab = AC*2^2k + (AD + BC)*2^k + BD
    # Рекурсивно вычислим AC, BD, (A + B)(C + D),
    # AD + BC = (A + B)(C + D) - AC - BD

    k = max(bin_len(a), bin_len(b)) - 1

    if k <= 0:
        return a & b

    A = a >> k
    B = a - (A << k)
    C = b >> k
    D = b - (C << k)

    AC = fast_mult(A, C)
    BD = fast_mult(B, D)
    MID = fast_mult(A + B, C + D) - AC - BD

    return (AC << (2 * k)) + (MID << k) + BD
