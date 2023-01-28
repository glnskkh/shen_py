# Часть (a)

def test_is_gaussian_prime():
    # Составные
    assert is_gaussian_prime(complex(2, 0)) == False
    assert is_gaussian_prime(complex(4, 2)) == False

    # Простые
    assert is_gaussian_prime(complex(1, 1)) == True
    assert is_gaussian_prime(complex(1, 2)) == True
    assert is_gaussian_prime(complex(-4, 11)) == True


def is_prime(n: int):
    from math import sqrt

    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False

    # Если мы не вернулись из цикла, то у числа не делителей до sqrt(n)
    # => n - простое
    return True


def is_gaussian_prime(c: complex):
    "По критерию Гаусса:"
    first_rule = (c.real == 0 and c.imag % 4 == 3) or (
        c.imag == 0 and c.real % 4 == 3)

    second_rule = c.real != 0 and c.imag != 0 and is_prime(int(abs(c)))

    return first_rule or second_rule

# Часть (б)


def test_factorize_gaussian():
    # Составные
    assert len([i for i in factorize_gaussian(2, 0)]) == 2

    # Простые
    assert len([i for i in factorize_gaussian(-4, 11)]) == 1


def factorize_gaussian(c: complex):
    # Перебераем потенциальные делители c,
    # пока c по модулю больше одного
    for i in range(1, int(abs(c))):
        for j in range(1, int(abs(c))):
            d = complex(i, j)
            m = int(abs(c))

            # В последующих строках мы делим с на d, если это возможно
            a = (c.real*d.real + c.imag*d.imag)
            b = (c.imag*d.real - c.real*d.imag)

            if a % m == 0 and b % m == 0:
                c = complex(a // m, b // m)
                yield d

    # Если после этого с по модулю больше 1,
    # то перед нами еще одно простое число
    if int(abs(c)) >= 1:
        yield c
