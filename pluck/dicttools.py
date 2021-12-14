def pluck(data: dict, key: str, sep: str = '.', default=object()):
    key = key.split(sep)
    d = data
    for k in key:
        d = d[k]

    return d
