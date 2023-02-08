from itertools import tee
from typing import NamedTuple, Any
DEFAULT_VALUE = object()


def minmax2(*lst, key=None, default=DEFAULT_VALUE):
    l = iter(*lst)
    l, l2, l3 = tee(l, 3)

    try:
        next(l3)
    except StopIteration:
        if default == DEFAULT_VALUE:
            raise ValueError
        return default, default

    return MinMax(min(l, default=default, key=key), max(l2, default=default, key=key))


class MinMax(NamedTuple):
    min: Any
    max: Any
