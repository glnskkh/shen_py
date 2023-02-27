"""
Необходимо разделить массив a на три части: элементы, меньшие b, равные, большие

Сложность: O(n)
"""


def test_divide():
    x = [5, 4, 3, 2, 1, 3]

    divide(x, 3)

    assert x[0] < 3
    assert x[1] < 3

    assert x[2] == 3
    assert x[3] == 3

    assert x[4] > 3
    assert x[5] > 3


def divide(a: list[int], b: int):
    l, m, r = 0, 0, len(a) - 1

    # a[..l] < b, a[l..m] == b, a[..r] > b
    while m < r:
        if a[m + 1] == b:
            m += 1
        elif a[m + 1] > b:
            a[r], a[m + 1] = a[m + 1], a[r]
            r -= 1
        else:  # a[m + 1] < b
            a[l], a[m + 1] = a[m + 1], a[l]
            l += 1
            m += 1
