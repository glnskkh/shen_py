"""
Необходимо найти индексы элементов (из неубывающих массивов длинами n и m),
сумма которых будет наиболее близка к заданному числу

Сложность: O(n + m) (прошу заметить не nm!!)
"""


def test_closest_sum():
    assert closest_sum([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10) == (4, 4)


def closest_sum(a: list[int], b: list[int], x: int) -> tuple[int, int]:

    # идея: совместим a и массив x - b

    i, j = 0, len(b) - 1
    mi, mj = i, j

    while not (i == len(a) or j == -1):
        if abs(a[i] + b[j] - x) < abs(a[mi] + b[mj] - x):
            mi, mj = i, j

        if a[i] + b[j] < x:
            i += 1
        elif a[i] + b[j] > x:
            j -= 1
        else:  # a[i] + b[j] == x
            break

    return mi, mj
