# 🧮 Problem 49: Spiral Traversal of a 2D Array
# --------------------------------------------------
# Problem Statement:
# Given a 2D array (matrix), print all its elements in spiral order starting from the top-left corner.
#
# Example:
# Input:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: simulate the spiral by keeping track of visited cells.
# - Optimized: use four pointers (top, bottom, left, right) to traverse layers of the matrix.
# - Handle edge cases:
#   → Empty matrix should return an empty list.
#   → Non-square matrices should also work correctly.

# Brute-force: simulate spiral using visited matrix
def brute(matrix):
    if not matrix or not matrix[0]:
        return []

    n, m = len(matrix), len(matrix[0])
    visited = [[False]*m for _ in range(n)]
    result = []

    # directions: right, down, left, up
    dir_r, dir_c = [0, 1, 0, -1], [1, 0, -1, 0]
    r = c = d = 0  # row, col, direction index

    for _ in range(n*m):
        result.append(matrix[r][c])
        visited[r][c] = True

        # compute next cell
        nr, nc = r + dir_r[d], c + dir_c[d]

        # change direction if out of bounds or visited
        if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + dir_r[d], c + dir_c[d]

        r, c = nr, nc

    return result

# Optimized: four-pointer approach
def optimized(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage
r = int(input())
matrix = [list(map(int, input().split())) for _ in range(r)]
print("Brute-force spiral:", brute(matrix))
print("Optimized spiral:", optimized(matrix))
