import functools


def cache(f):
    """Exposes cache as the cache attribute of a function"""
    f.cache = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if args in f.cache:
            return f.cache[args]
        res = f(*args, **kwargs)
        f.cache[args] = res
        return res

    return wrapper


@cache
def fib(n):
    print(f'computing fib({n})...')
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(3))
    print(fib.cache)
    print(fib(5))
    print(fib.cache)
