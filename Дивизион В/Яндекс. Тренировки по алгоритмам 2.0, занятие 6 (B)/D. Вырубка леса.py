def trees(A, B, K, M, g):
    n = g//K
    dn = A * n*(K-1)
    m =  g//M
    dm = B*m*(M-1)
    dmm = 0
    dnn =0
    if K != 1:
        dmm = (g % K)*A
    if M != 1:
        dnn =(g % M)*B
    return dn + dm + dmm+ dnn

if __name__ == '__main__':
    A, K, B, M, X = map(int, input().split())
    g_min = 0
    g_max = X // A + X// B

    while g_max != g_min:
        g_c = (g_min+g_max)//2

        if trees(A, B, K, M, g_c) < X:
            g_min = g_c+1
        else:
            g_max = g_c
    print(g_min)