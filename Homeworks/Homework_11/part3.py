

import time

def delayed_repeat(times=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                time.sleep(delay)
                func(*args, **kwargs)
            return
        return wrapper
    return decorator



@delayed_repeat(5,2)
def greeting(greet):
    print(f"Welcome, {greet}!")

greeting("Dato")















































