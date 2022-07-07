if __name__ == '__main__':
    n = int(input())
    moment = []
    for i in range(n):
        l, r = map(int, input().split())
        moment.append([l, '1open'])
        moment.append([r, '2close'])
    moment.sort()
    res = 0
    counter = 0
    x_last = None
    for x2, flag in moment:
        if flag == '1open':
            if counter == 0:
                x_last = x2
            counter += 1

        if flag == '2close':
            counter -= 1
            if counter == 0:
                res += x2 - x_last

    print(res)
