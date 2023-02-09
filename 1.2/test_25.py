""" Необходимо найти число, присутствующее во всех неубывающих подмассивах массива (обобщение 24й задачи),
Сложность O(n^3 + n^2), где n - число подмассивов
"""


def test_find():
    assert find([[0, 1, 2, 3], [1, 2, 3], [1, 5, 6]]) == 1


def find(list: list[list[int]]) -> int:
    indecies = [0] * len(list)

    found = False

    while not found:
        for i in range(len(indecies)):
            for j in range(len(indecies)):
                if list[i][indecies[i]] < list[j][indecies[j]]:
                    indecies[i] += 1

        found = True
        for i in range(1, len(indecies)):
            found = found and list[0][indecies[0]] == list[i][indecies[i]]

    return list[0][indecies[0]]
