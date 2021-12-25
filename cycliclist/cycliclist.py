from itertools import cycle
from collections import UserList


class CyclicList(UserList):
    def __iter__(self):
        yield from cycle(self.data)
