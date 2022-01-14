def trace(log):
    """receive the printing function as an argument"""
    padding_length = 0

    def decorator(f):
        def format_args(args, kwargs):
            str_kwargs = ", ".join((f"{k}={v}" for k, v in kwargs.items()))
            str_args = ", ".join(map(str, args))
            has_comma = (str_kwargs and ", ") or ''
            return str_args + has_comma + str_kwargs

        def wrapper(*args, **kwargs):
            nonlocal padding_length
            log(f'{" " * padding_length}enter {f.__name__}({format_args(args, kwargs)})')
            padding_length += 1
            result = f(*args, **kwargs)
            padding_length -= 1
            log(f'{" " * padding_length}leave {f.__name__}({format_args(args, kwargs)}): {result}')
            return result

        return wrapper

    return decorator


@trace(print)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(3))
