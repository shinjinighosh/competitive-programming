# 1295. Find Numbers with Even Number of Digits

'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(n)) % 2 == 0 for n in nums])
