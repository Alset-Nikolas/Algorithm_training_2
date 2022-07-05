
if __name__ == '__main__':
    S = int(input())
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    C = list(map(int, input().split()))[1:]

    A = list((x, i) for i, x in enumerate(A))
    B = list((x, i) for i, x in enumerate(B))
    C = list((x, i) for i, x in enumerate(C))
    ans =None
    A.sort()
    B.sort()
    C.sort(key=lambda x: (x[0], -x[1]))
    flag = False
    for a, a_pos in A:
        index_c = len(C) - 1
        for b, b_pos in B:
            c = C[index_c][0]
            while index_c > 0 and a + b + c > S:
                index_c -= 1
                c = C[index_c][0]

            if a + b + c == S and (not flag or (a_pos, b_pos, C[index_c][1]) < ans):
                ans = a_pos, b_pos, C[index_c][1]
                flag = True

    if flag:
        print(*ans)
    else:
        print(-1)

'''
9
1 4 5
22 2 3
1 1
'''