"""
Problem: Most Frequently Occurring Letter Pair (start letter, end letter)
Explanation:
Given a sentence S, create pairs from each word using the
first and last letter of that word. Return the pair that occurs most frequently.
If multiple pairs have the same highest frequency, return the one that
appears first in the sentence.
Example:
Input:
she is good grid god and ground player plotter
Output:
gd
"""
s = input().strip()
words = s.split()
order = []
freq = {}

for w in words:
    if len(w) == 0:
        continue
    pair = w[0] + w[-1]
    if pair not in freq:
        freq[pair]=0
        order.append(pair)
    freq[pair] +=1

max_pair = None
max_count = 1
for pair in order:
    if freq[pair] > max_count:
        max_count = freq[pair]
        max_pair = pair
print(max_pair)


