class ReverseView:
    def __init__(self, args):
        self.x = args

    def __iter__(self):
        yield from reversed(self.x)

    def __getitem__(self, index):
        i = len(self.x) - 1 - index if index >= 0 else abs(index) - 1
        return self.x[i]

    def __len__(self):
        return len(self.x)

    def __str__(self):
        return f"{list(reversed(self.x))}"

    def __repr__(self):
        return f"{list(reversed(self.x))}"
