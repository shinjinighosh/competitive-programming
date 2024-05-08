from collections import defaultdict
from math import floor

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        trigger = floor(len(nums) / 2)
        for num in nums:
            counter[num] += 1
            if counter[num] > trigger:
                return num
