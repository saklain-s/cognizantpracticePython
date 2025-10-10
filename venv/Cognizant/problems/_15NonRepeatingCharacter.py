from collections import Counter
def first_unique_index(s: str) -> int:
    freq=Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
def first_unique_char(s:str):
    freq=Counter(s)
    for ch in s:
        if freq[ch]==1:
            return ch
    return None

def first_unique_dict(s:str)->int:
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    for i in range(len(s)):
        if freq[s[i]]==1:
            return i
    return -1

def first_unique_dict_char(s):
    freq={}

    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None



text = "leetcode"
print(first_unique_index(text))
print(first_unique_char(text))
print(first_unique_dict(text))
print(first_unique_dict_char(text))