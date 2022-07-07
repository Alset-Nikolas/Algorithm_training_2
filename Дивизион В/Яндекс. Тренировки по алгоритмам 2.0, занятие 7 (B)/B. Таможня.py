if __name__ == '__main__':
    n = int(input())
    moment = []
    for i in range(n):
        t, l = map(int, input().split())
        moment.append([t, '2open'])
        moment.append([t+l, '1close'])
    moment.sort()
    n =0
    cnt = 0
    for t, flag in moment:
        if flag == '2open':
           cnt += 1
        else:
            cnt -= 1
        if cnt > n:
            n+=1
    print(n)

