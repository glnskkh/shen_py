def test_dull_squares():
    assert [i for i in dull_squares(4)] == [0, 1, 4, 9, 16]


def dull_squares(n: int):
    # Инвариант 0, 1, 4, ..., k ^ 2 возвращены
    for k in range(n + 1):
        yield k * k

    # Учитывая инвариант, все квадраты всех чисел до n возвращены
