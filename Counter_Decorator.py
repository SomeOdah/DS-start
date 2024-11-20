
# Decorator that returns number of times func been executed

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функция была вызвана: {wrapper.call_count} раз")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


