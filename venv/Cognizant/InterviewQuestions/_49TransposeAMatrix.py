# 🧮 Problem 50: Transpose a Matrix
# --------------------------------------------------
# Problem Statement:
# Given a 2D array (matrix), find its transpose.
# The transpose of a matrix is obtained by swapping rows with columns.
#
# Example:
# Input:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# Output:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: create a new matrix and fill transposed elements.
# - Optimized: for square matrices, swap elements in-place.
# - Handle edge cases:
#   → Empty matrix should return an empty list.
#   → Non-square matrices should be transposed into a new matrix.

def brute(matrix):
    if not  matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])

    newMatrix = [[0]*rows for _ in range(cols)]
    n = len(matrix)
    for i in range(rows):
        for j in range(cols):
            newMatrix[j][i] = matrix[i][j]

    return newMatrix
# only works for squared matrix
def optimized(matrix):
    # Only works for square matrices
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

#handels non squared matrix
def transpose(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with dimensions cols x rows
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
r = int(input())
matrix = [list(map(int,input().split())) for i in range(r)]
print(brute(matrix))
print(optimized(matrix))