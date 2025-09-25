
"""
Problem Description
You are given a string S consisting of lowercase English letters.
You have to generate a new expanded string where each character in S repeats equal to its first index occurrence.
The characters in the output string should be separated by hyphens ('-').
Note: Assume 1-based ind
Input Specification
input1:A string S consisting of lowercase English letters.
Output Specification
Return a string formatted as described, with characters separated by hyphens ('-').
Example
Input:
abcaba
Output:
a-bb-ccc-a-bb-a
"""
from distutils.command.build_scripts import first_line_re


def expand_String(s):
    first_index = {}
    result = []

    for i, ch in enumerate(s):
        if ch not in first_index:
            first_index[ch] = i + 1
        result.append(ch * first_index[ch])
    return '-' .join(result)

s = input()
print(expand_String(s))

