def test_rev_fact():
    assert 1.0 == rev_fact(0)
    assert 1.0+1.0 == rev_fact(1)
    assert 1.0+1.0+0.5 == rev_fact(2)
    assert 1.0+1.0+0.5+(1/6.0) == rev_fact(3)


def rev_fact(n: int):
    d = 1.0
    sum = 1.0

    # Инвариант sum = 1/0! + ... 1/(k - 1)!
    for k in range(n):
        d /= float(k + 1)
        sum += d

    # Учитывая инвариант и k = n+1 => sum - искомое число
    return sum
