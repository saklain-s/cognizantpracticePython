class Student:
    def __init__(self, name, age, grade):
        self.name = name          # Public
        self._age = age           # Protected
        self.__grade = grade      # Private

    def show_info(self):
        print(f"Name: {self.name}")       # Accessing public
        print(f"Age: {self._age}")        # Accessing protected
        print(f"Grade: {self.__grade}")   # Accessing private
# Create object
s = Student("Saklain", 21, "A")
# 1️⃣ Public Access
print(s.name)       # ✅ Works
# 2️⃣ Protected Access
print(s._age)       # ⚠️ Works, but not recommended
# 3️⃣ Private Access
# print(s.__grade)  # ❌ Error: 'Student' object has no attribute '__grade'
# ✅ Correct (but discouraged) way using name mangling
print(s._Student__grade)
# Method can access all (public, protected, private)
s.show_info()