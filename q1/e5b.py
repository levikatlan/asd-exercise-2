import functools
import inspect


def exception_safe(*args):
    if inspect.isfunction(args[0]):
        print('no params passed')
        f = args[0]

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*fargs, **fkwargs):
            try:
                return f(*fargs, **fkwargs)
            except args:
                print('no error')

        return wrapper

    return decorator


@exception_safe(ValueError, NameError)
def err(error):
    raise error


if __name__ == '__main__':
    err(ValueError)
    err(TypeError)
