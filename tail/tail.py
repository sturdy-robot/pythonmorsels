def tail(iterables, n):
    if n <= 0:
        return []

    it = list(iterables)
    return it[-n:]
    