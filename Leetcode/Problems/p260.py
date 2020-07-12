# 260. Single Number III
'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for key, value in freq.items():
            if value == 1:
                res.append(key)
        return res
