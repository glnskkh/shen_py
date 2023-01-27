def test_count_different():
    # (1)
    assert count_different([1, 2, 3, 3, 4], 10) == 4


# Идея: сортировка подсчетом (значения 0-k)
def count_different(x: list[int], k: int):
    counts = [0] * k

    count = 0
    for el in x:
        if counts[el] == 0:
            counts[el] += 1
            count += 1

    return count
