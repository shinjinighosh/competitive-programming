class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        res = [[0 for cell in range(n-2)] for row in range(n-2)]

        for r in range(n-2):
            for c in range(n-2):
                res[r][c] = max(grid[ii][jj] for ii in range(r, r+3) for jj in range(c, c+3))

        return res
