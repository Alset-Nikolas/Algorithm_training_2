def calc_dist_x2(A, B):
    a_x, a_y = A
    b_x, b_y = B
    return (a_x - b_x) ** 2 + (a_y - b_y) ** 2


def main(A, B, C, D):
    cords = [A, B, C, D]
    cords.sort()
    A = a_x, a_y = cords[0]
    B = b_x, b_y = cords[1]
    C = c_x, c_y = cords[2]
    D = d_x, d_y = cords[3]
    L_AB = calc_dist_x2(A, B)
    L_CD = calc_dist_x2(C, D)
    L_BD = calc_dist_x2(B, D)
    L_AC = calc_dist_x2(A, C)
    if L_AB == L_CD != 0 and L_BD == L_AC != 0:
        if (b_y - a_y) * (d_x - c_x) == (d_y - c_y) * (b_x - a_x) and (c_y - a_y) * (d_x - b_x) == (d_y - b_y) * (
                c_x - a_x):
            return True
    return False


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        numbers = list(map(int, input().split()))
        coords = []
        for i in range(0, len(numbers), 2):
            coords.append(numbers[i:i + 2])
        if main(*coords):
            print("YES")
        else:
            print("NO")

    assert main(*[[1, 1], [4, 2], [3, 0], [2, 3]])
    assert not main(*[[1, 1], [5, 2], [2, 3], [3, 0]])
    assert main(*[[0, 0], [5, 1], [6, 3], [1, 2]])
