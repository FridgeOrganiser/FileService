"""Module for declaring usefull decorators."""
from functools import wraps


def error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)

    return wrapper


