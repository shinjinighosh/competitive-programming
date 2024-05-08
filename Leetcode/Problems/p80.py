class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0 # keep track of where to keep the next number
        ctr = {} # num : occurrences
        for idx, num in enumerate(nums):
            if num not in ctr:
                ctr[num] = 1
                nums[ptr] = num
                ptr += 1
            elif ctr[num] == 1: 
                ctr[num] += 1
                nums[ptr] = num
                ptr += 1
        return ptr
