"""
Необходимо совместить два неубывающих массива длинами n и m
так, чтобы полученный массив неубывал
Сложность: O(n + m)
"""


def test_merge():
    assert merge([1, 2, 4], [3, 5, 6]) == [1, 2, 3, 4, 5, 6]


def merge(a: list[int], b: list[int]) -> list[int]:
    r = []

    # r - массив слияния, он неубывает,
    # к r[i + j] необходимо прибавить слева слияние a[i..] и b[j..]

    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1

    # Если мы дошли до сюда, то один из массивов закончился,
    # надо просто добавить остаток второго их них к r
    while i < len(a):
        r.append(a[i])
        i += 1

    while j < len(b):
        r.append(b[j])
        j += 1

    return r
