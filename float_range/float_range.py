class float_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            self.start, self.stop = args
            self.step = 1
        elif numargs == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError("Wrong number of arguments")

    def __len__(self):
        diff = self.stop - self.start
        if diff / self.step < 0:
            return 0
        div = diff // self.step
        mod = diff % self.step
        if mod == 0:
            return int(div)
        else:
            return int(div + 1)

    @staticmethod
    def _attrs(range_obj):
        if len(range_obj) == 0:
            return ()
        return next(iter(range_obj)), next(reversed(range_obj)), len(range_obj)

    def __iter__(self):
        i = self.start

        if self.step < 0:
            while i > self.stop:
                yield i
                i += self.step
        else:
            while i < self.stop:
                yield i
                i += self.step

    def __reversed__(self):
        i = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield i
            i -= self.step

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return self._attrs(self) == self._attrs(other)
        return NotImplemented
