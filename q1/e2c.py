def trace(f):
    """Shows nesting using indentation of recursive function"""
    padding_length = 0

    def format_args(args, kwargs):
        str_kwargs = ", ".join((f"{k}={v}" for k, v in kwargs.items()))
        str_args = ", ".join(map(str, args))
        has_comma = (str_kwargs and ", ") or ''
        return str_args + has_comma + str_kwargs

    def wrapper(*args, **kwargs):
        nonlocal padding_length
        print(f'{" " * padding_length}enter {f.__name__}({format_args(args, kwargs)})')
        padding_length += 1
        result = f(*args, **kwargs)
        padding_length -= 1
        print(f'{" " * padding_length}leave {f.__name__}({format_args(args, kwargs)}): {result}')
        return result

    return wrapper


@trace
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(3))
