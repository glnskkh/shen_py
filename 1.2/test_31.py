"""
Дан массив a и число b. Необходимо переставить элементы в массиве таким образом, чтобы слева от некоторой границы стояли числа меншие b, а справа - большие

Сложность: O(n)
"""


def test_divide():
    # (1)
    x = [5, 4, 3, 2, 1]
    divide(x, 3)

    for i in x[:1]:
        assert i < 3

    for i in x[4:]:
        assert i > 3


def divide(a: list[int], b: int):
    # a[..i] меньше b и a[j..] больше b

    i, j = 0, len(a) - 1

    while True:
        while i < j and a[i] < b:
            i += 1
        while i < j and a[j] >= b:
            j -= 1

        if not (i < j):
            break

        a[i], a[j] = a[j], a[i]
