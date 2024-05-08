class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        memo = set()

        for idx, num in enumerate(nums):
            if num not in memo:
                memo.add(num)
                nums[ptr] = num
                ptr += 1
        return ptr
