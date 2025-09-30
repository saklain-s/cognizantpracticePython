str1 = input()
cnt = 0
for ch in str1:
    if ch == 'a' or ch == 'e' or ch =='i' or ch== 'o' or ch =='u' or ch =='A' or ch == 'E' or ch== 'I' or ch =='O' or ch =='U':
        cnt+=1
print(cnt)

cnt2=0
str2 = input()
for ch in str2:
    if ch in "aeiouAEIOU":
        cnt2+=1
print(cnt2)

# Read input
S = input().strip()

# Set of vowels (both lowercase & uppercase)
vowels = set("aeiouAEIOU")

# Counter
count = 0

# Check each character
for ch in S:
    if ch in vowels:
        count += 1

# Output the total vowel count
print(count)
