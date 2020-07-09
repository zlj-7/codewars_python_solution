def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_dict = {
        'year': 0,
        'day': 0,
        'hour': 0,
        'minute': 0,
        'second': 0,
    }
    time_spend = {
        'year': 365 * 24 * 60 * 60,
        'day': 24 * 60 * 60,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1,
    }
    remain = seconds
    for opt in ['year', 'day', 'hour', 'minute', 'second']:

        cur = remain // time_spend[opt]
        if cur == 0:
            continue
        time_dict[opt] = cur
        remain -= cur * time_spend[opt]

    res = []

    for opt in ['year', 'day', 'hour', 'minute', 'second']:
        if time_dict[opt] != 0:
            if time_dict[opt] > 1:
                res.append(f'{time_dict[opt]} {opt}s')
            else:
                res.append(f'{time_dict[opt]} {opt}')

    return (", ".join(res[:-1]) + ' and ' + res[-1]) if len(res) > 1 else res[0]