""" Сложим два целых числа a и b за O(b) инкрементов """


def test_sum():
    assert summ(2, 2) == 4
    assert summ(1, 3) == 4
    assert summ(0, 0) == 0
    assert summ(44, 32) == 76


def summ(a: int, b: int):
    r = a

    # Инвариант: r = a + k
    for k in range(b):
        r += 1

    # r = a + k, k = b => r = a + b
    return r
