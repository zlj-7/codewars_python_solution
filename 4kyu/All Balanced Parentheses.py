def balanced_parens(n):
    # Your code here!
    res = []
    def dfs(l, r, cur):
        if len(cur) == 2*n:
            res.append(cur)
        else:
            if r < l:
                dfs(l, r+1, cur + ')')
            if l < n:
                dfs(l+1, r, cur + '(')
    dfs(0, 0, "")
    return res if res != [] else [""]