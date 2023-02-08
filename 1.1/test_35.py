""" Поделим a на b за O(log2n) шагов """


def test_division():
    assert division(12, 5) == (2, 2)
    assert division(12, 13) == (0, 12)
    assert division(25, 2) == (12, 1)


def division(a: int, b: int):
    """Возвращает значение-пару: (частное, остаток),
    сложность O(logn) в терминах сложений,
    алгоритм деления двоичных чисел в столбик"""

    b1 = b
    while b1 <= a:
        b1 *= 2

    q, r = 0, a

    while b1 != b:
        b1 //= 2
        q *= 2

        if not r < b1:
            r -= b1
            q += 1

    return (q, r)
