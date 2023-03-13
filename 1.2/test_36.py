""" Дана матрица A размером n*n и m <= n необходимо для каждого из квадратов  m*m вычислить сумму элементов, стоящих в нем

Сложность: O((n - m + 1)^2)
"""


def test_square():
    x = [
        [1, 2, 3, 4],
        [8, 7, 6, 5],
        [9, 10, 11, 12],
        [16, 15, 14, 13],
    ]

    assert square_sums(x, 3) == [
        [57, 60],
        [96, 93]
    ]


def line_sums(a: list[list[int]], m: int) -> list[list[int]]:
    lines: list[list[int]] = []

    for i in range(len(a)):
        s = sum(a[i][:m])

        lines.append([])

        for j in range(len(a[i]) - m + 1):
            lines[i].append(s)

            if j != len(a[i]) - m:
                s += a[i][j + m] - a[i][j]

    return lines


def transpose(a: list[list[int]]) -> list[list[int]]:
    """ Транспонируем прямоугольную матрицу """

    b: list[list[int]] = []

    for i in range(len(a[0])):
        b.append([])

        for j in range(len(a)):
            b[i].append(a[j][i])

    return b


def square_sums(a: list[list[int]], m: int) -> list[list[int]]:
    # Найдем суммы по блокам длины m
    # Затем, проходя по строкам, будем считать суммы блоков, вычисленных на предыдущих этапах

    lines = line_sums(a, m)
    lines = transpose(lines)

    blocks = line_sums(lines, m)
    blocks = transpose(blocks)

    return blocks
