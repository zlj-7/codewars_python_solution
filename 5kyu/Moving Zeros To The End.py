from functools import cmp_to_key

def cmp(x, y):
    if not (type(x) == int or type(x) == float) and not (type(y) == int or type(y) == float):
        return 0
    elif not (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        return 0 if y != 0 else -1
    elif (type(x) == int or type(x) == float) and not (type(y) == int or type(y) == float):
        return 1 if x == 0 else 0
    else:
        if x != 0 and y != 0:
            return 0
        elif x == 0 and y != 0:
            return 1
        elif x != 0 and y == 0:
            return -1
        else:
            return 0

def move_zeros(array):
    return sorted(array, key=cmp_to_key(cmp))
