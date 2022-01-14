def trace(f=None, *, log=print):
    def format_args(args, kwargs):
        str_kwargs = ", ".join((f"{k}={v}" for k, v in kwargs.items()))
        str_args = ", ".join(map(str, args))
        has_comma = (str_kwargs and ", ") or ''
        return str_args + has_comma + str_kwargs

    if f is None:
        return lambda f: trace(f, log=log)

    def wrapper(*args, **kwargs):
        log(f'enter {f.__name__}({format_args(args, kwargs)})')
        result = f(*args, **kwargs)
        log(f'leave {f.__name__}({format_args(args, kwargs)}): {result}')
        return result

    return wrapper


@trace()
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(3))
