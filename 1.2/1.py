def test_zeroed():
    assert zeroed(5) == [0, 0, 0, 0, 0]


def zeroed(n: int):
    x = []

    # Инвариант: x[0..k] - нули
    for k in range(n):
        x.append(0)

    # Инвариант, k = n => условие задачи выполнено
    return x
