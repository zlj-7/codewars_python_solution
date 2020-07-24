def solution(args):
    # TODO: implement
    ans, tmp = [], []
    for arg in args:
        if len(tmp) == 0:
            tmp.append(arg)
        elif len(tmp) < 3:
            # continue
            if arg - tmp[-1] == 1:
                tmp.append(arg)
            else:
                ans.extend(map(str, tmp))
                tmp = [arg]
        else:
            if arg - tmp[-1] == 1:
                tmp.append(arg)
            else:
                ans.append(str(tmp[0]) + '-' + str(tmp[-1]))
                tmp = [arg]
    if len(tmp) != 0:
        if len(tmp) < 3:
            ans.extend(map(str, tmp))
        else:
            ans.append(str(tmp[0]) + '-' + str(tmp[-1]))
    return ",".join(ans)
