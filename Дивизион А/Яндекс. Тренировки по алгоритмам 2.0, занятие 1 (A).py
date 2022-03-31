def main(a, b, c, d):
    def calc_classics(a, b):
        if a != 0:
            ans = -b / a
        else:
            if b == 0:
                ans = "INF"
            else:
                ans = "NO"
        return ans

    ans_classics = calc_classics(a, b)
    ans = None
    if c == 0:
        ans = ans_classics
    elif d == 0:
        if ans_classics != 0 :
            ans = ans_classics
        else:
            ans = "NO"
    else:
        if ans_classics != -d/c:
            ans = ans_classics
        else:
            ans = "NO"
    if isinstance(ans, float):
        if ans_classics == int(ans_classics):
            return int(ans)
        else:
            return "NO"
    return ans


if __name__ == '__main__':
    numbers = []
    for i in range(4):
        numbers.append(int(input()))
    res = main(*numbers)
    print(res)

    assert main(*[1, 1, 2, 2]) == "NO"
    assert main(*[2, -4, 7, 1]) == 2
    assert main(*[35, 14, 11, -3]) == "NO"
