import time
from functools import wraps

def timer_func(func):
    
    name = f"{func.__name__!r}"

    @wraps(func)
    def wrap_func(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        time.sleep(1)
        t2 = time.perf_counter()
        print(f'Completed {name} in {"%.2gs" % (t2 - t1)}')
        return result
    return wrap_func