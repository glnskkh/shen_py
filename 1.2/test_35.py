"""
Дан массив длины n, для каждого из участков длины n необходимо найти максимальный элемент на этом участке

Сложность: O(n)
"""


def test_maxs():
    assert maxs([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def right_maxs(a: list[int], m: int) -> list[int]:
    """ На iтом месте стоит максимум из элементов принажлежащих блоку длины m справа от a[i] """

    r = [0] * len(a)

    local_m = 0
    for i, el in reversed(list(enumerate(a))):
        if i % m == m - 1 or el > local_m:
            local_m = el

        r[i] = local_m

    return r


def left_maxs(a: list[int], m: int) -> list[int]:
    """ На iтом месте стоит максимум из элементов принажлежащих блоку длины m слева от a[i] """

    l = [0] * len(a)

    local_m = 0
    for i, el in enumerate(a):
        if i % m == m - 1 or el > local_m:
            local_m = el

        l[i] = local_m

    return l


def maxs(a: list[int], m: int) -> list[int]:
    right = right_maxs(a, m)
    left = left_maxs(a, m)

    r = [0] * (len(a) - m + 1)

    # Мы знаем масимумы на каждом из блоков длины m
    # теперь мы просто должны заметить, что блок либо разбивается границей блока на два или полностью лежит в нем
    for i, _ in enumerate(r):
        r[i] = max(right[i], left[i + m - 1])

    return r
