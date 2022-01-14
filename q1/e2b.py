def trace(f):
    """Reports arguments, returns values and errors"""

    def format_args(args, kwargs):
        str_kwargs = ", ".join((f"{k}={v}" for k, v in kwargs.items()))
        str_args = ", ".join(map(str, args))
        has_comma = (str_kwargs and ", ") or ''
        return str_args + has_comma + str_kwargs

    def wrapper(*args, **kwargs):
        try:
            print(f'enter {f.__name__}({format_args(args, kwargs)})')
            result = f(*args, **kwargs)
            print(f'leave {f.__name__}({format_args(args, kwargs)}): {result}')
        except Exception as error:
            print(f'leave {f.__name__}({format_args(args, kwargs)}):on error {error}')
            result = error
        return result

    return wrapper


@trace
def div(x, y):
    return x / y


if __name__ == '__main__':
    print(div(4, 2))
    print(div(x=1, y=0))
    print(div(1, y=2))
