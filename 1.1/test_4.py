""" Возведем целое число в целую степень за O(logn) """


def test_power():
    assert power(2, 2) == 4
    assert power(12, 2) == 144
    assert power(4, 0) == 1


def power(a: int, n: int):
    k = n
    b = 1
    c = a

    # Инвариант: a ^ n = b * c ^ k
    while k > 0:
        if k % 2 == 0:
            c *= c
            k /= 2
        else:
            b *= c
            k -= 1

    # a ^ n = b * c ^ k, k = 0 => a ^ n = b
    return b
