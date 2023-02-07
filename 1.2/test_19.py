def test_unincreasing_count():
    assert unincreasing_count([5, 4, 3, 2, 1, 1], [4, 3, 1]) == 3


def unincreasing_count(a: list[int], b: list[int]) -> int:
    k = 0

    i, j = 0, 0

    # Точно так же, как и в предыдущей задаче

    while not (i == len(a) or j == len(b)):
        if a[i] > b[j]:
            i += 1
        elif a[i] < b[j]:
            j += 1
        else:  # a[i] == b[j]
            t = a[i]
            k += 1

            while i < len(a) and a[i] == t:
                i += 1

            while j < len(b) and b[j] == t:
                j += 1

    return k
