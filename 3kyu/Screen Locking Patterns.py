def count_patterns_from(firstPoint, length):
    # Your code here!

    if length >= 10 or length <= 0:
        return 0
    moves = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (-1,1), (1,-1), (-1,-1),]
    another = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, -1), (2, -1), (-2, 1)]
    visited = set()
    count = 0
    map_point = {
        'A' : (0, 0),
        'B' : (0, 1),
        'C' : (0, 2),
        'D' : (1, 0),
        'E' : (1, 1),
        'F' : (1, 2),
        'G' : (2, 0),
        'H' : (2, 1),
        'I' : (2, 2),
    }
    start = map_point[firstPoint]
    visited = set()
    visited.add(start)
    def dfs(loc, curLen):
        if curLen == 1:
            nonlocal count
            count += 1
        else:
            for step in moves:
                next_ = (loc[0]+step[0], loc[1]+step[1])
                if 0 <= next_[0] <= 2 and 0 <= next_[1] <= 2:
                    if next_ not in visited:
                        visited.add(next_)
                        dfs(next_, curLen-1)
                        visited.remove(next_)
                    else:
                        next_ = (loc[0]+step[0]*2, loc[1]+step[1]*2)
                        if 0 <= next_[0] <= 2 and 0 <= next_[1] <= 2:
                            if next_ not in visited:
                                visited.add(next_)
                                dfs(next_, curLen-1)
                                visited.remove(next_)
            for step in another:
                next_ = (loc[0]+step[0], loc[1]+step[1])
                if 0 <= next_[0] <= 2 and 0 <= next_[1] <= 2:
                    if next_ not in visited:
                        visited.add(next_)
                        dfs(next_, curLen-1)
                        visited.remove(next_)
    dfs(start, length)
    return count

if __name__ == '__main__':
    print(count_patterns_from('D', 9))


