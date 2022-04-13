if __name__ == '__main__':
    n = int(input())
    colors = set()
    counter = dict()
    for i in range(n):
        colors_i, val_i = list(map(int, input().split()))
        colors.add(colors_i)
        if colors_i not in counter:
            counter[colors_i] = 0
        counter[colors_i] += val_i
    colors = list(colors)
    colors.sort()
    for val in colors:
        print(val, counter[val])
