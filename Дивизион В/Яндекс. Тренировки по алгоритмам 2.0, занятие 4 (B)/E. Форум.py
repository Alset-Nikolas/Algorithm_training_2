if __name__ == '__main__':
    start = 0
    flag_subject = False
    subjects = dict()
    with open("input.txt", "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            words = line.split()
            if i == 0:
                word = words[0]
                n = int(word)
                subject_or_comment = [False] * (n + 1)
                continue
            if flag_subject:
                subjects[line] = 0
                subject_or_comment[start] = line
                flag_subject = False
            if len(words) == 1:
                word = words[0]
                if word.isdigit():
                    start += 1
                    if word == "0":
                        # subject_or_comment[start] = 0
                        flag_subject = True
                        continue
                    else:
                        subject_or_comment[start] = word

    for el in subject_or_comment[1:]:
        if el.isdigit():
            x = el
            while x.isdigit():
                x = subject_or_comment[int(x)]
            subjects[x] += 1


    max_comment = -1
    sub = None
    for key, val in subjects.items():
        if val > max_comment:
            max_comment = val
            sub = key
    print(sub)