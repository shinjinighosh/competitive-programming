# 1351. Count Negative Numbers in a Sorted Matrix

'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.
'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if grid[i][j] < 0:
                    res += 1
                else:
                    break
        return res
