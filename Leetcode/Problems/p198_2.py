class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # dp[i] = max(dp[i-2], dp[i-3]) + nums[i] # <- this is the max if you chose the current house
            # either dont rob the current house, or do (and dont rob the previous one)
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # return max(dp[-1], dp[-2])
        return dp[-1]
