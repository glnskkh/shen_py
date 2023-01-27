def test_fast_fib():
    assert fast_fib(0) == 0
    assert fast_fib(1) == 1
    assert fast_fib(2) == 1
    assert fast_fib(3) == 2
    assert fast_fib(7) == 13


def matrix_mult(A: list[list[int]], B: list[list[int]]):
    """Перемножение двух матриц размера 2*2"""
    C = [[0, 0], [0, 0]]

    # По определению перемножения матриц
    C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]

    return C


def matrix_power(A: list[list[int]], n: int):
    """Алгоритм быстрого возведения матрицы в степень"""
    k = n

    # Единичная матрица
    B = [[1, 0], [0, 1]]
    C = A

    # Инвариант: A^n = B*C^k
    while k > 0:
        if k % 2 == 0:
            C = matrix_mult(C, C)
            k /= 2

            # C^k' = (C^2)^(k/2) = C^k
        else:
            B = matrix_mult(B, C)
            k -= 1

            # B*C^k'= B*C*C^(k-1) = B*C^k

    # A^n = B*C^k, k = 0 => A^n = B
    return B


def fast_fib(n: int):
    A = [[1, 1], [1, 0]]

    # Замечание:
    # Рассмотрим произведение матрицы а на строку[a b]
    # Получаем: [a b]*A = [[a + b][a]]
    # Если взять[f(n) f(n-1)]*A = [[f(n)+f(n-1)][f(n)]] = [[f(n+1)][f(n)]]
    # по определению
    # Тогда нам достаточно найти A*n за log(n) шагов
    A = matrix_power(A, n)

    r = A[0][1]

    return r
