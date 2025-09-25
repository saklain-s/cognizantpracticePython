def greet(x):
    message = "Hello "+x
    return f"Hello, {x}"

print(greet("Saklain"))

#default parameters
def power(base,exp=2):
    return base ** exp

print(power(3))
print(power(3,3))


#args
def add(*number):
    return sum(number)

print(add(1,2,3,5,6,6,7))

#*kwargs

def dict(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

dict(name="saklain", age=21)


square = lambda x: x*x
print(square(5))


def factorial(n):
    if n == 0 or n ==1:
        return 1
    return  n * factorial(n-1)

print(factorial(5))
