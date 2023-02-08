"""
Считаем число различных элементов в неотсортированном массиве
сначала сортировка выбором, затем как в предыдущей задаче
Сложность O(n^2 + n - 1)
"""


def test_count_different():
    assert count_different([1, 2, 3, 4, 4]) == 4
    assert count_different([1, 1, 1]) == 1


def test_selection_sort():
    # (1)
    x = [5, 4, 3, 2, 1]
    selection_sort(x)

    assert x == [1, 2, 3, 4, 5]


def selection_sort(x: list[int]):
    "Худший вариант: O(n^2)"

    def _inner_sort(n: int):
        # x[n..len] отсортированы

        if n <= 1:
            return

        m = 0
        for k in range(1, n):
            if x[k] > x[m]:
                m = k

        x[n - 1], x[m] = x[m], x[n - 1]

        _inner_sort(n - 1)

    _inner_sort(len(x))

    return x


def count_different(x: list[int]):
    # Сведем задачу к предыдущей - отсортируем,
    # а потом посчитаем число различых элементов
    selection_sort(x)

    count = 1
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:
            count += 1

    return count
