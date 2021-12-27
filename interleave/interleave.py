def interleave(iterable1, iterable2):
    for i, j in zip(iterable1, iterable2):
        yield i
        yield j
