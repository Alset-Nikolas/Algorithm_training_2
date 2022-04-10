fib_info = [1, 1]
fib_numbers = set()
fib_numbers.add(0)
fib_numbers.add(1)
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        new_number = int(input())
        new = fib_info[-1]
        while new_number > new:
            new += fib_info[-2]
            fib_info.append(new)
            fib_numbers.add(new)
        if new_number in fib_numbers:
            print("Yes")
        else:
            print("No")

