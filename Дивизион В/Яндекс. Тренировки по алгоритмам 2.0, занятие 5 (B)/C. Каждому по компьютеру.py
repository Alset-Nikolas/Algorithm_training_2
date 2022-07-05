n, m = map(int, input().split())
x = list(map(int, input().split()))
idx_x = [i for i in range(n)]
y = list(map(int, input().split()))
idx_y = [i for i in range(m)]
x, idx_x = zip(*sorted(zip(x, idx_x)))
y, idx_y = zip(*sorted(zip(y, idx_y)))
res = [0] * n
pointer = 0
k = 0
for i in range(len(x)):
    while pointer < len(y) and y[pointer] <= x[i]:
        pointer += 1
    if pointer == len(y):
        break
    res[idx_x[i]] = idx_y[pointer] + 1
    k += 1
    pointer += 1
print(k)
print(*res)
