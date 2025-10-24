def decorator1(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator1
def say_hello():
    print("Hello!0")

say_hello()
