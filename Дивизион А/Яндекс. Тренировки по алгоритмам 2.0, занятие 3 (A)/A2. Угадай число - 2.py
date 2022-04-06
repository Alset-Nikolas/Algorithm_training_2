

if __name__ == '__main__':
    n = int(input())
    info = []
    ans = input()
    numbers = list(range(n + 1))
    len_numbers = n
    while ans != "HELP":
        new_fact = list(map(int, ans.split()))
        ans = input()
        no_zero = list()
        for x in new_fact:
            if numbers[x] != 0:
                no_zero.append(x)
        len_no_zero = len(no_zero)
        if len_numbers - len_no_zero >= len_no_zero:
            len_numbers -= len_no_zero
            for val in new_fact:
                numbers[val] = 0
            print("NO")
        else:
            numbers = [0] * (n + 1)
            for x in no_zero:
                numbers[x] = x
            print("YES")
            len_numbers = len_no_zero

    for x in numbers:
        if x != 0:
            print(x, end=" ")
