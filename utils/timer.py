import functools
import time
import datetime

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # 2
        run_time = end_time - start_time # 3
        
        #print(f"Finished {func.__name__!r} in {run_time: .4f} secs") # wrapper version of the name
        print(f"{func.__name__} runtime: {str(datetime.timedelta(seconds=run_time))}")
        return value
    return wrapper_timer