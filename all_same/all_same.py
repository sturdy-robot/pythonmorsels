def all_same(seq):
    it = iter(seq)
    first = next(it, None)
    return all(x == first for x in it)
    