def test_div_mod():
    assert div_mod(12, 5) == (2, 2)
    assert div_mod(33, 2) == (16, 1)


def div_mod(a: int, b: int):
    rem = a
    div = 0

    # Инвариант: a = div * b + rem
    while not rem < b:
        rem -= b
        div += 1

    # Так как a = div*b + rem, rem < b => div - частное от деления, rem - остаток
    return div, rem
