def next_bigger(n):
    num_list = [c for c in str(n)]
    num1, num2 = None, None
    for i in range(len(num_list)-2, -1, -1):
        num1 = i
        for j in range(num1+1, len(num_list)):
            if num_list[j] > num_list[i]:
                if num2 == None:
                    num2 = j
                elif num_list[j] < num_list[num2]:
                    num2 = j
        if num2 != None:
            break
    if num2 == None:
        return -1

    num_list[num1], num_list[num2] = num_list[num2], num_list[num1]
    part2 = "".join(sorted(num_list[num1+1:]))
    res = "".join(num_list[:num1+1]) + part2
    return int(res)