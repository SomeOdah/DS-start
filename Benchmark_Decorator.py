import time

# This decorator returns time to execute func

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return f'Время выполнения функции {func.__name__} потребовалось {end - start:.15f}'
    return wrapper

