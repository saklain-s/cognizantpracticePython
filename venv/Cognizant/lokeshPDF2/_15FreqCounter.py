"""
Problem: Most Frequent Frequency
You are given a string S of length N containing uppercase English alphabets.
Your task is to find the frequency which occurs for the maximum number of letters
in the string. If multiple frequencies occur the same maximum number of times,
choose the smallest frequency.
Steps to solve:
1. Find the frequency of each letter in the string.
2. Find the frequency of the frequencies (i.e., count how many letters share the same frequency).
3. Return the frequency which occurred for the maximum number of letters.
   - If there is a tie, return the smallest frequency.
Input Specification:
input1 : An integer N representing the length of the string.
input2 : A string S containing uppercase English letters.
Output Specification:
- Return an integer representing the frequency which occurs for the maximum letters.
Example 1:
Input:
N = 9
S = "ACABABCCA"
Output:
2
Explanation:
- Letter frequencies: A:4, B:2, C:3
- Frequency of frequencies: 2→1, 3→1, 4→1
- All frequencies occur equally, so choose the smallest → 2

Example 2:
Input:
N = 20
S = "ACABDDABDCDACFAEGFDA"
Output:
1
Explanation:
- Letter frequencies: A:6, B:2, C:3, D:5, E:1, F:2, G:1
- Frequency of frequencies: 1→2 (E,G), 2→2 (B,F), 3→1, 5→1, 6→1
- Max occurrence is 2 (frequency 1 and 2), choose the smallest → 1
"""
# Read input
N = int(input())
S = input()

# Step 1: Count letter frequencies
freq = {}
for ch in S:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Step 2: Count frequency of frequencies
freq_of_freq = {}
for f in freq.values():
    freq_of_freq[f] = freq_of_freq.get(f, 0) + 1
print(freq_of_freq)

# Step 3: Find the frequency with the maximum occurrence
# If tie, choose the smallest frequency
max_occurrence = 0
result = 0
for f in freq_of_freq:
    if freq_of_freq[f] > max_occurrence:
        max_occurrence = freq_of_freq[f]
        result = f
    elif freq_of_freq[f] == max_occurrence:
        result = min(result, f)

print(result)
