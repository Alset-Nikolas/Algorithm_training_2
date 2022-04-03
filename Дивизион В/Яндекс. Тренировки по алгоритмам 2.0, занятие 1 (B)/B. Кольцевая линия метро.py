def main(n, i, j):
    if j > i:
        return min((j-i)-1, (n-j+i)-1)
    return min((i - j) - 1, (n - i + j) - 1)

if __name__ == '__main__':
    n, i, j = map(int, input().split())
    res = main(n, i, j)
    print(res)