def test_find_equal():
    assert find_equal([1, 2, 3], [2, 3, 4], [2, 4, 5]) == 1
    assert find_equal([1, 2, 3], [2, 3, 4], [3, 4, 5]) == 2
    assert find_equal([1, 2, 3], [2, 3, 4], [0, 4, 5]) == -1


def find_equal(a: list[int], b: list[int], c: list[int]) -> int:
    # Среди a[i..], b[j..], c[k..] содержиться общий элемент

    i, j, k = 0, 0, 0

    while not (i == len(a) or j == len(b) or k == len(c)):
        if a[i] < b[j] or a[i] < c[k]:
            i += 1
        elif b[j] < a[i] or b[j] < c[k]:
            j += 1
        elif c[k] < a[i] or c[k] < b[j]:
            k += 1
        else:
            break

    # мы достигли конца, а общего элемента так и не нашли -> его не было
    # иначе - был, вернем его индекс в первом массиве
    if i == len(a) or j == len(b) or k == len(c):
        return -1
    else:
        return i
