def hashable(v):
    try:
        hash(v)
    except TypeError:
        return False
    return True


def uniques_only(seq):
    seen = set()
    seen_add = seen.add
    gen = (
        x for x in seq if not (x in seen or seen_add(x)) and hashable(x)
    )
    yield from gen
