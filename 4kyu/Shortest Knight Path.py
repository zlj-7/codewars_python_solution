from queue import PriorityQueue
def knight(p1, p2):
    # start here!
    start = (ord(p1[0])-ord('a')+1, int(p1[1]))
    end = (ord(p2[0])-ord('a')+1, int(p2[1]))
    moves = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        step, loc = pq.get()
        if loc == end:
            return step
        for move in moves:
            next_ = (loc[0]+move[0], loc[1]+move[1])
            if 1 <= next_[0] <= 8 and 1 <= next_[1] <= 8:
                pq.put((step+1, next_))
                if next_ == end:
                    return step + 1
