def change(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]
    print(i, j)
    return numbers[j]



def main(N, numbers):

    for i in range(1, N-1):
        if numbers[i] != i:
            now = i
            while numbers[now] != i:
                now = change(numbers, now, N-1)
            now = change(numbers, now, N)
            now = change(numbers, now, N)
            change(numbers, numbers[N-1], N-1)
    if numbers[N-1] == N:
        change(numbers, N - 1, N)

if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(range(0, N + 1))
    for k, x in enumerate(range(M)):
        i_person, j_person = map(int, input().split())
        numbers[i_person], numbers[j_person] = numbers[j_person], numbers[i_person]
    res = main(N, numbers)
