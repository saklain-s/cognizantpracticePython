try:
    x = int(input())
    y = int(input())
    print(x//y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input, numbers only")