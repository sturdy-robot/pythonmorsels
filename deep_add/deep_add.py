from numbers import Number

def deep_add(seq, start=0):
    if isinstance(seq, Number):
        return seq
    return sum((deep_add(x) for x in seq), start)
