from typing import Iterable


def chunked(sequence: Iterable, n: int):
    l = []
    for item in sequence:
        l.append(item)
        if len(l) == n:
            yield l
            l = []
    if l:
        yield l
