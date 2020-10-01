'''
1. 简化多项式表达, 同一个表达式, 顺序字典序
2. 首位没有+
3. 先整体按照变量数, 从小到大排序.
4. 若变量数相同, 则按照字典序排序.
'''

def simplify(poly : str) -> str:

    coef = dict()
    i, n = 0, len(poly)

    while i < n:
        const = "-" if poly[i] == '-' else ""
        if poly[i] == '-' or poly[i] == '+':
            i += 1
        while i < n and poly[i].isdigit():
            const += poly[i]
            i += 1
        combo = []
        while i < n and (poly[i] != '+' and poly[i] != '-'):
            combo.append(poly[i])
            i += 1
        combo.sort()
        combo = "".join(combo)

        coef[combo] = coef.setdefault(combo, 0) + (int(const) if (const != "" and const != "-")
            else (-1 if const == "-" else 1))

    polynomials = []
    for key, val in coef.items():
        if val > 0:
            tmp = ("+{}".format(str(val) if val != 1 else ""), key)
            polynomials.append(tmp)
        elif val < 0:
            tmp = ("{}".format(str(val) if val != -1 else "-"), key)
            polynomials.append(tmp)

    polynomials.sort(key = lambda x : (len(x[1]), x[1]))

    res = ""
    for item in polynomials:
        res += item[0] + item[1]

    return res if res[0] != '+' else res[1:]


if __name__ == '__main__':

    poly = "-8fk+5kv-4yk+7kf-qk+yqv-3vqy+4ky+4kf+yvqkf"
    print(simplify(poly))