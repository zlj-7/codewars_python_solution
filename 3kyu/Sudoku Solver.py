import copy
def sudoku(puzzle):

    visited = {
        'box' : [],
        'row' : [],
        'col' : [],
    }

    for key in visited:
        for i in range(9):
            visited[key].append(set())

    init_visit(puzzle, visited)
    res = None
    def dfs(pos):
        if pos == (8, 8):
            nonlocal res
            if puzzle[-1][-1] != 0:
                res = copy.deepcopy(puzzle)
                return True
            for num in range(1, 10):
                if num not in visited['row'][-1] and (num not in visited['col'][-1]) \
                        and (num not in visited['box'][-1]):
                    puzzle[-1][-1] = num
                    res = copy.deepcopy(puzzle)
                    return True
            return False
        else:
            _next = (pos[0] + 1, 0) if pos[1] == 8 else (pos[0], pos[1] + 1)
            if puzzle[pos[0]][pos[1]] != 0:
                dfs(_next)
            else:
                box = 3 * (pos[0]//3) + (pos[1]//3)
                for num in range(1, 10):
                    if num not in visited['row'][pos[0]] and (num not in visited['col'][pos[1]]) \
                        and (num not in visited['box'][box]):
                        visited['row'][pos[0]].add(num)
                        visited['col'][pos[1]].add(num)
                        visited['box'][box].add(num)
                        puzzle[pos[0]][pos[1]] = num
                        if dfs(_next):
                            return True
                        visited['row'][pos[0]].remove(num)
                        visited['col'][pos[1]].remove(num)
                        visited['box'][box].remove(num)
                        puzzle[pos[0]][pos[1]] = 0
            return False
    dfs((0, 0))

    return res

def init_visit(puzzle, visited):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                visited['row'][i].add(puzzle[i][j])
                visited['col'][j].add(puzzle[i][j])
                visited['box'][3*(i//3)+j//3].add(puzzle[i][j])

if __name__ == '__main__':
    print('原始数独数据')
    puzzle = [[]]
