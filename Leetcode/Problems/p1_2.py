class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memo = {} # maps num to idx

        for idx, num in enumerate(nums):
            if target - num in memo:
                return [idx, memo[target-num]]
            else:
                memo[num] = idx
                

        
