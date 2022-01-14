import functools


def cache(f=None, *, max_size=None):
    if f is None:
        return lambda f: cache(f, max_size=max_size)
    f.cache = {}
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if args in f.cache:
            return f.cache[args]
        result = f(*args, **kwargs)
        if max_size and len(f.cache) >= max_size:
            f.cache.pop(list(f.cache.keys())[0])
        f.cache[args] = result
        return result

    return wrapper


@cache
def fib1(n):
    print(f'computing fib1({n})...')
    return n if n < 2 else fib1(n - 1) + fib1(n - 2)


@cache(max_size=3)
def fib2(n):
    print(f'computing fib2({n})...')
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    fib1(8)  # unlimited
    print(fib1.cache)
    fib2(2)
    print(fib2.cache)
    fib2(5)
    print(fib2.cache)
