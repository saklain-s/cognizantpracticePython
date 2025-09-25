"""
How to Attempt?
String Transformation
You are provided with two strings, S1 and S2. In S1, you can perform operations such as
adding, removing or swapping letters. Each operation has a specific cost value
associated with it, as shown below:
. If a letter is removed from S1, the cost is 0.
. If a pair of letters are swapped in S1, the cost is 0.
. If a new letter is added to the end of S1, the cost is 1.
Your task is to find and return an integer value representing the minimum cost required
to transform the string S1 into S2.
Note: The strings S1 and S2 consist uppercase alphabets only.
Input Specification:
input1 : A string value S1 representing the first string.
input2 : A string value S2 representing the target string.
Output Specification:
Return an integer value representing minimum cost required to transform the string
S1 into S2.
inp1 : ABD
inp2 : AABCCAD
"""
from collections import Counter

s1 = input().strip()
s2 = input().strip()

freq = {}
for ch in s1:
    freq[ch] = freq.get(ch,0)+1
cost = 0
freq2 = {}
for ch in s2:
    freq2[ch] = freq2.get(ch,0)+1
for ch in freq2:
    need = freq2[ch] - freq.get(ch,0)
    if need > 0:
        cost+=1

freq3 = Counter(s1)
freq4 = Counter(s2)
diff = freq4 - freq3
cost1 = sum(diff.values())
print(cost1)
