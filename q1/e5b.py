import functools
import inspect


def exception_safe(*args):

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*fargs, **fkwargs):
            try:
                return f(*fargs, **fkwargs)
            except Exception as error:
                if inspect.isfunction(args[0]):
                    print('Suppressing no params...')
                elif issubclass(error.__class__, args):
                    print('Suppressing given...')
                else:
                    raise error

        return wrapper

    if inspect.isfunction(args[0]):
        return decorator(args[0])

    return decorator


@exception_safe(ValueError, NameError)
def err(error):
    print(f'raising {error} error')
    raise error


if __name__ == '__main__':
    err(ValueError)
    err(NameError)
    err(TypeError)
