from math import ceil, floor
if __name__ == '__main__':
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, r = list(map(int, input().split()))

    res = 0
    for y in range(max(y1, y3 - r), min(y2, y3 + r)+1):
        dx = (r**2-(y-y3)**2)**0.5
        x_min = max(x1, ceil(x3-dx))
        x_max = min(x2, floor(x3 + dx))
        if x_max >= x_min:
            res += x_max - x_min + 1
    print(res)
