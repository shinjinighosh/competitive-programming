# 268. Missing Number

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = len(nums)
        for i in range(maximum + 1):
            if i not in seen:
                return i
