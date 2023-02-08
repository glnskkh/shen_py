""" Перевод числа в десятичную систему счисления за O(logn) шагов """


def test_decimal():
    assert decimal(12) == "12"
    assert decimal(341) == "341"
    assert decimal(100000) == "100000"


def decimal(n: int):
    base = 1

    while base*10 < n:
        base *= 10
    # base соответствует старшему разряду числа

    # Инвариант: цифры числа разрядов, больше, чем разрядов у base, напечатаны
    res = ""
    while base > 0:
        res += str(n // base)
        n %= base
        base //= 10

    return res
