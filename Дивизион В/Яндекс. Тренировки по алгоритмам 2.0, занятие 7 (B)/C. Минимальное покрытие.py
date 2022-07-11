def create_events():
    M = int(input())
    l_i, r_i = map(int, input().split())
    events = []  #
    while not(l_i == 0 and r_i == 0):
        if not( r_i <= 0 or l_i >= M):
            events.append([l_i, r_i])
        l_i, r_i = map(int, input().split())
    events.sort()
    return M, events

def find_max_event(events, start):
    max_len = 0
    ans = []
    for ev in events:
        l, r = ev
        l_i = r - start
        if l_i >= max_len:
            max_len = l_i
            ans = ev
    return ans


if __name__ == '__main__':
    M, events = create_events()
    ans = []
    probe=[]
    start = 0
    end = M
    i=0
    flag = False
    if len(events) == 0:
        flag = True
    while i < len(events):
        l, r = events[i]
        if l <= start:
           probe.append(events[i])
           i += 1
        else:
            if len(probe) == 0:
                flag = True
                break
            else:
                max_len_event = find_max_event(probe, start)
                probe = []
                start = max_len_event[1]
                ans.append(max_len_event)
                if start >= end:
                    break
    if len(probe) != 0:
        max_len_event = find_max_event(probe, start)
        probe = []
        end = max_len_event[1]
        if end >= M:
            ans.append(max_len_event)
        else:
            flag = True
    if flag:
        print('No solution')
    else:
        print(len(ans))
        for l, r in ans:
            print(l, r)
