if __name__ == '__main__':
    k = int(input())
    heaps = []
    for i in range(k):
        a_i, n_i = map(int, input().split())
        heaps += [a_i] * n_i
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

    print(end + 1 - start)
    for x in range(start, end+1):
        print(heaps[x], end=' ')
