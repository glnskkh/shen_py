""" Среди всех чисел 1..n найти в массиве длины n отсутствующее """


def test_missing():
    assert missing([1, 2, 4, 5]) == 3


def missing(a: list[int]) -> int:
    # Из суммы чисел 1,...,n: n(n+1)/2
    return int((len(a) + 1) * (len(a) + 2) / 2) - sum(a)
