"""
Необходимо найти число различных элементов в неубывающем массиве длиной n

Сложность O(n - 1)
"""


def test_count_different():
    # (1)
    assert count_different([1, 2, 3, 3, 4]) == 4


def count_different(x: list[int]):
    "Полагаем, что массив отсортирован по возрастанию"

    count = 1

    # Инвариант: в count число различных элементов в x[0..k+1]
    for k in range(len(x) - 1):
        if x[k] != x[k+1]:
            count += 1

    return count


# def count_different2(x: list[int]):
#     "Полагаем, что массив отсортирован по возрастанию"

#     count = 0

#     # Инвариант: x[k] - элемент, которого еще не было
#     k = 0
#     while k < len(x):
#         count += 1

#         i = k + 1
#         while i < len(x) and x[k] == x[i]:
#             i += 1
#         k = i

#     return k
