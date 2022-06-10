if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x = [(x_i, i) for i, x_i in enumerate(x)]
    y = list(map(int, input().split()))
    y = [(y_i, j) for j, y_i in enumerate(y)]
    x.sort(key=lambda x: x[0])
    y.sort(key=lambda x: x[0])
    p = 0
    j_sort = 0
    ans = []
    print(y)
    for x_i_sort, i_real in x:
        print('x_i_sort, i_real', x_i_sort, i_real)
        while j_sort < len(y):
            y_j, j_real = y[j_sort]
            if x_i_sort + 1 <= y_j:
                print('y_j, j_sort', y_j, j_sort)
                ans.append(j_real + 1)
                p += 1
                break
            j_sort += 1
    ans += [0] * (len(x) - len(ans))
    print(p)
    print(*ans)
