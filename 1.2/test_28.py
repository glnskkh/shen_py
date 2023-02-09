"""
Необходимо найти элемент в двумерном массиве, упорядоченном по неубыванию
по строкам и столбцам
Сложность: O(nm), где n*m - размерность массива
"""


def test_bin_search():
    x = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]

    assert bin_search(x, 4) == (1, 1)
    assert bin_search(x, 5) == (1, 2)
    assert bin_search(x, 8) == (2, 2)
    assert bin_search(x, 10) == (-1, -1)


def bin_search(list: list[list[int]], x: int) -> tuple[int, int]:
    i, j = len(list) - 1, 0

    # x может содержаться в list[..i][j..]
    while i >= 0 and j < len(list[0]):
        if list[i][j] == x:
            return i, j
        elif list[i][j] > x:
            i -= 1
        else:  # list[i][j] < x
            j += 1

    # list[..i][j..] пусто
    return -1, -1
