def snail(snail_map):
    res = []
    row, col = len(snail_map), len(snail_map[0])
    length = row * col
    res.extend(snail_map[0])

    s = (0, col-1)
    direction = ['down', 'left', 'up', 'right']
    dire_map = {
        'down' : (1, 0),
        'left' : (0, -1),
        'up' : (-1, 0),
        'right' : (0, 1),
    }
    cur_d = 0
    diff = 0
    flag = True
    while len(res) < length:
        if flag == True:
            diff += 1
            cur_l = row - diff
            flag = False
        else:
            cur_l = col - diff
            flag = True
        key = direction[cur_d]
        add = dire_map[key]
        for _ in range(cur_l):
            s = (s[0]+add[0], s[1]+add[1])
            res.append(snail_map[s[0]][s[1]])
        cur_d = (cur_d + 1) % 4

    return res