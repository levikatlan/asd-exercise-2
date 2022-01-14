import functools


def exception_safe(f):
    """Makes a function exception-safe by suppressing them"""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # noinspection PyBroadException
        try:
            return f(*args, **kwargs)
        except Exception:
            pass

    return wrapper


@exception_safe
def div(x, y):
    return x / y


if __name__ == '__main__':
    div(1, 0)
