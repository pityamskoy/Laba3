import time

def timeit_once(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result:list = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} has execution time={end_time - start_time:.5f} seconds.")
        return result
    return wrapper