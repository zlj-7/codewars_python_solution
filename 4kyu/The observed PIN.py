def get_pins(observed):

    if observed == '':
        return []

    digit_map = {
      '1' : ['2', '4'],
      '2' : ['1', '3', '5'],
      '3' : ['2', '6'],
      '4' : ['1', '5', '7'],
      '5' : ['2', '4', '6', '8'],
      '6' : ['3', '5', '9'],
      '7' : ['4', '8'],
      '8' : ['5', '7', '9', '0'],
      '9' : ['6', '8'],
      '0' : ['8']
    }

    Q = [observed[0]]
    Q.extend(digit_map[observed[0]])

    res = []


    while len(Q) != 0:

        cur = Q.pop()
        if len(cur) < len(observed):
            Q.append(cur + observed[len(cur)])
            Q.extend([cur + char for char in digit_map[observed[len(cur)]]])
        else:
            res.append(cur)

    return res
