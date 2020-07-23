from queue import PriorityQueue
def shortestPath(topology, startPoint, endPoint):
    solution = []
    pq = PriorityQueue()
    pq.put((0, startPoint))
    min_consume, min_len = None, None
    while not pq.empty():
        consume, path = pq.get()
        if min_consume != None and consume > min_consume:
            continue
        if path[-1] == endPoint:
            if min_consume == None:
                min_consume = consume
            if min_len == None or min_len > len(path):
                min_len = len(path)
            solution.append(path)
            continue
        for adjacent in topology[path[-1]].keys():
            if len(path) >= 2 and adjacent == path[-2]:
                continue
            else:
                pq.put((consume+topology[path[-1]][adjacent], path+adjacent))
    solution = filter( lambda x: len(x) == min_len, solution)
    return list(map(lambda x: list(x), sorted(solution)))

if __name__ == '__main__':
    topology = {'a': {'b': 10, 'c': 20, 'd': 20}, 'b': {'a': 10, 'c': 20, 'd': 20, 'e': 20, 'f': 20, 'g': 20},
     'c': {'a': 10, 'b': 20, 'e': 20}, 'd': {'a': 10, 'b': 20, 'f': 20}, 'e': {'b': 10, 'c': 20, 'g': 20},
     'f': {'b': 10, 'd': 20, 'g': 20}, 'g': {'b': 10, 'e': 20, 'f': 20}}
    print(shortestPath(topology, 'c', 'g'))
