if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    res = set()
    for i in range(k):
        a_i, b_i = list(map(int, input().split()))
        j = 0
        new_x = a_i
        while new_x <= n:
            if new_x % 7 != 6 and new_x % 7 != 0:
                res.add(new_x)
            j += 1
            new_x = a_i + j * b_i


    print(len(res))
