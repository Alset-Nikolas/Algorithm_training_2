if __name__ == '__main__':
    n,q = list(map(int, input().split()))
    mass = list(map(int, input().split()))
    pref_sum = [0] * (n+1)
    for i in range(n):
        pref_sum[i+1] = pref_sum[i] + mass[i]
    for i in range(q):
        l, r = map(int, input().split())
        print(pref_sum[r] - pref_sum[l-1])