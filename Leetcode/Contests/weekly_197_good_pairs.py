# 5460. Number of Good Pairs

'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ct = 0
        for key, val in freq.items():
            if val > 1:
                ct += (val * (val - 1)) // 2
        return ct
