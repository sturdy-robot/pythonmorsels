from itertools import groupby


def compact(lists):
    for k, _ in groupby(lists):
        yield k
