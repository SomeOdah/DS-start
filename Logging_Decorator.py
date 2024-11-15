
#Decorator returns args with which func was called

def logging(func):
    def wrapper(*args, **kwargs):
        return f'Функция вызвана с параметрами:\n{args, kwargs}'
    return wrapper

