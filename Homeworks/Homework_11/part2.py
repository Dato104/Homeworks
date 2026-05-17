


from functools import wraps

def decorator_operations(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"called function '{func.__name__}', with attributes {args[0]} and {args[1]}, returned {result}")
    return wrapper


@decorator_operations
def add(a, b):
    return a + b

add(10,15)


@decorator_operations
def multiply(a, b):
    return a * b
multiply(10,15)


