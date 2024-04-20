class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        i = 0
        while i < len(nums):
            arr.append(nums[i+1])
            arr.append(nums[i])
            i += 2
        return arr
        
