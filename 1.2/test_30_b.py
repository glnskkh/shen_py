"""
Необходимо поменять подстановку a на обратную ей без использования дополнительных массивов

Сложность O(n)
"""


def test_inverse():
    # (1)
    x = [1, 2, 3]
    y = inverse(x)

    assert y == [1, 2, 3]

    # (2)
    x = [4, 2, 1, 3]
    y = inverse(x)

    assert y == [3, 2, 4, 1]

    # (3)
    x = [1, 3, 2]
    y = inverse(x)

    assert y == [1, 3, 2]


def inverse(a: list[int]) -> list[int]:
    # Будем менять по циклам (сдвиг цикла на одну позицию влево)

    # все циклы, чьи первые элементы раснаходятся в a[..i], заменены на обратные и умножены на -1
    i = 0

    while i < len(a):
        if a[i] < 0:  # Этот элемент уже инвертирован
            i += 1
            continue

        current = i
        next = a[current] - 1

        # все обработанные элементы отмечены минусом
        # обрабатываем все элементы кроме циклов длина 1 и 2
        while next != i and not (current == i and abs(a[next]) - 1 == i):
            last = current
            current = next
            next = a[current] - 1

            a[current] *= -1

            a[last], a[current] = a[current], a[last]

        a[current] *= -1

        i += 1

    # Инвертируем все элементы
    for i in range(len(a)):
        a[i] *= -1

    return a
