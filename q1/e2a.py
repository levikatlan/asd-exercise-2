def trace(f):
    """Traces whenever a function is invoked and whenever it returns"""

    def wrapper(*args, **kwrags):
        print(f'enter {f.__name__}')
        result = f(*args, **kwrags)
        print(f'leave {f.__name__}')
        return result

    return wrapper


@trace
def inc(x):
    return x + 1


if __name__ == '__main__':
    print(inc(1))
