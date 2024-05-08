class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ctr = 0
        for idx, num in enumerate(nums):
            if num == val:
                nums[idx] = "-"
            else:
                ctr += 1
        i = 0 # pointer denoting place in nums to place next element
        j = 0 # pointer moving along nums
        while i < ctr: # move up elements
            num = nums[j]
            if num != "-":
                nums[i] = num
                i += 1
            j += 1
        return ctr

        
