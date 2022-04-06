
def bunery_right(numbers, x):
    '''
    Функция бинарного поиска первого элемента >= x
    :param numbers:
    :param x:
    :return:
    '''
    l = -1
    r = len(numbers)-1
    if len(numbers) > 1 and numbers[-1] < x:
        return len(numbers)
    while r -l != 1:
        m = (l + r ) // 2
        if numbers[m] < x:
            l = m
        else:
            r = m
    return r

def bunery_left(numbers, x):
    '''
    Функция бинарного поиска первого элемента <= x
    :param numbers:
    :param x:
    :return:
    '''
    l = -1
    r = len(numbers)-1
    if len(numbers) > 1 and numbers[0] > x:
        return -1
    while r -l != 1:
        m = (l + r ) // 2
        if numbers[m] > x:
            r = m
        else:
            l = m
    return l




def main(L, numbers):
    n = len(numbers)
    if L % 2 != 0:
        magik_block = L // 2
        if magik_block in numbers:
            index_pop = numbers.index(magik_block)
            return [numbers[index_pop]]
        x_r = bunery_right(numbers, magik_block)
        x_l = bunery_left(numbers, magik_block)
        return [numbers[x_l], numbers[x_r]]
    else:
        magik_block_l = L // 2 - 1
        magik_block_r = L // 2
        if magik_block_l in numbers and magik_block_r in numbers:
            index_pop1 = numbers.index(magik_block_l)
            index_pop2 = numbers.index(magik_block_r)
            return [numbers[index_pop1], numbers[index_pop2]]
        x_r = bunery_right(numbers, magik_block_r)
        x_l = bunery_left(numbers, magik_block_l)
        return [numbers[x_l], numbers[x_r]]


if __name__ == '__main__':
    len_dosk, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    res = main(len_dosk, numbers)
    print(*res)
    assert main(5, [0, 2]) == [2]
    assert main(13, [1, 4, 8, 11]) == [4, 8]
    assert main(14, [1, 6, 8, 11, 12, 13]) == [6, 8]
