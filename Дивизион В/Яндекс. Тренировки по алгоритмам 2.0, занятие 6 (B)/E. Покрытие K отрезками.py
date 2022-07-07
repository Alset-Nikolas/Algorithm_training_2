def calc_cnt(l, xn):
    cnt = 0
    right = xn[0] - 1
    for x in xn:
        if x > right:
            cnt += 1
            right = x + l
    return cnt

if __name__ == '__main__':
    n,k = map(int, input().split())
    xn = list(map(int, input().split()))
    xn.sort()
    l_min = 0
    l_max = xn[-1] - xn[0]
    while l_min < l_max:
        l = (l_max + l_min)//2
        cnt = calc_cnt(l, xn)
        if cnt <= k:
            l_max= l
        else:
            l_min = l+1
    print(l_min)


