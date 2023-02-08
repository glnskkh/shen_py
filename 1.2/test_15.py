"""
Необходимо перемножить два многочлена a и b,
O(nm), где n, m - степени многочленов a и b соответственно
"""


def test_polynom_mult():
    assert polynom_mult([1, 1], [1, 1]) == [1, 2, 1]
    assert polynom_mult([1, -1], [1, 1, 1]) == [1, 0, 0, -1]


def polynom_mult(a: list[float], b: list[float]):
    "Перемножим два многочлена f и g с коэфициентами a и b"
    if len(a) < len(b):
        a, b = b, a

    # Коэфициенты произведения
    m: list[float] = []

    # У нас уже есть i элементов в m;
    # Действительные числа, представленные типом float образуют поле =>
    # degh = degf + degg
    for i in range(len(a) + len(b) - 1):
        p = 0

        j = min(i, len(a) - 1)
        while j >= 0 and i-j < len(b):
            p += a[j] * b[i - j]
            j -= 1

        m.append(p)

    return m
