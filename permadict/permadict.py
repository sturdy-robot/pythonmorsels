from collections.abc import MutableMapping


class PermaDict(MutableMapping):
    def __init__(self, mapping=(), silent=False, **kwargs):
        self._mapping = dict(mapping)
        self.silent = silent
        e = dict(kwargs)
        self._mapping.update(e)

    def force_set(self, key, value):
        self._mapping[key] = value

    def __setitem__(self, key, value) -> None:
        if key in self._mapping.keys():
            if self.silent:
                return
            raise KeyError
        self._mapping[key] = value

    def __delitem__(self, value) -> None:
        self._mapping.pop(value)

    def __len__(self) -> int:
        return len(self._mapping)

    def __iter__(self):
        yield from self._mapping

    def __getitem__(self, key):
        return self._mapping[key]
