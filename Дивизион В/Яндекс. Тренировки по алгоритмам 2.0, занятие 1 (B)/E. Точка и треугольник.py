def calc_dist(A, B):
    x1, y1 = A
    x2, y2 = B
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def main(d, coords):
    x, y = coords
    if x >= 0 and y >= 0:
        if y+x <= d:
            return 0
    A = (0, 0)
    B = (d, 0)
    C = (0, d)
    d1 = calc_dist(coords, A)
    d2 = calc_dist(coords, B)
    d3 = calc_dist(coords, C)
    if d1 <= min(d2,d3):
        return 1
    elif d2 <= min(d1,d3):
        return 2
    else:
        return 3

if __name__ == '__main__':
    d = int(input())
    coords = list(map(int, input().split()))
    res = main(d, coords)
    print(res)
