from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """logger wrapper"""
        print(f"--- {function.__name__}: {args} {kwargs} input")
        output = function(*args, **kwargs)
        print(f"--- {function.__name__}: {output} out")
        return output
    return wrapper
