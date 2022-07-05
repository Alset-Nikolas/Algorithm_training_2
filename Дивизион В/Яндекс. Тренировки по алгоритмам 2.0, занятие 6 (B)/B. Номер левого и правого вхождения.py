def left_bin(x):
    '''
    Сколько чисел >= x
    '''
    l = 0
    r = len(mass) - 1

    while l < r:
        m = (l + r) // 2
        if mass[m] >= x:
            r = m
        else:
            l = m + 1
    if mass[l] != x :
        return 0
    return l + 1

def right_bin(x):
    '''
    Сколько чисел <= x
    '''
    l = 0
    r = len(mass)-1

    while l < r:
        m = (l + r + 1) //2

        if mass[m] <= x:
            l = m
        else:
            r = m - 1
    if mass[l] != x:
        return 0
    return l + 1

def calc(x):
    l_i = left_bin(x)
    r_i = right_bin(x)
    return l_i , r_i


if __name__ == '__main__':
    n = int(input())
    mass =  list(map(int, input().split()))
    mass.sort()
    k = int(input())
    mass_X =  list(map(int, input().split()))
    for x in mass_X:
        print(*calc(x))
