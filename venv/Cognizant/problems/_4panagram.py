# from collections import Counter
#
# text1 = input().lower()
# text2 = input().lower()
#
# temp1 = ''.join(sorted(text1))
# temp2 = ''.join(sorted(text2))
#
# if temp1 == temp2:
#     print("Anagrams")
# else:
#     print("no")
#
# freq1 = {}
# for ch in text1:
#     freq1[ch] = freq1.get(ch,0)+1
#
# freq2 = {}
# for ch in text2:
#     freq2[ch] = freq2.get(ch,0)+1
#
# if freq1 == freq2:
#     print("Anagrams")
# else:
#     print("No")
#
# if Counter(text1) == Counter(text2):
#     print("Anagrams")
# else:
#     print("No")
#
# # str1 = input().lower()
# # str2 = input().lower()
# #
# # temp1 = ''.join(sorted(str1))
# # temp2 = ''.join(sorted(str2))
# #
# # if temp1 == temp2:
# #     print("Anagrams")
# # else:
# #     print("No")
# #
# # dict1 ={}
# # for ch in str1:
# #     dict1[ch] = dict1.get(ch,0)+1
# #
# # dict2={}
# # for ch in str2:
# #     dict2[ch] = dict2.get(ch,0)+1
# #
# # if dict1 == dict2:
# #     print("Anagrams")
# # else:
# #     print("No")
# #
# # from collections import Counter
# #
# # if Counter(str1) == Counter(str2):
# #     print("Anagrams")
# # else:
# #     print("No")
#
#
#


text1 = input().lower()
text2 = input().lower()

newText1 = ''.join(sorted(text1))
newText2 = ''.join(sorted(text2))

if newText1 == newText2:
    print("anangrams")
else:
    print("No")

freq = {}
for ch in text1:
    freq[ch] = freq.get(ch,0)+1

freq2 = {}
for ch in text2:
    freq2[ch] = freq2.get(ch,0)+1
if freq2 == freq:
    print("Anagrams")
else:
    print("No")

from collections import Counter

if Counter(text1) == Counter(text2):
    print("Anagrams")
else:
    print("No they are not")