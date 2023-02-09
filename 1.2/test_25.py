"""
Необходимо найти общий элемент всех подмассивов
двумерного массива размером n*m
Сложность: O((n^2)*m)
"""


def test_find():
    assert find([[0, 1, 2, 3], [1, 2, 3], [1, 5, 6]]) == 1


def find(list: list[list[int]]) -> int:
    indecies = [0] * len(list)

    found = False

    while not found:
        # Сдвигаем все индексы так, чтобы ни один из элементов не был меньше другого
        for i in range(len(indecies)):
            for j in range(len(indecies)):
                if list[i][indecies[i]] < list[j][indecies[j]]:
                    indecies[i] += 1

        # Проверяем, совпали ли элементы
        found = True
        for i in range(1, len(indecies)):
            found = found and list[0][indecies[0]] == list[i][indecies[i]]

    # Элементы совпали -> возвращаем найденый элемент
    return list[0][indecies[0]]
