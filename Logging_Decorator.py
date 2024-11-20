
#Decorator returns args with which func was called

def logging(func):
    def wrapper(*args, **kwargs):
        print(f'Функция вызвана с параметрами:\n{args, kwargs}')
        return func(*args, **kwargs)
    return wrapper

