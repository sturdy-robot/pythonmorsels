from unicodedata import normalize
from abc import ABC, abstractmethod
from functools import total_ordering
from collections import UserString


@total_ordering
class FuzzyOrder(ABC):
    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class FuzzyString(FuzzyOrder, UserString):
    def __lt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self._normalize(str(self.data)) < self._normalize(str(other))

    def __contains__(self, item):
        if not isinstance(item, (FuzzyString, str)):
            return NotImplemented
        if isinstance(item, FuzzyString):
            item = str(item)
        return self._normalize(str(item)) in self._normalize(str(self.data))

    @staticmethod
    def _normalize(text: str):
        return normalize("NFKD", text.casefold())

    def __eq__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self._normalize(str(self.data)) == self._normalize(str(other))
