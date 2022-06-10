def sweets_calc(heaps):
    start = 0
    end = len(heaps) - 1
    while end - start >= 2:
        min_val = min(heaps[end], heaps[start])
        heaps[end] -= min_val
        heaps[start] -= min_val
        heaps[end - 1] += min_val
        heaps[start + 1] += min_val
        if heaps[end] == 0:
            end -= 1
        if heaps[start] == 0:
            start += 1

    return end + 1 - start, heaps[start:end + 1]


if __name__ == '__main__':
    k = int(input())
    heaps = []
    for i in range(k):
        a_i, n_i = map(int, input().split())
        heaps += [a_i] * n_i
    n, ans = sweets_calc(heaps)
    print(n)
    print(' '.join([str(x) for x in ans]))

    assert sweets_calc([2, 2, 3, 3, 2]) == (2, [11, 1])
    assert sweets_calc([1, 1, 1, 1, 1, 1, 1]) == (1, [7])
    assert sweets_calc([1, 2, 3, 4, 5, 5]) == (2, [15, 5])
