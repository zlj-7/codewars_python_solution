from queue import PriorityQueue
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.val < other.val

# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    from collections import Counter
    cnt = Counter(s)
    return sorted([(k, v) for k, v in cnt.items()], key = lambda x: x[1], reverse=True)

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) <= 1:
        return None
    pq = PriorityQueue()
    for freq in freqs:
        char, count = freq
        pq.put((count, TreeNode(char)))
    while pq.qsize() > 1:
        item1, item2 = pq.get(), pq.get()
        root = TreeNode('#')
        root.left = item1[1]
        root.right = item2[1]
        pq.put((item1[0]+item2[0], root))
    _, root = pq.get()
    Huffman_code = dict()
    def travel(root, code):
        if root:
            if root.val != '#':
                Huffman_code[root.val] = code
            if root.left:
                travel(root.left, code + '0')
            if root.right:
                travel(root.right, code + '1')
    travel(root, '')
    return ("".join([Huffman_code[char] for char in s])) if len(s) else ""


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):

    if len(freqs) <= 1:
        return None

    pq = PriorityQueue()
    for freq in freqs:
        char, count = freq
        pq.put((count, TreeNode(char)))
    while pq.qsize() > 1:
        item1, item2 = pq.get(), pq.get()
        root = TreeNode('#')
        root.left = item1[1]
        root.right = item2[1]
        pq.put((item1[0]+item2[0], root))
    _, root = pq.get()
    CodeMap = dict()
    def travel(root, code):
        if root:
            if root.val != '#':
                CodeMap[code] = root.val
            if root.left:
                travel(root.left, code + '0')
            if root.right:
                travel(root.right, code + '1')
    travel(root, '')
    cur, res = "", ""
    for char in bits:
        if cur not in CodeMap:
            cur += char
        else:
            res += CodeMap[cur]
            cur = char

    return (res + CodeMap[cur]) if len(bits) else ""