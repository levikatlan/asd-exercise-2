import inspect


def validate_types(**types):
    """Validates function arguments and returns value types based on the keyword arguments"""

    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            call_args = inspect.getcallargs(f, *args, **kwargs)
            for arg, val in call_args.items():
                if type(val) is not types[arg]:
                    raise ValueError(f'argument "{arg}" must be {types[arg].__name__}')
            return result

        return wrapper

    return decorator


@validate_types(x=int, y=int, return_value=int)
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add(1, 3))  # 4
    print(add('foo', 'bar'))  # ValueError, argument 'x' must be int
