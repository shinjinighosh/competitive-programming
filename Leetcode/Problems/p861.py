# 861. Score After Flipping Matrix

'''
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.
'''


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        res = 0
        for c in range(cols):
            col_sum = 0
            for r in range(rows):
                col_sum += A[r][c] ^ A[r][0]
            res += max(col_sum, rows - col_sum) * 2 ** (cols - 1 - c)
        return res
