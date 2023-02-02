def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(7) == 13


def fib(n: int):
    a = 0
    b = 1

    # Инвариант:
    # a - член последовательности фиббоначи под номером k,
    # b - следующий за ним член той же последовательности
    for k in range(n):
        b = a + b
        a = b - a

    # a - k-тое число фиббоначи, k = n => k = f(n)
    return a
