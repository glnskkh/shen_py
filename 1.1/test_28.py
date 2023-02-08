""" Поиск целых решений уравнения x^2 + y^2 < n за O(n^2) """


def test_slow_count_solutions():
    assert slow_count_solutions(1) == 1
    assert slow_count_solutions(2) == 3
    assert slow_count_solutions(4) == 4
    assert slow_count_solutions(6) == 8


def slow_count_solutions(n: int):
    count = 0

    # Перебор всех подходящий решений
    k = 0
    while k*k < n:
        l = 0
        while l*l+k*k < n:
            count += 1
            l += 1

        k += 1

    return count
