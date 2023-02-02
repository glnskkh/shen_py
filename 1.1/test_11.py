def test_slow_rev_fact():
    assert 1.0 == slow_rev_fact(0)
    assert 1.0+1.0 == slow_rev_fact(1)
    assert 1.0+1.0+0.5 == slow_rev_fact(2)
    assert 1.0+1.0+0.5+(1/6.0) == slow_rev_fact(3)


def fact(n: int):
    "Стандартная реализация вычисления факториала за O(n)"
    p: int = 1

    for k in range(2, n + 1):
        p *= k

    return p


def slow_rev_fact(n: int):
    "Сложность: O(n^2)"
    sum: float = 0

    # sum = 1/0! + 1/1! + ... + 1/(k - 1)!
    for k in range(n + 1):
        sum += 1 / fact(k)

    # k = n + 1 =>
    return sum
