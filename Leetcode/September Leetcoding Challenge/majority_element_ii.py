# Majority Element II

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for elt in nums:
            if elt in counts:
                counts[elt] += 1
            else:
                counts[elt] = 1
        threshold = math.floor(len(nums) / 3)
        res = []
        for k, i in counts.items():
            if i > threshold:
                res.append(k)
        return res
