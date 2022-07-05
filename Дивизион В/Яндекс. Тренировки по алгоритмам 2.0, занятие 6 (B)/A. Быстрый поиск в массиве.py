# def bin(x):
#     '''
#     Сколько чисел <= x
#     '''
#     l = -1
#     r = len(mass)
#
#     while l < r:
#         m = (l + r) >> 1
#         print(l,m,r)
#         if mass[m] > x:
#             r = m
#         else:
#             l = m + 1
#     return r
def bin_r(x):
    '''
    Сколько чисел >= x
    '''
    l = -1
    r = len(mass)

    while l < r:
        m = (l + r+1) //2
        if m >= len(mass):
            return 0
        if mass[m] < x:
            l = m
        else:
            r = m - 1
    return len(mass) - l - 1

def calc(l, r):
    l_i = bin_r(l)
    r_i = bin_r(r+1)
    return l_i - r_i


if __name__ == '__main__':
    n = int(input())
    mass =  list(map(int, input().split()))
    mass.sort()
    k = int(input())
    for i in range(k):
        print(calc(*list(map(int, input().split()))), end=' ')

