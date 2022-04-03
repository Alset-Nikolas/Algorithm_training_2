def main(r, i , c):
    if i==0:
        if r != 0 :
            res = 3
        else:
            res = c
    elif i == 1:
        res = c
    elif i == 4:
        if r != 0 :
            res = 3
        else:
            res = 4
    elif i == 6:
        res = 0
    elif i == 7:
        res = 1
    else:
        res = i
    return res

if __name__ == '__main__':
    r = int(input())
    i = int(input())
    c = int(input())

    res = main(r, i , c)
    print(res)