# class MyError(Exception):
#     pass
#
# try:
#     raise MyError("This is my custom error!")
# except MyError as e:
#     print("Caught error:",e)

class AgeLimitError(Exception):
    def __init__(self,age):
        self.age = age
        super().__init__(f"Age {age} is too small! Must be >= 18")

def register(age):
    if age < 18:
        raise AgeLimitError(age)
    print("Registered successfully")

try:
    register(19)
except AgeLimitError as e:
    print("Error:",e)