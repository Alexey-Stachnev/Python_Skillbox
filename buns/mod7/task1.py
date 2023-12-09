from typing import Callable


def validate_args(func: Callable) -> Callable:
    """
    Декоратор, проверяющий корректность переденных данных
    """

    def wrapped_func(*args: list):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(args)

    return wrapped_func
