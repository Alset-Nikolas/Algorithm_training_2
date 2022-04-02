if __name__ == '__main__':
    p = int(input())
    a = p //3
    b = (p-a)//2
    c = p-a-b
    if a+b > c:
        print(a, b, c)
        if p % 2 == 0:
            e = 2
        else:
            e = 1
        d = (p-e)//2
        f = p-d-e
        print(e, d, f)
    else:
        print(-1)