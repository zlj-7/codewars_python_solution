from queue import PriorityQueue
def blox_solver(arr: list):

    hole, block = None, None
    rows, cols = len(arr), len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 'X':
                hole = (i, j)
            elif arr[i][j] == 'B':
                block = (i, j)
            if hole and block:
                break

    pq = PriorityQueue()
    # 走到该位置的步数, 此时block的状态
    pq.put((0, [block], ""))
    memory = dict()

    while not pq.empty():
        cost, loc, path = pq.get()
        trans_loc = loc[0] if len(loc) == 1 else (loc[0], loc[1])
        pre_cost = memory.get(trans_loc, None)
        if pre_cost != None and len(pre_cost) <= cost:
            continue
        memory[trans_loc] = path
        if len(loc) == 1 and loc[0] == hole:
            break
        candidates = GetCandidates(arr, loc)

        for candidate in candidates:
            pq.put((cost+1, candidate[0], path+candidate[1]))

    return memory[hole]

def GetCandidates(arr: list, loc: list) -> list:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dire_map = {
        (0, 1) : 'R',
        (0, -1) : 'L',
        (-1, 0) : 'U',
        (1, 0) : 'D'
    }
    candidates = []
    if len(loc) == 1:
        one_loc = loc[0]
        for cur in directions:
            tmp = [(cur[0]+one_loc[0], cur[1]+one_loc[1]), (2*cur[0]+one_loc[0], 2*cur[1]+one_loc[1])]
            if InMap(arr, tmp):
                candidates.append([tmp, dire_map[cur]])
    else:
        # 竖放
        if abs(loc[0][0] - loc[1][0]) == 1:
            for cur in directions[:2]:
                tmp = [(cur[0]+loc[0][0], cur[1]+loc[0][1]), (cur[0]+loc[1][0], cur[1]+loc[1][1])]
                if InMap(arr, tmp):
                    candidates.append([tmp, dire_map[cur]])
            if loc[0][0] > loc[1][0]:
                loc[0], loc[1] = loc[1], loc[0]
            tmp1 = [(loc[0][0]-1, loc[0][1])]
            tmp2 = [(loc[1][0]+1, loc[1][1])]
            if InMap(arr, tmp1):
                candidates.append([tmp1, 'U'])
            if InMap(arr, tmp2):
                candidates.append([tmp2, 'D'])
        # 横放
        else:
            for cur in directions[2:]:
                tmp = [(cur[0] + loc[0][0], cur[1] + loc[0][1]), (cur[0] + loc[1][0], cur[1] + loc[1][1])]
                if InMap(arr, tmp):
                    candidates.append([tmp, dire_map[cur]])
            if loc[0][1] > loc[1][1]:
                loc[0], loc[1] = loc[1], loc[0]
            tmp1 = [(loc[0][0], loc[0][1]-1)]
            tmp2 = [(loc[1][0], loc[1][1]+1)]

            if InMap(arr, tmp1):
                candidates.append([tmp1, 'L'])
            if InMap(arr, tmp2):
                candidates.append([tmp2, 'R'])
    return candidates

def InMap(arr: list, loc: list):
    for tmp in loc:
        if tmp[0] < 0 or tmp[0] >= len(arr) or tmp[1] < 0 or tmp[1] >= len(arr[0]):
            return False
        if arr[tmp[0]][tmp[1]] == '0':
            return False
    return True

if __name__ == '__main__':

    example_tests = [
        ['1110000000',
         '1B11110000',
         '1111111110',
         '0111111111',
         '0000011X11',
         '0000001110'],
        ['000000111111100',
         '111100111001100',
         '111111111001111',
         '1B11000000011X1',
         '111100000001111',
         '000000000000111'],
        ['00011111110000',
         '00011111110000',
         '11110000011100',
         '11100000001100',
         '11100000001100',
         '1B100111111111',
         '11100111111111',
         '000001X1001111',
         '00000111001111'],
        ['11111100000',
         '1B111100000',
         '11110111100',
         '11100111110',
         '10000001111',
         '11110000111',
         '11110000111',
         '00110111111',
         '01111111111',
         '0110011X100',
         '01100011100'],
        ['000001111110000',
         '000001001110000',
         '000001001111100',
         'B11111000001111',
         '0000111000011X1',
         '000011100000111',
         '000000100110000',
         '000000111110000',
         '000000111110000',
         '000000011100000']
    ]
    for arr in example_tests:
        print(blox_solver(arr))

    example_sols = [['RRDRRRD', 'RDDRRDR', 'RDRRDDR'], ['ULDRURRRRUURRRDDDRU', 'RURRRULDRUURRRDDDRU'],
                    ['ULURRURRRRRRDRDDDDDRULLLLLLD'], ['DRURURDDRRDDDLD'],
                    ['RRRDRDDRDDRULLLUULUUURRRDDLURRDRDDR', 'RRRDDRDDRDRULLLUULUUURRDRRULDDRRDDR',
                     'RRRDRDDRDDRULLLUULUUURRDRRULDDRRDDR', 'RRRDDRDDRDRULLLUULUUURRRDDLURRDRDDR']]
    for i, x in enumerate(example_tests):
        print(blox_solver(x) in example_sols[i])

