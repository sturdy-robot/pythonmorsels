from functools import wraps
# from contextlib import contextmanager
# from dataclasses import dataclass
# from types import TracebackType
# from typing import Optional


# @dataclass
# class SuppressedException:
#     exception: Optional[Exception] = None
#     traceback: Optional[TracebackType] = None


# @contextmanager
# def suppress(*error):
#     info = SuppressedException(exception=None, traceback=None)
#     try:
#         yield info
#     except error as e:
#         info.exception = e
#         info.traceback = e.__traceback__
    


class suppress:
    def __init__(self, *error: Exception):
        self.e = error
        self.exception = None
        self.traceback = None

    def __call__(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            with self:
                return function(*args, **kwargs)
        
        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, exc, exc_val, traceback):
        self.exception = exc_val
        self.traceback = traceback

        return isinstance(exc_val, self.e)