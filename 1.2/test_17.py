"""
Для двух возрастающих многочленов необходимо посчитать число общих членов
длиной n и m
Сложность: O(n + m)
"""


def test_count_intersection():
    assert count_intersection([1, 2, 3, 4], [2, 3, 4, 5]) == 3


def count_intersection(a: list[int], b: list[int]):
    k = 0

    # k - число общий элементов в a[0..i] и b[0..j]

    i, j = 0, 0
    while not (i == len(a) or j == len(b)):
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            k += 1
            i += 1
            j += 1

    # i == len(a) или j == len(b), причем a[i] или b[j]
    # присутствуют в одном из массивов, но отсутствуют в другом

    return k
