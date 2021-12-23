class LoopInfo:
    def __init__(self, index, current, is_last, previous, next_item):
        self.index = index
        self.current = current
        self.previous = previous
        self.next = next_item
        self.is_first = index == 0
        self.is_last = is_last


def loop_helper(iterable, previous_default=None, next_default=None):
    for index, item in enumerate(iterable):
        previous = iterable[index-1] if index > 0 else previous_default
        try:
            next_item = iterable[index+1] if index < len(iterable) else next_default
        except IndexError:
            next_item = next_default
        is_last = index == len(iterable) - 1
        yield item, LoopInfo(index, item, is_last, previous, next_item)
