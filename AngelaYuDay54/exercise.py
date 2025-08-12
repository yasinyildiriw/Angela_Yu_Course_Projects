import time

def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        finish_time = time.time()
        result = finish_time - current_time
        print(result)

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(100000):
        i*i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i*i


fast_function()
slow_function()
