import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# Practical example 1 - Logging

def logger(function):
    def wrapper(*args, **kwargs):
        fname = function.__name__
        value = function(*args, **kwargs)
        with open('decorator_log.txt', 'a+') as f:
            f.write(f"{fname} returned {value} \n")
        print(f"{fname} returned {value}")
        return value

    return wrapper


# Practical example 2 - Timing

def timer(function):
    def wrapper(*args, **kwargs):
        fname = function.__name__
        t0 = time.time()
        value = function(*args, **kwargs)
        t1 = time.time()
        print(f"{fname} took {t1 - t0} s")
        return value

    return wrapper


@logger
def add(x, y):
    return x + y


@timer
def add(x, y):
    return x + y


def repeat(number_of_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(number_of_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(number_of_times=3)
def greet(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    say_hello()
    greet("World")
    add(2, 3)
