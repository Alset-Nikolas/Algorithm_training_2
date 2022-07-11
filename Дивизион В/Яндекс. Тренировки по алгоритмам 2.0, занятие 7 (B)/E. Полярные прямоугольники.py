import math



if __name__ == '__main__':
    n = int(input())
    r_min = 0
    r_max = math.inf
    events = []
    for i in range(1, n+ 1):
        r1, r2, p1, p2 = list(map(float, input().split()))
        r_min = max(r_min,r1)
        r_max = min(r_max, r2)
        events.append([p1, -i])
        events.append([p2, i])
    events.sort()

    us = set()
    cnt=0
    for e in events:
        if e[1] < 0:
            cnt += 1
            us.add(abs(e[1]))
        elif e[1] in us:
            cnt -= 1
    ans =0
    for i in range(len(events)):
        ev = events[i]
        if ev[1] < 0:
            cnt += 1
        else:
            cnt -= 1
        if cnt == n:
            if i < len(events) - 1:
                ans += (events[i+1][0]-events[i][0]) * (r_max**2-r_min**2)/2
            else:
                ans += (events[0][0] - events[-1][0] + 2*math.pi) * (r_max ** 2 - r_min ** 2) / 2
    print(ans)