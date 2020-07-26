def accum(s):
    return "-".join([c + c.lower()*i for c, i in zip(s.upper(), range(len(s)))])