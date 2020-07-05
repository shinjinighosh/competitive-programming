# 766. Toeplitz Matrix

'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
'''


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        starters = [(i, 0) for i in range(M)]
        for i in range(N):
            starters.append((0, i))
        starters.remove((0, 0))  # because it was added twice
        for start_x, start_y in starters:
            init = matrix[start_x][start_y]
            while start_x < M and start_y < N:
                if matrix[start_x][start_y] != init:
                    return False
                start_x += 1
                start_y += 1
        return True
