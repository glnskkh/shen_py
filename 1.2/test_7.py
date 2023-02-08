""" Как и предыдущая задача, просто необходимо сортировать за O(nlogn) шагов  (сделано при помощи сортировки слиянием)
Сложность O(nlogn + n - 1)
"""


def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]


def test_merge_sort():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_count_different():
    assert count_different([1, 2, 3, 4, 4]) == 4
    assert count_different([1, 1, 1]) == 1


def merge(a: list[int], b: list[int]):
    x = [0] * (len(a) + len(b))

    i, j, k = 0, 0, 0
    while k < len(a) + len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                x[k] = a[i]
                i += 1
            else:
                x[k] = b[j]
                j += 1
        elif i < len(a):
            x[k] = a[i]
            i += 1
        elif j < len(b):
            x[k] = b[j]
            j += 1

        k += 1

    return x


def merge_sort(x: list[int]):
    "Сортировка слиянием: Средний случай O(nlogn)"
    if len(x) <= 1:
        return x

    left = x[:len(x) // 2]
    right = x[len(x) // 2:]

    return merge(merge_sort(left), merge_sort(right))


def count_different(x: list[int]):
    # Сведем задачу к предыдущей - отсортируем,
    # а потом посчитаем число различых элементов
    x = merge_sort(x)

    count = 1
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:
            count += 1

    return count
