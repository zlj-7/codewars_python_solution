import math
from queue import PriorityQueue

# solve1 bsf
def wire_DHD_SG1(existingWires):

    _existingWires = existingWires.split('\n')
    _r, _c = len(_existingWires), len(_existingWires[0])
    _existingWires = [list(row) for row in _existingWires]
    # 格式 到某个的距离,当前位置,形成的路径list[(),(),()]
    _pq = PriorityQueue()
    # 起点到该位置的距离, 更新
    _memset = dict()
    # 路径
    _path = dict()
    # 起点与终点
    _start = _end = _res = None
    for i in range(_r):
        for j in range(_c):
            if _existingWires[i][j] == 'S':
                _start = (i, j)
            elif _existingWires[i][j] == 'G':
                _end = (i, j)
    # 当前位置, 离起点所经过的距离, 路径
    _pq.put((0, _start, None))
    while not _pq.empty():
        _dist, _cur, _pre = _pq.get()
        if _cur in _memset and _memset[_cur] <= _dist:
            continue
        _memset[_cur] = _dist
        _path[_cur] = _pre
        if _cur == _end:
            # _res = copy.deepcopy(_path)
            break
        next_ = reach(_cur, _existingWires)
        for item in next_:
            tmp_pos, tmp_dist = item
            if tmp_pos in _memset and _memset[tmp_pos] <= _dist + tmp_dist:
                continue
            _pq.put((_dist+tmp_dist, tmp_pos, _cur))

    if _end not in _path.keys():
        return "Oh for crying out loud..."

    _cur = _path[_end]
    while _cur != _start:
        _existingWires[_cur[0]][_cur[1]] = 'P'
        _cur = _path[_cur]

    ans = ""
    for i in range(_r):
        for j in range(_c):
            ans += _existingWires[i][j]
        ans += '\n'
    return ans.strip('\n')

def reach(pos, existingWires):
    adds = [(0,1),(0,-1),(-1,0),(1,0),(-1,1),(-1,-1),(1,-1),(1,1)]
    res = []
    r, c = len(existingWires), len(existingWires[0])
    for add in adds:
        tmp_pos = (pos[0]+add[0], pos[1]+add[1])
        if 0 <= tmp_pos[0] < r and 0 <= tmp_pos[1] < c and existingWires[tmp_pos[0]][tmp_pos[1]] != 'X':
            dist = math.sqrt((pos[0]-tmp_pos[0])**2 + (pos[1]-tmp_pos[1])**2)
            res.append((tmp_pos, dist))
    return res