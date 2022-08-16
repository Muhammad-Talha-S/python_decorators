import time
import logging
from functools import wraps

def timer_func(func):
    
    name = f"{func.__name__!r}"

    @wraps(func)
    def wrap_func(*args, **kwargs):
        logging.basicConfig(filename='timer.log',level=logging.DEBUG)
        logging.debug(f'Start {name}')
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        logging.debug(f'Completed {name} in {"%.2gs" % (t2 - t1)}')
        return result
    return wrap_func