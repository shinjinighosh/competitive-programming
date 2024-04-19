class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        last_idx = -1 # keeps track of where to replace
        counter = 0 # goes upto k

        for idx, num in enumerate(nums):
            if num != val:
                counter += 1
                last_idx += 1
                nums[last_idx] = num
            else:
                nums[idx] = "-"

        return counter
        
