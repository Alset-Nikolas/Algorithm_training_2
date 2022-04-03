def main(x, y, z):
    x1 = min(min(z, y), x)
    z1 = max(z, max(x,y))
    y1 = sum([x, y, z]) - x1 - z1
    if x1 == y1 and z1 >= 1970 and x1<=12:
        return 1
    if (x1 <= 12 and y1 <= 12) or z < 1970 or (x1 >12 and y>12):
        return 0
    return 1

if __name__ == '__main__':
    x, y, z = map(int, input().split())
    res = main(x, y, z)
    print(res)
