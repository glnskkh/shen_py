def test_count_zeroes():
    assert count_zeroes([0, 0, 3, 4, 5, 0, 50]) == 3


def count_zeroes(x: list[int]):
    # Инвариант: c - число нулей в x[0..k]
    c = 0

    for k in range(len(x)):
        if x[k] == 0:
            c += 1

    return c
