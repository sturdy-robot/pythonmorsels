from itertools import zip_longest


def zip_discard_gen(*iterables, sentinel=object()):
    return ((entry for entry in iterable if entry is not sentinel)
            for iterable in zip_longest(*iterables, fillvalue=sentinel))


def interleave(*iterables):
    for i in zip_discard_gen(*iterables):
        yield from i
