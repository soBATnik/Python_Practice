import time

def time_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
    return wrapper


@time_decorator
def time_sleep(x):
    time.sleep(x)

time_sleep(5)