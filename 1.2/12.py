# Идея: воспользуемся схемой Горнера

def test_polynom():
    assert polynom(1, [1, -2, 1]) == 0
    assert polynom(0, [0, 1]) == 0
    assert polynom(5, [0, 1]) == 5
    assert polynom(4, [0, 0, 1]) == 16


def polynom(x: float, a: list[float]):
    """
    Вычисляем значения полинома с коэфициентами
    a[n]x^n + ... + a[0] в точке x
    """

    result = 0

    # result = a[i](... (a[n]x + a[n - 1])x) ...) +
    for i in range(len(a)):
        result *= x
        result += a[-i-1]

    return result
