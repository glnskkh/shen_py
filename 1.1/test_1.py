def test_swap():
    assert swap(12, 21) == (21, 12)


def swap(a: float, b: float):
    # Первое значение - то, что храниться в t, второе - в a, третье - в b

    # t a b

    t = a
    # a a b

    a = b
    # a b b

    b = t
    # a b a

    # => a хранит в себе значение b, а b - значение a

    return (a, b)
