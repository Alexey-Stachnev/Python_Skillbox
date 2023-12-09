import time
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

def time_decorator(func):
    def wrapper_func(*args, **kwargs):
        if not hasattr(wrapper_func, 'start_time'):
            wrapper_func.start_time = time.time()
            result = func(*args, **kwargs)
            wrapper_func.end_time = time.time()
            print(f"Функция {func.__name__} выполнялась {wrapper_func.end_time - wrapper_func.start_time} секунд")
            delattr(wrapper_func, 'start_time')
            delattr(wrapper_func, 'end_time')
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper_func

@memoize
@time_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@time_decorator
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))
print(fibonacci_1(50))