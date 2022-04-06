def main(n, info):
    numbers = set(range(1, n+1))
    ans = []
    for new_fact in info:
        new_vars = set(new_fact)
        if len(numbers - new_vars) >= len(numbers & new_vars):
            numbers -= new_vars
            ans.append("NO")
        else:
            numbers =  numbers & new_vars
            ans.append("YES")
    ans.append(numbers)
    return ans




if __name__ == '__main__':
    n = int(input())
    info = []
    ans = input()
    while ans != "HELP":
        info.append(list(map(int, ans.split())))
        ans = input()

    res = main(n, info)
    ans = list(res[-1])
    for x in res[:-1]:
        print(x)
    for x in sorted(ans):
        print(x, end=" ")


    assert main(10, [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]) == ["NO", "YES", {6, 8, 10}]
    assert main(10, [[1], [2], [3], [4], [5], [6], [7], [8], [9]]) == ["NO"] * 9 + [{10}]
    assert main(16, [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12], [13, 14], [16]]) == ["NO"] * 4 + [{15}]
