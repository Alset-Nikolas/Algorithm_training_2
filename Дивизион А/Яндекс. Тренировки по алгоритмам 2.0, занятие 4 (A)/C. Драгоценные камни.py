
if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    text = input()
    first = set()
    second = set()
    back_counter = dict()
    for i in range(k):
        first_,second_ =  input()
        if second_ not in back_counter:
            back_counter[second_] = []
        back_counter[second_].append(first_)
        first.add(first_)
        second.add(second_)
    counter = dict()
    res = 0
    for el in text:
        if el in second:
            for first_i in back_counter[el]:
                if first_i in counter:
                    res += counter[first_i]
        if el in first:
            if el not in counter:
                counter[el] = 0
            counter[el] += 1

    print(res)



