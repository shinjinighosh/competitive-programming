# 136. Single Number

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for key, value in freq.items():
            if value == 1:
                return key
