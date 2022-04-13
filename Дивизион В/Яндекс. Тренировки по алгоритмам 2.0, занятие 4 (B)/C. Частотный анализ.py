if __name__ == '__main__':
    counter = dict()
    with open("input.txt", "r") as file:
        for line in file:
            for word in line.split():
                if word not in counter:
                    counter[word] = 0
                counter[word] += 1
    words = []
    for word, freq in counter.items():
        words.append([freq, word])
    words.sort(key=lambda x: x[1])
    words.sort(key=lambda x: x[0], reverse=True)
    for freq, word in words:
        print(word)