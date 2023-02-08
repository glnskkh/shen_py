""" Необходимо поменять местами значения двух целочисленных переменных без использования посторонних переменных, сложность O(1) для чисел равной длины """


def test_ariphmetic_swap():
    assert ariphmetic_swap(12, 21) == (21, 12)


def ariphmetic_swap(a: float, b: float):
    # Первое значение - a, второе - b

    # a b

    a = a + b
    # a+b a

    b = a - b
    # a+b ((a + b)-b)=a

    a = a - b
    # ((a+b)-a)=b a

    # => a хранит значение b, b хранит значение a

    return (a, b)
