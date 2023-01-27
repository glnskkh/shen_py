# Идея: у каждого прямоугольника лишь один левый верхний угол
# => будем считать их (черная клетка, под которой и справа от которой тоже черные клетки)
def count_rectangles(field: list[list[int]]):
    count = 0

    for i in range(len(field) - 1):
        for j in range(len(field[i]) - 1):
            isBlack = field[i][j] == 1 and \
                field[i + 1][j] == 1 and field[i][j+1] == 1

            if isBlack:
                count += 1

    return count
