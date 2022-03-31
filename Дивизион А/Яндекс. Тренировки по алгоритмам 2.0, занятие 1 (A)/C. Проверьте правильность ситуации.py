def calc_x_0(info):
    n_x = 0
    n_0 = 0
    for line in info:
        for el in line:
            if el == 1:
                n_x += 1
            if el == 2:
                n_0 += 1
    return n_x, n_0


def check_x_or_0(info, param=2):
    '''
    Проверяем на корректную победу

    :param info: поле
    :param param: значение 1-икс, значение 2-ноль
    :return:
    '''
    flag_0_line = False
    flag_0_h = False
    for i in range(3):
        if info[i][0] == info[i][1] == info[i][2] == param:
            flag_0_line = True
        if info[0][i] == info[1][i] == info[2][i] == param:
            flag_0_h = True
    diag_left = bool(info[0][0] == info[1][1] == info[2][2] == param)
    diag_right = bool(info[2][0] == info[1][1] == info[0][2] == param)

    if sum([flag_0_line, flag_0_h, diag_left,diag_right]) <= 2:
        if sum([flag_0_line, flag_0_h, diag_left,diag_right]) != 0:
            return True, "WINNER"
        return True, "NO_WINNER"
    return False, None


def main(info):
    n_x, n_0 = calc_x_0(info)

    flag_x, win_x = check_x_or_0(info, param=1)
    flag_0, win_0 = check_x_or_0(info, param=2)
    if flag_x and flag_0:
        if win_0 == win_x == "WINNER":
            return False

        if win_x == win_0 == "NO_WINNER":
            if n_0 == 4 and n_x == 5:
                return True
            if n_x >= n_0 and n_x-n_0<2:
                return True
        if win_0 == "WINNER" and n_0 == n_x:
            return True
        if win_x == "WINNER" and n_x - 1 == n_0:
            return True

    return False


if __name__ == '__main__':
    info = []
    for i in range(3):
        new_line = list(map(int, input().split()))
        info.append(new_line)
    if main(info):
        print("YES")
    else:
        print("NO")
    assert not main([[1, 1, 1]] * 3)
    assert main([[2, 1, 1], [1, 1, 2], [2, 2, 1]])
    assert main([[1, 1, 1], [2, 0, 2], [0, 0, 0]])
    assert main([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert not main([[1, 1, 1], [0, 1, 0], [0, 0, 1]])
    assert not main([[1, 1, 1], [2, 1, 0], [2, 1, 2]])
    assert not main([[1, 1, 1], [0, 0, 0], [2, 2, 2]])
    assert not main([[1, 1, 1], [0, 1, 1], [0, 0, 0]])
    assert not main([[1, 1, 1], [2, 1, 1], [2, 2, 2]])
    assert  main([[1, 1, 1], [2, 1, 2], [2, 2, 1]])
    assert not main([[0, 0, 0], [0, 2, 0], [0, 0, 0]])
    assert main([[0, 0, 0], [0, 1, 2], [0, 0, 0]])
    assert main([[0, 0, 0], [1, 1, 2], [0, 0, 0]])
    assert main([[0, 2, 1], [1, 1, 2], [0, 0, 2]])
    assert main([[0, 0, 0]] * 3)
    assert  main([[1, 2, 1], [2, 1, 2], [1, 2, 1]])
    assert not main([[1, 2, 1], [1, 2, 2], [1, 2, 1]])
