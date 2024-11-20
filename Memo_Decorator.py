
# Decorator that creates hash-table for func results

def memo(func):
    def wrapper(*args, **kwargs):
        try:
            return wrapper.__dict__[str(*args)]
        except:
            wrapper.__dict__[str(*args)] = func(*args, **kwargs)
            return func(*args, **kwargs)
    return wrapper


