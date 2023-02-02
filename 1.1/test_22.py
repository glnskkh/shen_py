def test_factorize():
    assert [i for i in factorize(12)] == [2, 2, 3]
    assert [i for i in factorize(1000)] == [2, 2, 2, 5, 5, 5]


def factorize(n: int):
    k = 2

    # Инвариант: все простые числа, входящие в состав числа n, возвращены
    while n > 1:
        while n % k != 0:
            k += 1

        # k | n, k - наименьшее из тех, что делит n => k простое
        yield k
        n //= k
