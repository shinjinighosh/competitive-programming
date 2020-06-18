# 1252. Cells with Odd Values in a Matrix

'''
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
'''


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # O(mnk) solution: for every cell, add to res if it ends up odd
        res = 0
        matrix = [[0 for c in range(m)] for r in range(n)]
        for row in range(n):
            for col in range(m):
                for ri, ci in indices:
                    if row == ri:
                        matrix[row][col] += 1
                    if col == ci:
                        matrix[row][col] += 1

        for row in range(n):
            for col in range(m):
                if matrix[row][col] % 2 == 1:
                    res += 1
        return res
