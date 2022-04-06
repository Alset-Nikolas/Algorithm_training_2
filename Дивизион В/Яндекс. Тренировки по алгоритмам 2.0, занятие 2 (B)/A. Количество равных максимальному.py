def main(numbers):
    max_number = 0
    q_n = 0
    for n in numbers:
        if n > max_number:
            max_number = n
            q_n = 1
        elif n == max_number:
            q_n += 1
    return q_n
if __name__ == '__main__':
    numbers = []
    n = int(input())
    while n != 0:
        numbers.append(n)
        n = int(input())
    res = main(numbers)
    print(res)

    assert main([1, 7, 9]) == 1
    assert main([1, 3, 3, 1]) == 2