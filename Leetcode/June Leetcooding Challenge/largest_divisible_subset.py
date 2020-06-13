# Largest Divisible Subset


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        nums.sort()
        dp = [1 for i in range(len(nums))]
        res = []
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:  # not mutually prime
                    dp[i] = max(dp[i], dp[j] + 1)  # either we can take i, or j and both
        for i in range(1, max(dp) + 1):
            res.append(nums[dp.index(i)])
        return res
