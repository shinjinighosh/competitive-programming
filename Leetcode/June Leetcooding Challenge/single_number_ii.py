#   Single Number II

'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for key, val in counts.items():
            if val == 1:
                return key
