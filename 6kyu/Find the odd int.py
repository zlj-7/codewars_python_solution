def find_it(seq):
    # TODO: implement
    ans = 0
    for val in seq:
        ans ^= val
    return ans