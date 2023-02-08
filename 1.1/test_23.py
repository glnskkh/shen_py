""" Разложим целое число на простые сомножители за O(sqrt(n)) """


def test_factorize():
    assert [i for i in fast_factorize(12)] == [2, 2, 3]
    assert [i for i in fast_factorize(1000)] == [2, 2, 2, 5, 5, 5]


def fast_factorize(n: int):
    l = 2

    while n != 1:
        if n % l == 0:
            # l | n и нет других делителей, меньших l => l просто
            yield l
            n //= l
        else:
            if l*l > n:
                l = n  # У числа нет простых делителей больше его корня -> проверяем его самого на простоту сразу
            else:
                l += 1
