if __name__ == '__main__':
    all_numbers = list(map(int, input().split()))
    counter = dict()
    no_ans = set()
    for x in all_numbers:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
        if counter[x] > 1:
            no_ans.add(x)
    for x in all_numbers:
        if x not in no_ans:
            print(x, end=' ')



