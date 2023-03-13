""" Дана матрица n*n, надо для каждого из квадратов размера m*m указать максимум из чисел, лежащих внутри квадрата """


def test_square_maxs():
    x = [
        [1, 2, 3, 4],
        [8, 7, 6, 5],
        [9, 10, 11, 12],
        [16, 15, 14, 13],
    ]

    assert square_maxs(x, 3) == [
        [11, 12],
        [16, 15]
    ]


def line_maxs(a: list[int], m: int) -> list[int]:
    l = [0] * len(a)

    local_m = a[0]
    for i, el in enumerate(a):
        if i % m == 0 or local_m < el:
            local_m = el

        l[i] = local_m

    r = [0] * len(a)

    local_m = a[len(a) - 1]
    for i, el in reversed(list(enumerate(a))):
        if i % m == 0 or local_m < el:
            local_m = el

        r[i] = local_m

    maxs = [0] * (len(a) - m + 1)
    for i in range(len(maxs)):  # i=1,(len(a) - m)
        maxs[i] = max(r[i], l[i + m - 1])

    return maxs


def transpose(a: list[list[int]]) -> list[list[int]]:
    """ Транспонируем прямоугольную матрицу """

    b: list[list[int]] = []

    for i in range(len(a[0])):
        b.append([])

        for j in range(len(a)):
            b[i].append(a[j][i])

    return b


def square_maxs(a: list[list[int]], m: int) -> list[list[int]]:
    lines = list(map(lambda x: line_maxs(x, m), a))
    lines = transpose(lines)

    blocks = list(map(lambda x: line_maxs(x, m), lines))
    blocks = transpose(blocks)

    return blocks
