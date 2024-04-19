class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last_idx = 0 # keep track of last unique position in the array
        memo = set() # keep track of processed elements

        for idx, num in enumerate(nums):
            if num not in memo:
                memo.add(num)
                nums[last_idx] = num
                last_idx += 1

        return len(memo)
        
