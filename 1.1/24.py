def test_is_prime():
    assert is_prime(11) == True
    assert is_prime(7) == True
    assert is_prime(1021) == True

    assert is_prime(12) == False
    assert is_prime(1024) == False


def is_prime(a: int):
    # Инвариант: ни одно из чисел меньше k не делит a
    k = 2
    while k*k <= a:
        if a % k == 0:
            return False
        k += 1

    # инвариант, k*k > a => ни одно число до квадратного корня не делит a => a - простое
    return True
