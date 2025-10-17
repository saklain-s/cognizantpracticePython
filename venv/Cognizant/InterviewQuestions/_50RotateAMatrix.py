# 🧮 Problem 51: Rotate a Matrix by 90 Degrees
# --------------------------------------------------
# Problem Statement:
# Given a 2D array (matrix), rotate it 90 degrees clockwise.
#
# Example:
# Input:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Output:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: create a new matrix and fill rotated elements.
# - Optimized: for square matrices, rotate in-place using transpose + reverse rows.
# - Handle edge cases:
#   → Empty matrix should return an empty list.
#   → Non-square matrices should be rotated into a new matrix.
def brute(matrix):
    if not matrix and not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    # Create a new matrix with swapped dimensions
    rotated = [[0] * rows for _ in range(cols)]

    # Fill rotated matrix
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = matrix[i][j]

    return rotated


def optimized(matrix):
    if not matrix and not matrix[0]:
        return []
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix


r = int(input())
matrix = [list(map(int,input().split()))for _ in range(r)]
print(optimized(matrix))