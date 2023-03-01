"""
По массиву a длины n и m <= n необходимо вычислить суммы всех подотрезков длины m

Сложность: O(n)
"""


def test_sums():
    assert sums([1, 2, 3, 4, 5], 3) == [6, 9, 12]


def sums(a: list[int], m: int) -> list[int]:
    s = 0

    for i in range(m):
        s += a[i]

    r = [s]

    # s' = s - a[i] + a[i + m]
    for i in range(len(a) - m):
        s += a[i + m] - a[i]
        r.append(s)

    return r
