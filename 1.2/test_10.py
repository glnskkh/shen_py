""" Необходимо развернуть массив, сложность O(n / 2) """


def test_reverse():
    # (1)
    a1 = [1, 2, 3]
    reverse(a1)
    assert a1 == [3, 2, 1]


def reverse(x: list[int]):
    for i in range(len(x) // 2):
        x[i], x[-i-1] = x[-i-1], x[i]
