"""
Необходимо посчитать число одинаковых членов в двух неубывающих массивах
длин n и m
Сложность: O(n + m)
"""


def test_count_undecreacing():
    assert count_undecreacing([1, 1, 2, 3, 4], [1, 2, 4]) == 3


def count_undecreacing(a: list[int], b: list[int]) -> int:
    k = 0

    # k - число одинаковых элементов в a[0..i] и b[0..j]
    # a[i], b[j] - элементы, которые еще не встречалось

    i, j = 0, 0

    while not (i == len(a) or j == len(b)):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            k += 1
            t = a[i]

            # просто пропускаем все элементы, равные данному

            while i < len(a) and a[i] == t:
                i += 1

            while j < len(b) and b[j] == t:
                j += 1

    return k
