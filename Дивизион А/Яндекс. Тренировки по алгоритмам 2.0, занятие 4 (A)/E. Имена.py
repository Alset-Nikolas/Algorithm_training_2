def max_literal_index(name_1, count1, count2):
    '''Функия поиска'''
    max_symbol = None
    ans_index1 = None
    del_dict = dict()
    for i, t in enumerate(name_1):
        if t in count2 and count2[t] > 0:
            if t not in del_dict:
                del_dict[t] = 0
            del_dict[t] += 1
            if max_symbol is None:
                max_symbol = t
                ans_index1 = i
                for key, val in del_dict.items():
                    count1[key] -= val
            else:
                if t > max_symbol:
                    max_symbol = t
                    ans_index1 = i
                    for key, val in del_dict.items():
                        count1[key] -= val
    if ans_index1 is None:
        return -1, - 1
    return ans_index1, max_symbol


def remove(name_2, max_symbol, count2):
    del_dict = dict()
    for i, t in enumerate(name_2):
        if t not in del_dict:
            del_dict[t] = 0
        del_dict[t] += 1
        if t == max_symbol:
            for key, val in del_dict.items():
                count2[key] -= val
            return i


def create_count_dict(name_1):
    count = dict()
    for t in name_1:
        if t not in count:
            count[t] = 0
        count[t] += 1
    return count


if __name__ == '__main__':
    name1 = input()
    name2 = input()
    count1 = create_count_dict(name1)
    count2 = create_count_dict(name2)
    ans = []
    i_index, max_symbol = max_literal_index(name1, count1, count2)
    while i_index!=-1:
        ans.append(max_symbol)
        j_index = remove(name2, max_symbol, count2)
        name1 = name1[i_index+1:]
        name2 = name2[j_index+1:]
        i_index, max_symbol = max_literal_index(name1, count1, count2)

    print(''.join(ans))
