
if __name__ == '__main__':
    n = int(input())
    mass = list(map(int, input().split()))
    pref_sum = [0] * (n + 1)
    min_val = 0
    ans = None
    for i in range(n):
        pref_sum[i + 1] = pref_sum[i] + mass[i]
        if pref_sum[i+1] > min_val:
            if ans is None:
                ans = pref_sum[i+1] - min_val
            else:
                ans = max(ans, pref_sum[i+1] - min_val)
        else:
            min_val = pref_sum[i+1]
    if ans is None:
        print(mass[0])
    else:
        print(ans)
