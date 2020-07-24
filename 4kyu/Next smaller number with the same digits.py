def next_smaller(n):
    # TODO: implement
    digits = [val for val in str(n)]
    idx1, idx2 = None, None
    for i in range(len(digits)-2, -1, -1):
        idx1 = i
        for j in range(len(digits)-1, i, -1):
            if digits[i] > digits[j]:
                if idx2 == None:
                    idx2 = j
                else:
                    if digits[j] > digits[idx2]:
                        idx2 = j
        if idx2 != None:
            break
    if idx2 == None:
        return -1
    if idx1 == 0 and digits[idx2] == '0':
        return -1
    digits[idx1], digits[idx2] = digits[idx2], digits[idx1]
    return int("".join(digits[:idx1+1]) + "".join(sorted(digits[idx1+1:], reverse=True)))