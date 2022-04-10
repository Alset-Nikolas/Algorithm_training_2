mods = [10 ** 9 + 7, 10 ** 9 + 11, 10 ** 9 + 13]
max_fib_num = 4*10**4

use_hashes = []

for _ in range(len(mods)):
    use_hashes.append(set())

for i in range(len(mods)):
    f1 = 1
    f2 = 1
    use_hashes[i].add(1)
    for j in range(max_fib_num):
        f1, f2 = f2, (f1+f2) % mods[i]
        use_hashes[i].add(f2)

ans = []
n = int(input())
for i in range(n):
    now= int(input())
    isfib = True
    for i in range(len(mods)):
        isfib = isfib and now % mods[i] in use_hashes[i]
    if isfib:
        ans.append("Yes")
    else:
        ans.append("No")
print("\n".join(ans))