def test_intersection():
    assert intersection([1, 2, 3, 4, 5], [2, 4, 5, 6]) == [2, 4, 5]


def intersection(a: list[int], b: list[int]) -> list[int]:
    r: list[int] = []

    # искомый список - r и приписать пересечение a[i..] с b[j..]

    i, j = 0, 0

    while not (i == len(a) or j == len(b)):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:  # a[i] == b[j]
            r.append(a[i])
            i += 1
            j += 1

    # мы дошли до конца одного из массивов, следовательно, в нем уже не
    # найдется элементов, которые могут присутствовать в другом массиве, ведь
    # в нем вообще нет элементов
    return r