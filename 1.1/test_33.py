"""
Вычислим значения f, если известно, что
f(0)=0
f(1)=1
f(2n)=f(n)
f(2n+1)=f(n)+f(n+1)

О(log2(n)) шагов
"""


def test_compute():
    assert compute(0) == 0
    assert compute(1) == 1
    assert compute(4) == 1
    assert compute(5) == 3


def compute(n: int):
    # Идея:
    # Давайте будем хранить f(n) = a*f(k) + b*f(k+1)

    k = n
    a, b = 1, 0

    while k > 0:
        if k % 2 == 0:
            a += b
            k //= 2
        else:
            b += a
            k //= 2

    # a*f(0) + b*f(1) = b*f(1) = b =>
    return b
