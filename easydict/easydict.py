class EasyDict:
    def __init__(self, _dict=None, normalize=False, **kwargs):
        self._normalize = normalize
        if _dict is not None:
            self.__dict__.update(_dict)
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def get(self, key, default=None):
        return getattr(self, self.normalized(key), default)

    def normalized(self, key):
        return key.replace(' ', '_') if self._normalize else key

    def __getitem__(self, key):
        return getattr(self, self.normalized(key))

    def __eq__(self, other):
        return (
            self.__dict__ == other.__dict__
            if isinstance(self, EasyDict)
            else NotImplemented
        )

    def __setitem__(self, key, value):
        setattr(self, self.normalized(key), value)

    def __repr__(self):
        return repr(self.__dict__)
