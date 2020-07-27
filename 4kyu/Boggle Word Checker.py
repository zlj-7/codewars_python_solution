def find_word(board, word):
    def dfs(loc, pos):
        if pos == len(word):
            return True
        for move in moves:
            next_ = (loc[0]+move[0], loc[1]+move[1])
            if 0 <= next_[0] < len(board) and 0 <= next_[1] < len(board[1]):
                if board[next_[0]][next_[1]] == word[pos] and next_ not in visited:
                    visited.add(next_)
                    if dfs(next_, pos+1):
                        return True
                    visited.remove(next_)
        return False

    moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != word[0]:
                continue
            visited = set()
            visited.add((i, j))
            if dfs((i, j), 1):
                return True
    return False
