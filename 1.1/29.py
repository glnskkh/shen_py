def test_slow_count_solutions():
    assert fast_count_solutions(1) == 1
    assert fast_count_solutions(2) == 3
    assert fast_count_solutions(4) == 4
    assert fast_count_solutions(6) == 8


def fast_count_solutions(n: int):
    k, l = 0, 0

    # Точка 0, l лежит наверху четверти окружности
    while l*l < n:
        l += 1

    s = 0

    # Инвариант:
    # s - число точек под предыдущими k столбцами
    # Точка l, k лежит сверху k столбца
    while l > 0:
        s += l

        k += 1

        while l > 0 and (l-1)*(l-1)+k*k >= n:
            l -= 1

    return s
