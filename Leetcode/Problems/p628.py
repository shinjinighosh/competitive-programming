# 628. Maximum Product of Three Numbers

'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        return max(nums[0] * nums[1] * nums[l - 1], nums[l - 1] * nums[l - 2] * nums[l - 3])
