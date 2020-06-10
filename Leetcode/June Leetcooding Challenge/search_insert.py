# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums and target <= nums[0]:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i] < target < nums[i + 1]:
                return i + 1
        if nums[len(nums) - 1] == target:
            return len(nums) - 1
        if len(nums) == 1 and target > nums[0]:
            return 1
        return i + 2

        # alternate faster solution
        '''
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)
        '''
