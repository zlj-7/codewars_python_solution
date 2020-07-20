from collections import defaultdict

def mix(s1, s2):
    # TODO: implement
    MapS1 = defaultdict(int)
    MapS2 = defaultdict(int)
    for c1 in s1:
        if c1.islower():
            MapS1[c1] += 1
    for c2 in s2:
        if c2.islower():
            MapS2[c2] += 1
    info = []
    all_char = MapS1.keys() | MapS2.keys()
    for c in all_char:
        s1_c = MapS1[c] if c in MapS1.keys() else 0
        s2_c = MapS2[c] if c in MapS2.keys() else 0
        if max(s1_c, s2_c) <= 1:
            continue
        if s1_c > s2_c:
            info.append((1, c, s1_c))
        elif s1_c < s2_c:
            info.append((2, c, s2_c))
        else:
            info.append((3, c, s1_c))
    info.sort(key = lambda x:(-x[2], x[0], x[1]))
    ans = []
    for item in info:
        tmp = ""
        if item[0] == 3:
            tmp += "=:" + item[1] * item[2]
        elif item[0] == 1:
            tmp += "1:" + item[1] * item[2]
        else:
            tmp += "2:" + item[1] * item[2]
        ans.append(tmp)
    return "/".join(ans)