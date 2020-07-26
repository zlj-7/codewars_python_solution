from collections import defaultdict

def isPrime(m):
    if m == 1:
        return False
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            return False
    return True

def decomp(n):
    # TODO:implement
    count = defaultdict(int)
    memory = defaultdict(dict)
    for i in range(2, n+1):
        if isPrime(i):
            memory[i] = {i:1}
            count[i] += 1
            continue
        div, cur = 2, i
        while div < cur:
            if not isPrime(div):
                div += 1
                continue
            if cur % div == 0:
                break
            div += 1
        tmp_dict = defaultdict(int)
        tmp_dict.update(memory[cur // div])
        if div not in tmp_dict.keys():
            tmp_dict[div] = 1
        else:
            tmp_dict[div] += 1
        memory[i] = tmp_dict
        for key, val in tmp_dict.items():
            count[key] += val

    ans = " * ".join(map(lambda x: (str(x[0]) + '^' + str(x[1])) if x[1] > 1 else str(x[0]), sorted(count.items(), key = lambda x:x[0])))
    return ans