# 🧮 Problem 13: Check if two strings are anagrams
# --------------------------------------------------
# Problem Statement:
# Given two strings s1 and s2, determine if they are anagrams of each other.
#
# Two strings are anagrams if they contain the same characters in the same frequency,
# but the order of characters can be different.
#
# Example:
# Input: s1 = "listen", s2 = "silent"
# Output: True
#
# Input: s1 = "hello", s2 = "bello"
# Output: False
#
# Expected:
# - Implement your own logic to check if two strings are anagrams.
# - You can use sorting, dictionaries, or arrays to count character frequencies.



def first(s1,s2):
    temp1 = sorted(s1)
    temp2 = sorted(s2)

    return temp1 == temp2

def second(s1,s2):
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1

    fre2 = {}
    for ch in s2:
        fre2[ch] = fre2.get(ch,0)+1


    return freq == fre2


from collections import Counter
def third(s1,s2):

    return Counter(s1) == Counter(s2)

s1 = input().strip()
s2 = input().strip()
print(first(s1,s2))
print(second(s1,s2))
print(third(s1,s2))