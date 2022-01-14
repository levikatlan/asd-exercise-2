import time


def time_execution(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f'{f.__name__} took {end - start:.2f} seconds to execute')
        return result

    return wrapper


@time_execution
def wait(n):
    time.sleep(n)


if __name__ == '__main__':
    wait(1)
    wait(2)
