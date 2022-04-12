if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    counter = dict()
    for x in range(n):
        for symvol in input():
            if symvol not in counter:
                counter[symvol] =0
            counter[symvol] += 1
    for x in range(k):
        for symvol in input():
            counter[symvol] -= 1

    res = []
    for kye, val in counter.items():
        res.append(kye*val)
    print(''.join(res))

