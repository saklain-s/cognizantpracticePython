import math
"""You are given:

N → the number of strings

A list of N strings

Goal:

For each string:

Remove all vowels (a, e, i, o, u and their uppercase forms).

Count how many characters remain.

Find the number of permutations of those remaining characters.
Since the question says consider all the letters as different
→ order matters and we treat identical letters as distinct.
→ Permutation count = factorial of length of the remaining string.

Among all the strings, find the maximum permutation count.

If all strings have no remaining characters → return 0."""

n = int(input())
arr = [input().strip() for _ in range(n)]

vowels = set("aeiouAEIOU")
max_perm = 0
for s in arr:
    remaining = [ch for ch in s if ch not in vowels]
    k = len(remaining)
    if k > 0:
        perms = math.factorial(k)
        max_perm = max(max_perm,perms)
print(max_perm)