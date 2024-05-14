class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # length of the LIS that ends with element at i
        for idx, num in enumerate(nums): # can this be the potential end
            for j in range(idx):
                if nums[j] < num: 
                    # num can be tacked on
                    dp[idx] = max(dp[idx], 1 + dp[j])
        return max(dp)
