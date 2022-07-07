def f(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    if a < 0:
        a *= -1
        b *= -1
        c *= -1
        d *= -1

    x_start = -2000
    x_end = 2000
    e = 10 ** -5
    while x_end-x_start >= e:
        x_c = (x_start + x_end) / 2
        if f(a, b, c, d, x_c)  > 0:
            x_end = x_c
        else:
            x_start = x_c

    print((x_start+x_end)/2)
