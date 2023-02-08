""" Разворот целого числа n за O(logn) шагов """


def test_reverse_decimal():
    assert reverse_decimal(341) == "143"
    assert reverse_decimal(100000) == "000001"


def reverse_decimal(n: int):
    # Инвариант: n символов с конца числа напечатаны
    res = ""
    while n > 0:
        res += str(n % 10)
        n //= 10

    return res
