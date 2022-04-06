def main(n, info):
    numbers = list(range(n + 1))
    ans = []
    len_numbers = n
    for new_fact in info:
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


if __name__ == '__main__':
    n = int(input())
    info = []
    ans = input()
    while ans != "HELP":
        info.append(list(map(int, ans.split())))
        ans = input()

    main(n, info)

    # assert main(10, [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]) == ["NO", "YES", {6, 8, 10}]
    # assert main(10, [[1], [2], [3], [4], [5], [6], [7], [8], [9]]) == ["NO"] * 9 + [{10}]
    # assert main(16, [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12], [13, 14], [16]]) == ["NO"] * 4 + [{15}]
