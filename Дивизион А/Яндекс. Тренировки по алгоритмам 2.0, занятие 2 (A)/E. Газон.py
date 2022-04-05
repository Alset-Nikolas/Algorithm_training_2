def rectangle(x1, y1, x2, y2):
    ''' [y_max, x_max, y_min, x_min]    '''
    return [max(y1, y2), max(x1, x2), min(y1, y2), min(x1, x2)]


def cross(short_rectangle, wet_rectangle):
    y_max_1, x_max_1, y_min_1, x_min_1 = short_rectangle
    y_max_2, x_max_2, y_min_2, x_min_2 = wet_rectangle
    return [min(y_max_1, y_max_2), min(x_max_2, x_max_1), max(y_min_1, y_min_2), max(x_min_1, x_min_2)]


if __name__ == '__main__':
    x1, y1, x2, y2 = list(map(int, input().split()))
    short_rectangle = rectangle(x1, y1, x2, y2)
    x3, y3, r = list(map(int, input().split()))

    wet_rectangle = rectangle(x3 - r, y3 - r , x3 + r , y3 + r)
    res_rec = cross(short_rectangle, wet_rectangle)
    y_max, x_max, y_min, x_min = res_rec
    res = 0

    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if (x-x3)**2 + (y-y3)**2<=r**2:
                res += 1
    print(res)
