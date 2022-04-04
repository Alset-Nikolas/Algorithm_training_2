'''
Очень долго, но работает :)

'''
import math


def calc_d(mass, x):
    d = 0
    for x_ in mass:
        d += abs(x - x_)
    return d


def main(homes_cords):
    min_d = math.inf
    res = None
    for x in homes_cords:
        new_d = calc_d(homes_cords, x)
        if new_d < min_d:
            res = x
            min_d = new_d

    return res


if __name__ == '__main__':
    n = int(input())
    homes_cords = list(map(int, input().split()))
    res = main(homes_cords)
    print(res)
