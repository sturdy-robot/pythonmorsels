def minmax(lists, *, key=None):
    if not lists:
        raise ValueError("List is empty")

    if key is None:
        return (min(lists), max(lists))
    else:
        return(min(lists, key=key), max(lists, key=key))

