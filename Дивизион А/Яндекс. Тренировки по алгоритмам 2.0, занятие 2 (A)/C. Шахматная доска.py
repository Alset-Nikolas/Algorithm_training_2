def main(dosk):
    res = 0
    for i in range(1, 9, 1):
        for j in range(1, 9, 1):
            if dosk[i][j] == 1:
                max_add = 4
                max_add -= dosk[i - 1][j]
                max_add -= dosk[i + 1][j]
                max_add -= dosk[i ][j + 1]
                max_add -= dosk[i ][j - 1]
                res += max_add
    return res


def pprint():
    for line in dosk:
        for el in line:
            print(el, end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    dosk = [[0 for x_ in range(10)] for x in range(10)]
    for i in range(n):
        x, y = list(map(int, input().split()))
        dosk[y][x] = 1
    res = main(dosk)
    print(res)

