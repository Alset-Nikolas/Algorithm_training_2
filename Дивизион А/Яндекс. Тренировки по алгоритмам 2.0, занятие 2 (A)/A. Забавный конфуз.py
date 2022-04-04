def main(k, numbers):
    sum_list = sum(numbers)

    n = len(numbers)
    if k == 1:
        p=1
    else:
        p=0.5
        for i in range(2,k):
            p -= 2**(-i)
    new_l = []
    for x in numbers:
        new_l.append((-1)**k*(x-sum_list*p))
    # print(new_l)
    print(int(max(new_l) - min(new_l)))

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    res = main(k, numbers)