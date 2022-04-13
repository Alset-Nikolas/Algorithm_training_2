if __name__ == '__main__':
    colors = set()
    counter = dict()
    with open("input.txt", "r") as f:
        for line in f:
            colors_i, val_i = line.split()
            colors.add(colors_i)
            if colors_i not in counter:
                counter[colors_i] = 0
            counter[colors_i] += int(val_i)
    colors = list(colors)
    colors.sort()
    for val in colors:
        print(val, counter[val])
