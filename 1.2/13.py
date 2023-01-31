# Схема Горнера + вычисление производной в точке
# на каждом шаге мы получаем Pl(x) = x * P(x) + a,
# Pl1'(x) = (x * P(x) + a)' = xP'(x) + P(x)

def test_compute():
    assert compute(1, [1, -2, 1]) == (0, 0)
    assert compute(0, [1, -2, 1]) == (1, -2)


def compute(x: float, a: list[float]):
    """Вычисляем значения полинома с коэфициентами a[..] в точке x,
    и его производную в этой точке"""

    r, d = 0, 0

    # r есть значение полинома из коэфициентов до с,
    # d - производная этого многочлена
    for c in reversed(a):
        d = d * x + r
        r = r * x + c

    return r, d
