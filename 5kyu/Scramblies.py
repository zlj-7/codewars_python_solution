from collections import Counter
def scramble(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    for key in c2.keys():
        if key not in c1.keys():
            return False
        if c1[key] > c2[key]:
            return False
    return True
