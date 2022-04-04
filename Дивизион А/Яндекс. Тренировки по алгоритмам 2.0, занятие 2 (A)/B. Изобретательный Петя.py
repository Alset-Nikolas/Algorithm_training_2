def main(x, y):
    n = len(x)
    m = len(y)
    st_i = m - n
    end_i = st_i + n - 1
    res = ''
    while end_i >= 0:
        if st_i < 0 and end_i >= 0:
            flag = False
            if res == "" and st_i == 0 and end_i == n - 1:
                break
            del_index = end_i
            for j in range(n):
                while len(x[j:]) < len(y[:del_index + 1]):
                    res = y[del_index] + res
                    del_index -= 1
                if x[j:] == y[:del_index + 1]:
                    flag = True
                    break
            if flag:
                print(res)
            else:
                print(y)
            break
        if y[st_i: end_i + 1] == x:
            st_i -= n
            end_i -= n
        else:
            res = y[end_i:]
            st_i -= 1
            end_i -= 1
    else:
        print(res)


if __name__ == '__main__':
    x = input()
    y = input()
    res = main(x, y)
