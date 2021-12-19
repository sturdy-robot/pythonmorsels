DEFAULT_VALUE = object()


def minmax2(lst, *, key=None, default=DEFAULT_VALUE):
    if not lst:
        if default == DEFAULT_VALUE:
            raise ValueError
        return default, default

    if not isinstance(lst, list):
        lst = iter(lst)

    if key is None:
        return min(lst), max(lst)
    else:
        return min(lst, key=key), max(lst, key=key)
