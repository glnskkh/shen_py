""" Копируем массив src в dest за O(min(|src|, |dest|)) """


def test_copy():
    # (1)
    src1 = [0, 0, 0]
    dest1 = [1, 2, 3]

    copy(src1, dest1)

    assert dest1 == [0, 0, 0]


def copy(src: list[int], dest: list[int]):
    # Инвариант: dest[0..k] скопирован в src[0..k]
    for k in range(min(len(src), len(dest))):
        dest[k] = src[k]
