
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
    interests = count1.keys() & count2.keys()
    while len(interests)>0:
        max_simvol = max(interests)
        val_max_simvol = min(count1[max_simvol], count2[max_simvol])
        ans.append(max_simvol*val_max_simvol)
        name1 = name1.replace(max_simvol, "#", val_max_simvol)
        name1 = name1[name1.rfind("#") + 1:]
        name2 = name2.replace(max_simvol, "*", val_max_simvol)
        name2 = name2[name2.rfind("*") + 1:]
        count1 = create_count_dict(name1)
        count2 = create_count_dict(name2)
        interests = count1.keys() & count2.keys()
    print(''.join(ans))
