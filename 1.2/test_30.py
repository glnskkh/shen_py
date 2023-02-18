"""
Пусть нам дана некоторая подстановка, записаная видом
1 -> a[0], 2 -> a[1], ...

Необходимо определить четность подстановки за O(n)
"""


def test_is_even():
    assert is_even([]) == True
    assert is_even([1, 2, 3]) == True
    assert is_even([1, 3, 2]) == True


def count_cycles(a: list[int]):
    k = 0
    i = 0
    while i < len(a):
        if a[i] < 0:
            i += 1
            continue

        k += 1
        j = a[i] - 1

        while a[j] != a[i]:
            j = a[j] - 1

    return k


def is_even(a: list[int]) -> bool:
    # Для начала посчитаем k - число циклов в a

    return (len(a) - count_cycles(a)) % 2 == 0
