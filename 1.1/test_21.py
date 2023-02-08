""" Генерируем квадраты всех целых чисел до n за O(1) умножений """


def test_squares():
    assert [i for i in squares(4)] == [0, 1, 4, 9, 16]


def squares(n: int):
    s = 0

    # Инвариант:
    # s = k ^ 2
    # 0 1 4 ... k-1 возвращены
    for k in range(n + 1):
        yield s
        s += k + k + 1

    # Учитывая инвариант, квадраты всех чисел до n возвращены
