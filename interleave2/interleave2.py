from itertools import cycle


def interleave(*args):
    return map(next, cycle(map(iter, args)))
