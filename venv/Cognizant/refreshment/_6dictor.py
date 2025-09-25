dict = {"Fname":"saklain","age":23,"Lname":"shaik"}

print(dict["Fname"])

dict["age"] = 24

print(dict)
print(dict.values())
print(dict.keys())



word = "cognizant"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch,0)+1
print(freq)
print(freq.values())