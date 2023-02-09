"""
Необходимо найти общий элемент всех подмассивов
двумерного массива размером n*m
Сложность: O(nm)
"""


def test_find():
    assert find([[1, 2, 3], [1, 2, 3], [1, 4, 5]]) == 1


def find(list: list[list[int]]) -> int:
    indecies = [0] * len(list)

    while True:
        # Сдвигаем индексы, пока они меньше, чем элемент в первом массиве

        for i in range(1, len(indecies)):
            while list[i][indecies[i]] < list[0][indecies[0]]:
                indecies[i] += 1

        # Проверяем, совпадают ли они
        found = True
        for i in range(1, len(indecies)):
            found = found and list[i][indecies[i]] == list[0][0]

        if not found:
            indecies[0] += 1
        else:
            break

    # Возвращаем найденный элемент
    return list[0][indecies[0]]
