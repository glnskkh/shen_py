"""
Поиск (бинарный)
Необходимо определить, входит ли элемент в неубывающий массив
Сложность O(logn)
"""


def test_bin_search():
    assert bin_search([0, 1, 2, 3, 4, 5, 6], 4) == 4


def bin_search(list: list[int], x: int) -> int:
    l, r = 0, len(list) - 1

    # x может быть в list[l..r]
    while l < r:
        mid = (l + r) // 2

        if list[mid] == x:
            return mid
        elif list[mid] < x:
            l = mid
        else:  # list[mid] > x
            r = mid

    return -1
