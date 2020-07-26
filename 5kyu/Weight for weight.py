def order_weight(strng):
    str_list = []
    for string in strng.split(' '):
        digit = sum(map(int, string))
        str_list.append((string, digit))
    return " ".join(list(map(lambda x:x[0],sorted(str_list, key=lambda x : (x[1] ,x[0])))))