# 152. Maximum Product Subarray

'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp = [i for i in nums]
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i], dp[i-1]*dp[i])
        if not nums:
            return 0

        res = max_p = min_p = nums[0]

        # there are cases that min_p , i or max_p could be the largest product
        for i in nums[1:]:
            max_p, min_p = max(max_p * i, min_p * i, i), min(max_p * i, min_p * i, i)
            res = max(res, max_p)

        return res
        # return max(dp)
