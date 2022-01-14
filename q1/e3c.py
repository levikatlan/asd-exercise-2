import functools


def cache(max_size):
    """Recieves the maximum cache size, and keeps the last recently added values."""

    def decorator(f):
        f.cache = {}

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if args in f.cache:
                return f.cache[args]
            result = f(*args, **kwargs)
            if len(f.cache) >= max_size:
                f.cache.pop(list(f.cache.keys())[0])
            f.cache[args] = result
            return result

        return wrapper

    return decorator


@cache(3)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(2))
    print(fib.cache)
    print(fib(5))
    print(fib.cache)
