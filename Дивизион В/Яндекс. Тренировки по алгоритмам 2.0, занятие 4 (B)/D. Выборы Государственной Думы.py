import math

if __name__ == '__main__':
    n = 450
    info = []
    all_people = 0
    res = []
    with open("input.txt", "r") as file:
        for line in file:
            words = line.split()
            name_i = " ".join(words[:-1])
            val_i = int(words[-1])
            all_people += val_i
            info.append([name_i, val_i])
    p = all_people / 450
    for i in range(len(info)):
        res.append(info[i][1] // p)
    # print(res)
    div_ = [[info[i][1] % p, res[i], i] for i in range(len(info))]
    div_.sort(key=lambda x: x[1])
    div_.sort(key=lambda x: x[0], reverse=True)
    start_i = 0
    index = div_[start_i][2]
    # print(div_)
    while sum(res) != 450:
        res[index] += 1
        start_i = (start_i + 1) % len(info)
        index = div_[start_i][2]

    for i in range(len(info)):
        print(info[i][0], int(res[i]))

