def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def c(k):
    if k == 1:
        return 1
    if isPrime(k):
        return 0
    C = int((k*k*k)**0.5)
    if C*C != k*k*k:
        return 0
    flag = True
    factors = []
    div = 2
    while C>1:
        if flag:
            if isPrime(C):
                factors.append(C)
                factors.append(1)
                break
            flag = False
        if C % div != 0:
            div += 1
            continue
        C //= div
        factors.append(div)
        flag = True
    if len(factors) == 2:
        return 1
    cnt = set()
    visited = set()
    def dfs(a,b,pos):
        if pos == len(factors):
            cnt.add((a, b))
        else:
            if (a*factors[pos], b, pos+1) not in visited:
                dfs(a*factors[pos], b, pos+1)
                visited.add((a*factors[pos], b, pos+1))
            if (a, b*factors[pos], pos+1) not in visited:
                dfs(a, b*factors[pos], pos+1)
                visited.add((a, b*factors[pos], pos+1))
    dfs(1, 1, 0)
    return len(cnt)