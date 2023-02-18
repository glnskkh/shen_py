"""
Пусть нам дана некоторая подстановка, записаная видом
1 -> a[0], 2 -> a[1], ...

Необходимо определить четность подстановки за O(n)
"""


def test_is_even():
    assert is_even([]) == True
    assert is_even([1, 2, 3]) == True
    assert is_even([1, 3, 2]) == False


def count_cycles(permutation: list[int]) -> int:
    i: int = 0
    k: int = 0

    # Уже посчитаны те циклы, чьи первые элементы находятся среди первых i элементов массива
    while i < len(permutation):
        # Если элемент меньше 0, то мы уже посчитали цикл, в который он входит
        if permutation[i] < 0:
            i += 1
            continue

        # Проходим по циклу и меняем все элементы на противоположные
        k += 1
        j: int = i
        while permutation[j] > 0:
            l = j

            j = permutation[j] - 1
            permutation[l] *= -1

        i += 1

    # i == len(perm) -> Все циклы посчитаны
    return k


def is_even(permutation: list[int]) -> bool:
    N = len(permutation)
    cycles = count_cycles(permutation)

    # Четность подстановки зависит от числa l1-1 + l2-1 + ... + lk-1 =
    # n - k, где n=l1+l2+... - длина подстановки, l1...lk - длины циклов,
    # k - число циклов
    return (N - cycles) % 2 == 0
