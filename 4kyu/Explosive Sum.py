def exp_sum(n):
    #TODO: implement
    res = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        res[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                res[i][j] = 1 + res[i][j-1]
            elif i > j:
                res[i][j] = res[i-j][j] + res[i][j-1]
            else:
                res[i][j] = res[i][i]
    return res[-1][-1]
