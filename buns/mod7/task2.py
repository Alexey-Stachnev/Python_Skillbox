import functools
from typing import Callable, Dict

DICT: Dict[int, tuple[int, str, str]] = {}

def memoize(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(num: int) -> int:
        if num in DICT.keys():
            return DICT[num][0]
        result = func(num)
        DICT[num] = (result, func.__name__, func.__doc__)
        return result
    return wrapped_func
