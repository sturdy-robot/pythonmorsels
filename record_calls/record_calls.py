from functools import wraps


class record_calls:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)
