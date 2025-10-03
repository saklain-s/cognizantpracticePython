from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def is_anagramDict(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    freq1 = {}
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    freq2 = {}
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    return freq1 == freq2

def is_anagramCounter(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


text1 = "silent"
text2 = "listen"

if is_anagram(text1, text2):
    print("Anagram")

if is_anagramDict(text1, text2):
    print("Anagram")

if is_anagramCounter(text1, text2):
    print("Anagram")
