def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18+ to register")
    print("valid age")

try:
    check_age(15)
except ValueError as e:
    print("Error",e)