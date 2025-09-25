s = "  Hello123 World  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print("upper",s.upper())
print("lower",s.lower())

words = s.split()
print(words)

joined = "".join(words)
print(joined)

print(s.replace("World","galaxy"))


print(s.find("He"))

print(s.count("l"))

print(s.startswith(" "))
print(s.endswith(" "))

str = "saklainshaik"
str2 = "12345"
str3 = str+str2
str4 = "   "

print(str.isalpha())
print(str2.isdigit())
print(str3.isalnum())
print(str4.isspace())

print(str.capitalize())

print(str.title())

str5 = "Saklain Vempalli Shaik"
str6 = str5.split()
print(str6)

str7 = (",").join(str6)
print(str7)

str8 = "abcdefghijklmno"
print(str8[::-1])
print(len(str8))
str91 = "abc"
length = len(str91)
print(length)