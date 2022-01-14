def cache(f):
    """Caches function results by argument"""
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        res = f(*args, **kwargs)
        cache[args] = res
        return res

    return wrapper


@cache
def fib(n):
    print(f'computing fib({n})...')
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(3))
    print(fib(5))
