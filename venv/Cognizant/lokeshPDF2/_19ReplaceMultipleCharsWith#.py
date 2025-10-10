"""
Problem:
Given a string S, replace every group of two or more consecutive identical characters
with a single '#'. After that, if multiple '#' characters appear consecutively,
compress them into a single '#'. Return the final modified string.
"""

def transform_string(s: str) -> str:
    result = []
    i = 0
    n = len(s)

    while i < n:
        j = i
        while j < n and s[i]==s[j]:
            j+=1
        run_len = j - i
        if run_len >=2:
            if not result or result[-1] != '#':
                result.append('#')
        else:
            result.append(s[i])
        i = j
    return ''.join(result)


text = input().strip()
print(transform_string(text))
