if __name__ == '__main__':
    n = input()
    info = dict()
    elemnts = set()
    for x in input():
        if x not in info:
            info[x] = 0
        info[x] += 1
        elemnts.add(x)
    ans = []
    center = None
    for x in sorted(list(elemnts)):
        if info[x] % 2 == 0 :
            ans+=x*(info[x]//2)
        else:
            if info[x] // 2 > 0:
                ans += x * (info[x] // 2)
            if center is None and info[x] % 2 != 0:
                center = x
    print("".join(ans)+"".join(ans[::-1]) if center is None else "".join(ans)+center+"".join(ans[::-1]))