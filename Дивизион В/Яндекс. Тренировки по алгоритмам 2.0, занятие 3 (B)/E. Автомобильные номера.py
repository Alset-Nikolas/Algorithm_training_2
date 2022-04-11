if __name__ == '__main__':
    n = int(input())
    info_person = []
    for x in range(n):
        info_person.append(list([simvol for simvol in input()]))

    answer = []
    max_parametr = 0
    m = int(input())
    for i_number in range(m):
        real_number = input()
        number = set(real_number)
        start = 0
        i_max_parametr = 0
        while start != n:

            if all([x in number for x in info_person[start]]):
                i_max_parametr +=1
            start += 1
        if i_max_parametr > max_parametr:
            max_parametr = i_max_parametr
            answer = [real_number]
        elif i_max_parametr == max_parametr:
            answer.append(real_number)
    
    for x in answer:
        print(x)
