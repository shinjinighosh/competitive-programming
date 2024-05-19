# TLE Solution

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        strs = [str(num) for num in nums]
        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        res += 1
        return res

