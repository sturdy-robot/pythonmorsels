def sum_timestamps(times):
    sum_ts = 0
    for time in times:
        if len(time.split(':')) > 2:
            h, m, s = time.split(':')
            h = int(m) * 3600
            sum_ts += h
        else:
            m, s = time.split(':')

        m = int(m) * 60
        s = int(s) + m
        sum_ts += s

    m = int(sum_ts / 60)
    s = int(sum_ts % 60)

    if m > 59:
        h = int(sum_ts / 3600)
        m = int((sum_ts % 3600) / 60)

        return f'{h}:{m:02d}:{s:02d}'

    return f'{m}:{s:02d}'
