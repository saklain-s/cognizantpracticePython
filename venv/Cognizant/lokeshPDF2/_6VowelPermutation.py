import math
"""
Problem: Vowel Permutation

Explanation:
Given a string S, count the number of permutations of all the consonants
while keeping the positions of the vowels fixed.  
• Vowels (a, e, i, o, u) remain in their original positions.  
• Only the consonant characters are permuted.  
• If there are no consonants, the result should be 0.

Example:
Input : "ABC"
Step  : Vowels → A
        Consonants → B, C  → 2 consonants
Permutations of consonants = 2! = 2
Output: 2
"""

s= input().strip()
vowels = set("aieouAEIOU")

consonants = [ch for ch in s if ch not in vowels]
k = len(consonants)
if k == 0:
    print(0)
else:
    print(math.factorial(k))
