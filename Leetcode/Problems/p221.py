class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] represents the side length of the largest square whose bottom right corner is cell (i, j)
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        curr_max = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    dp[r][c] = 1
                    curr_max = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "0": # a square can never end at a 0
                    continue
                else:
                    dp[i][j] = 1 +  min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    if dp[i][j] > curr_max:
                        curr_max = dp[i][j]
        
        return curr_max ** 2


