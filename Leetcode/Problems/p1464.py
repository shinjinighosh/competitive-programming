# 1464. Maximum Product of Two Elements in an Array

'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        abs_max = 0
        second_max = 0
        for num in nums:
            if num > abs_max:
                second_max = abs_max
                abs_max = num
            elif second_max < num:
                second_max = num
        return (abs_max - 1) * (second_max - 1)
