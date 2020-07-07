# 73. Set Matrix Zeroes

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_set = set()
        cols_to_set = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_to_set.add(row)
                    cols_to_set.add(col)

        # ALTERNATE for the rest of it
        # for row in range(rows):
        #     if row in rows_to_set:
        #         matrix[row] = [0] * cols
        # for col in range(cols):
        #     if col in cols_to_set:
        #         for row in range(rows):
        #             matrix[row][col] = 0
        for row in range(rows):
            for col in range(cols):
                if row in rows_to_set or col in cols_to_set:
                    matrix[row][col] = 0
