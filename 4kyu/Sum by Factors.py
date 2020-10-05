def sum_for_list(lst):

    # 先找出绝对值最大的数, 然后通过素数筛, 选出所有的素数
    # 选出素数集合后, 对每个数, 我们计算其因数, 选出其中的素数, 将其值, 加入到字典中
    # 总结全部结果即可...
    n = max(map(abs, lst))
    NotPrime = [False] * (n+1)
    NotPrime[0], NotPrime[1] = True, True

    for j in range(2, n+1):
        if NotPrime[j]:
            continue
        for i in range(2*j, n+1, j):
            NotPrime[i] = True

    prime_lst = []
    for i in range(2, n+1):
        if NotPrime[i]:
            continue
        prime_lst.append(i)

    # 记录每个因子...
    summary = dict()
    for num in lst:
        ori = num
        for prime in prime_lst:
            if prime > abs(num): break
            contain = False
            while num % prime == 0:
                num //= prime
                contain = True
            if contain:
                summary[prime] = summary.setdefault(prime, 0) + ori

    return sorted([[k, v] for k, v in summary.items()], key= lambda x: x[0])


if __name__ == '__main__':

    print(sum_for_list([15, 30, -45] ))








