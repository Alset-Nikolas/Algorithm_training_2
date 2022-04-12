if __name__ == '__main__':
    num1 = input()
    num2 = input()
    counter1 = dict()
    all_numbers1 = set()
    counter2 = dict()
    all_numbers2 = set()

    for t in num1:
        if t not in counter1:
            counter1[t] = 0
        counter1[t] += 1
        all_numbers1.add(t)

    for t in num2:
        if t not in counter2:
            counter2[t] = 0
        counter2[t] += 1
        all_numbers2.add(t)

    all_num = list(all_numbers1 & all_numbers2)
    all_num.sort(reverse=True)
    if len(all_num) != 0:
        res = []
        for x in all_num:
            res.append(x*min(counter1[x], counter2[x]))
        ans = "".join(res)
        if int(ans)==0:
            print(0)
        else:
            print(ans)

    else:
        print(-1)