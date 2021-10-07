def tail(iterables, n):
    if n <= 0:
        return []
    
    it = [i for i in iterables]
    return it[-n:]
    