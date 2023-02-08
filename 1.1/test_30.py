""" Деление едицницы на n с точностью pers, O(pers) операций деления """


def test_inversed():
    assert inversed(2, 2) == "0.50"


def inversed(n: int, pers: int):
    res = "0."

    r = 1

    # Алгоритм деления в столбик
    for i in range(pers):
        res += str((10 * r) // n)
        r = (10 * r) % n

    return res
