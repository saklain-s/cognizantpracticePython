from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    temp1 = sorted(s1)
    temp2 = sorted(s2)
    if temp1 == temp2:
        return True
    else:
        return False

def is_anagramDict(s1: str, s2: str) -> bool:
    freq1={}
    for ch in s1:
        freq1[ch] = freq1.get(ch,0)+1

    freq2 = {}
    for ch in s1:
        freq2[ch] = freq2.get(ch,0)+1
    if freq1 == freq2:
        return True
    else: return False

def is_anagramCounter(s1: str, s2: str) -> bool:
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False



text1 = "silent"
text2 = "listen"

anagram = is_anagram(text1,text2)
if anagram:
    print("Anagram")
