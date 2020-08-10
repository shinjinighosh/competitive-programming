# 1329. Sort the Matrix Diagonally

'''
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.
'''


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nums = []
        if not mat:
            return mat
        rows = len(mat)
        cols = len(mat[0])
        # for row in mat:
        #     for elt in row:
        #         nums.append(elt)
        res = [[0 for _ in range(cols)] for xyz in range(rows)]
        # nums.sort(reverse=True)
        starters = [(i, 0) for i in range(rows - 1, -1, -1)]
        for j in range(1, cols):
            starters.append((0, j))
        # print(starters)
        for r, c in starters:
            nums = []
            temp_r = r
            temp_c = c
            while 0 <= temp_r < rows and 0 <= temp_c < cols:
                nums.append(mat[temp_r][temp_c])
                temp_r += 1
                temp_c += 1
            nums.sort(reverse=True)
            # print(nums)
            while 0 <= r < rows and 0 <= c < cols:
                # print(r,c)
                res[r][c] = nums.pop()
                r += 1
                c += 1
        return res
