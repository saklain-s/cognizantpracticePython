"""
Title: Minimum Conversions to Make a String Alternating

Problem Statement:
Jacob has a string S containing only the characters 'X' and 'Y'.
A string is considered balanced (alternating) when:
- After every 'X' there is a 'Y' and after every 'Y' there is an 'X'.
- There are no consecutive occurrences of the same character.
  For example, "XYXY" and "YXYX" are balanced, but "XXY", "YYX", or "XXX" are not.

Jacob wants to convert the given string into a balanced string only by interchanging characters
(i.e., changing an 'X' to 'Y' or a 'Y' to 'X') without adding or removing any characters.

Your task is to return the minimum number of character conversions required to make the string balanced.

Input Specification:
- input1 : A string S containing only 'X' and 'Y'.

Output Specification:
- Return an integer: the minimum number of conversions required.

Example:
Input:
S = "XXYYXXY"
Output:
3
"""

def min_conversions_to_alternate(S: str) -> int:
    # Pattern 1: Starting with 'X' -> "XYXYXY..."
    pattern1 = ''.join('X' if i % 2 == 0 else 'Y' for i in range(len(S)))
    # Pattern 2: Starting with 'Y' -> "YXYXYX..."
    pattern2 = ''.join('Y' if i % 2 == 0 else 'X' for i in range(len(S)))

    # Count mismatches for both patterns
    changes1 = sum(1 for i in range(len(S)) if S[i] != pattern1[i])
    changes2 = sum(1 for i in range(len(S)) if S[i] != pattern2[i])

    return min(changes1, changes2)


# ----------- User Input ------------
S = input("Enter a string containing only 'X' and 'Y': ").strip().upper()

# Optional: validate input
if not S or any(ch not in ('X', 'Y') for ch in S):
    print("Invalid input! Please enter a string containing only 'X' and 'Y'.")
else:
    print("Minimum conversions required:", min_conversions_to_alternate(S))
