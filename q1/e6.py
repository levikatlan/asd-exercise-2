import threading
import time


def synchronize(lock):
    """Synchronizes function with respect to some lock"""

    def decorator(f):
        def wrapper(*args, **kwargs):
            with lock:
                result = f(*args, **kwargs)
            return result

        return wrapper

    return decorator


lock = threading.Lock()


@synchronize(lock=lock)
def f():
    time.sleep(1)
    print('f')


@synchronize(lock=lock)
def g():
    time.sleep(1)
    print('g')


if __name__ == '__main__':
    threading.Thread(target=f).start()
    threading.Thread(target=g).start()
