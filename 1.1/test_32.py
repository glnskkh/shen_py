""" Определим период ф-ии f: {1..n} -> {1..n}, O(n) вызовов f """


def test_func_period():
    assert func_period(lambda n: (n + 1) % 100) == 100
    assert func_period(lambda n: (n + 2) % 50) == 25


def func_period(f):
    # Инвариант: a = f ^ k(1), b = f ^ 2k(1)
    a = f(1)
    b = f(f(1))

    k = 1

    while a != b:
        a = f(a)
        b = f(f(b))

        k += 1

    # Если a == b, то на предыдущих итерациях не было этого равенства, а раз так, то
    # k - наименьший период функции f
    return k
