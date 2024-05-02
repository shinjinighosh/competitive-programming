class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i]
        for i in range(n):
            if i != n-i-1:
                res += mat[i][n-i-1]
        return res
