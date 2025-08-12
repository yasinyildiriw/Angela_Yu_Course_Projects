from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greetings():
    print("How are you")

say_hello()
say_greetings()
say_bye()
