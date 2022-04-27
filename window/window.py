from typing import Iterable
from collections import deque


def window(iterable: Iterable, n: int):
    if n == 0:
        return []

    current_number = deque(maxlen=n)
    for item in iterable:
        current_number.append(item)
        if len(current_number) == n:
            yield tuple(current_number)
