def read_info():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    events = []
    for i in range(m):
        l, r = map(int, input().split())
        events.append([l, 1, i])
        events.append([r, 3, i])
    for ai in a:
        events.append([ai, 2, None])
    events.sort()
    return m, events


if __name__ == '__main__':
    m, events = read_info()
    now_l = set()
    ans = [0] * m
    cats = 0
    for ev in events:
        val, flag, i = ev
        if flag == 1:
            now_l.add(i)
            ans[i] = cats
        elif flag == 2:
            cats += 1
        else:
            now_l.remove(i)
            ans[i] = cats - ans[i]
    for ans_i in ans:
        print(ans_i)
