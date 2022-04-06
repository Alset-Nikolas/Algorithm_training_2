n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(sum(numbers[:-1]))