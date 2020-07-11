# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

'''
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.
'''


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        if len(nums) == 5:
            init = nums[1] - nums[0]
            for i in range(1, len(nums) - 1):
                if nums[i + 1] - nums[i] < init:
                    init = nums[i + 1] - nums[i]
            return init
        # print(nums)
        changing_max = abs(nums[-4] - nums[0])
        changing_min = abs(nums[3] - nums[-1])
        # print(changing_max, changing_min)
        return min(changing_max, changing_min)

# [5,3,2,4]
# [1,5,0,10,14]
# [6,6,0,1,1,4,6]
# [1,5,6,14,15]
