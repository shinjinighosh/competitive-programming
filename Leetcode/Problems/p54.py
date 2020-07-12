# 54. Spiral Matrix

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # solution not working
        # m = len(matrix)
        # n = len(matrix[0])
        # current = [0,0]
        # switch = "r" # either l or r
        # res = []
        # while len(res) < m*n:
        #     # res.append(matrix[current[0]][current[1]])
        #     # print(res)
        #     if switch == "r":
        #         if current[1] == 0:
        #             while current[1] < n:
        #                 res.append(matrix[current[0]][current[1]])
        #                 print(res)
        #                 current[1] += 1
        #             current[1] -= 1
        #         else:
        #             while current[1] >= 0:
        #                 res.append(matrix[current[0]][current[1]])
        #                 print(res)
        #                 current[1] -= 1
        #             current[1] += 1
        #         switch = "l"
        #     else:
        #         if current[0] == 0:
        #             while current[0] < m:
        #                 res.append(matrix[current[0]][current[1]])
        #                 print(res)
        #                 current[0] += 1
        #             current[0] -= 1
        #         else:
        #             while current[0] >= 0:
        #                 res.append(matrix[current[0]][current[1]])
        #                 print(res)
        #                 current[0] -= 1
        #             current[1] += 1
        #         switch = "r"
        # return res

        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        seen = [[False] * n for i in matrix]
        res = []
        # for clockwise turns
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        # di is direction and cr, cc are next positions
        for _ in range(m * n):
            res.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res
