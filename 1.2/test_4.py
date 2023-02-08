""" Ищем максимальный элемент в массиве за O(n) """


def test_max():
    assert max(x=[1, 2, 3, 5, 4]) == 5


def max(x: list[int]):
    m = x[0]

    # Инвариант: m - максимальный элемент из x[0..k]
    for k in range(1, len(x)):
        if x[k] > m:
            m = x[k]

    return m
