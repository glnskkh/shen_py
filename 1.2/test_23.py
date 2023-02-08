"""
Необходимо найти общий элемент трех массивов
(известно, что он есть, массивы неубывают, длинами n, m, l)
Сложность: O(n + m + l)
"""


def test_same():
    assert same([1, 2, 3], [2, 4, 6], [2]) == 2


def same(a: list[int], b: list[int], c: list[int]) -> int:
    i, j, k = 0, 0, 0

    # среди a[i..], b[j..], c[k..] содержится одинаковый элемент

    while not (a[i] == b[j] == c[k]):
        if a[i] < b[j] or a[i] < c[k]:
            i += 1
        if b[j] < a[i] or b[j] < c[k]:
            j += 1
        if c[k] < a[i] or c[k] < b[j]:
            k += 1

    return a[i]
