# 74. Search a 2D Matrix

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        def getPos(ind, m, n):
            # given ind, an index in row-major format, and mxn matrix, return pos tuple
            return (ind // n, ind % n)
            # for y in range(n-1, -1, -1):
            #     Nx = ind - y
            #     if Nx % n == 0:
            #         return (Nx//n, y)

        left_idx, right_idx = 0, m * n
        while right_idx > left_idx:
            middle_idx = (left_idx + right_idx) // 2
            x, y = getPos(middle_idx, m, n)
            num = matrix[x][y]
            if num > target:
                right_idx = middle_idx
            elif num < target:
                left_idx = middle_idx + 1
            else:
                return True
        return False
