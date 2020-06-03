from queue import PriorityQueue

def path_finder(maze):
    maze = maze.split('\n')
    memory = dict()
    pq = PriorityQueue()
    r, c = len(maze), len(maze[0])
    start, end = (0,0), (r-1, c-1)
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    pq.put((0, start))
    while not pq.empty():
        step, cur = pq.get()
        if cur in memory and memory[cur] <= step:
            continue
        memory[cur] = step
        # 第一次遇到终点, 结束BFS
        if cur == end:
            break
        for nei in neighbors:
            next_ = (nei[0] + cur[0], nei[1] + cur[1])
            if (0 <= next_[0] < r) and (0 <= next_[1] < c) and maze[next_[0]][next_[1]] != 'W':
                if next_ in memory and memory[next_] <= step + 1:
                    continue
                pq.put((step+1, next_))

    return memory[end] if end in memory else False