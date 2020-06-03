from collections import defaultdict
def encode_rail_fence_cipher(string, n):
    if len(string) == 0:
        return string
    res = ""
    level = defaultdict(str)
    cur_level = 0
    direction = 1
    for char in string:
        level[cur_level] += char
        cur_level += direction
        if cur_level == 0 or cur_level == n-1:
            direction *= -1
    for i in range(n):
        res += level[i]
    return res

def decode_rail_fence_cipher(string, n):
    if len(string) == 0:
        return string
    level_count = defaultdict(int)
    for current in range(n):
        pos = current
        gap = {1:2*(n-1-current), -1: 2*(current)}
        direction = 1 if current != n-1 else -1
        while pos < len(string):
            level_count[current] += 1
            pos += gap[direction]
            if current != 0 and current != n-1:
                direction *= -1
    level = defaultdict(str)
    preSum = 0
    for i in range(n):
        level[i] = string[preSum:preSum+level_count[i]]
        preSum += level_count[i]
    Iterations = []
    for i in range(n):
        Iterations.append(iter(level[i]))
    res = ""
    cur_level = 0
    direction = 1
    for _ in string:
        res += next(Iterations[cur_level])
        cur_level += direction
        if cur_level == 0 or cur_level == n-1:
            direction *= -1
    return res

if __name__ == '__main__':
    string = "WEAREDISCOVEREDFLEEATONCE"
    encode = encode_rail_fence_cipher(string, 3)
    print('encode : ' + encode)
    decode = decode_rail_fence_cipher(encode, 3)
    print('decode : ' + decode)
    print(decode == string)