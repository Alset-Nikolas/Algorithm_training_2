if __name__ == '__main__':
    all_numbers = set()
    for x in list(map(int, input().split())):
        print("YES" if x in all_numbers else "NO")
        all_numbers.add(x)
