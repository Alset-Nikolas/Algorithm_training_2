def main(lines):
    max_l = max(lines)
    sum_l = sum(lines)
    if max_l > sum_l - max_l:
        return max_l-(sum_l - max_l)
    return sum_l
if __name__ == '__main__':
    n = int(input())
    lines = list(map(int, input().split()))
    res = main(lines)
    print(res)

    assert main([1, 5, 2, 1]) == 1
    assert main([5, 12, 4, 3]) == 24