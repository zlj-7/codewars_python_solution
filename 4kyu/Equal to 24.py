from collections import Counter
def equal_to_24(a, b, c, d):
    arr_lists = set()
    cnt = Counter([a, b, c, d])
    def find_all(arr, cnt):
        if len(arr) == 4:
            arr_lists.add(tuple(arr))
        else:
            for num in [a, b, c, d]:
                if cnt[num] > 0:
                    cnt[num] -= 1
                    find_all(arr + [num], cnt)
                    cnt[num] += 1
    find_all([], cnt)
    result = None
    def dfs(pos, left, exp):
        nonlocal result
        if pos == 4:
            try:
                if eval(exp) == 24:
                    result = exp
            except Exception:
                pass
        if result == None and pos < 4:
            cur_num = str(arr[pos])
            if pos == 3:
                dfs(pos+1, 0, exp + cur_num + ')'*left)
            else:
                #decrease or not change
                for i in range(left+1):
                    part_exp = cur_num + ')' * i
                    for opt in ['+','-','*','/']:
                        dfs(pos+1, left-i, exp + part_exp + opt)
                #increase
                part_exp = '(' + cur_num
                for opt in ['+', '-', '*', '/']:
                    dfs(pos+1, left+1, exp + part_exp + opt)
    for arr in arr_lists:
        dfs(0, 0, "")
        if result:
            return result
    return "It's not possible!"
