"""
Вычисление более сложной функции, по правилам:
f(0) = 13
f(1) = 17
f(2) = 20
f(3) = 30
f(2n) = 43f(n) + 57f(n+1)
f(2n+1) = 91f(n) + 179f(n + 1)

O(log2n) шагов
"""


def test_compute():
    # Простые значения
    assert compute(0) == 13
    assert compute(1) == 17
    assert compute(2) == 20
    assert compute(3) == 30

    # Уже с пересчетом
    assert compute(4) == 43 * compute(2) + 57 * compute(3)
    assert compute(5) == 91 * compute(2) + 179 * compute(3)


def compute(n: int):
    """Рекурсивные вызовы выполняются лишь для базовых случаем, сложность O(logn)"""

    # Базовые случаи
    if n == 0:
        return 13
    if n == 1:
        return 17
    if n == 2:
        return 20
    if n == 3:
        return 30

    # f(n) = a*f(k) + b*f(k+1) + c*f(k+2)
    k = n
    a, b, c = 1, 0, 0

    while k > 2:
        if k % 2 == 0:
            a, b, c = 43 * a + 91 * b, 57 * a + 179 * b + 43 * c, 57 * c
        else:
            a, b, c = 91 * a, 179 * a + 43 * b + 91 * c, 57 * b + 179 * c

        k //= 2

    # с == 0 только в том случае, если n было равно 4,
    # тогда был бы вызов f(n + 2), которого не должно было бы быть
    if c == 0:
        return a * compute(k) + b * compute(k + 1)
    else:
        return a * compute(k) + b * compute(k + 1) + c * compute(k + 2)
