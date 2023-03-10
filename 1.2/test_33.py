"""
Задача о голландском флаге:
Необходимо расположить элементы 0, 1, 2 так, чтобы они разбивали массив по границе

Сложность: O(n)

Возможна для n разбиений, поэтому вложима по характеристическим предикатам, как бинарный поиск изначально был про [0000...01...11], так и здесь может быть 0 - >, 1 - <, 2 - =
"""


def test_divide():
    # (1)
    x = [0, 2, 1, 2, 2, 1]

    divide(x)

    assert x == [0, 1, 1, 2, 2, 2]


def divide(a: list[int]):
    l, m, r = 0, 0, len(a) - 1

    # a[..l] = 0, a[l+1..m] = 1, a[m+1..r] = 2
    while m < r:
        if a[m] == 1:
            m += 1
        elif a[m] == 0:
            a[l], a[m] = a[m], a[l]
            l += 1
            m += 1
        else:  # a[m] == 2:
            a[m], a[r] = a[r], a[m]
            r -= 1
