# -*- coding:utf-8 -*-

def to_chinese_numeral(n):

    num_str = str(n)
    if num_str[0] == '-':
        ans = '负'
        num_str = num_str[1:]
    else:
        ans = ''
    if '.' in num_str:
        part1, part2 = num_str.split('.')
    else:
        part1 = num_str
        part2 = None
    ans += transform(part1, True) + transform(part2, False)
    return ans

def transform(part, mode):
    if part == None:
        return ""
    numerals = {
        "-": "负",
        ".": "点",
        "0": "零",
        "1": "一",
        "2": "二",
        '3': "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九",
        "10": "十",
        "100": "百",
        "1000": "千",
        "10000": "万"
    }
    if mode == False:
        res = "点"
        for char in part:
            res += numerals[char]
        if res[-1] == '零':
            return res[:-1]
        else:
            return res
    else:
        res = ""
        base = int(10 ** (len(part)-1))
        for char in part:
            if char == '0':
                if len(res) == 0 or res[-1] != '零':
                    res += '零'
            else:
                prefix = numerals[char]
                if base >= 10:
                    next_ = numerals[str(base)]
                else:
                    next_ = ""
                res += prefix + next_
            base //= 10

        if len(res) == 1:
            return res
        if res[-1] == '零':
            res = res[:-1]
        if res.startswith('一十'):
            res = res[1:]
        return res