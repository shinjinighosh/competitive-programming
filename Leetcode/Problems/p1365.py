# 1365. How Many Numbers Are Smaller Than the Current Number

'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''


# time complexity O(nlogn)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = copy.deepcopy(nums)
        temp.sort()
        positions = {}
        for i in range(len(temp)):
            if temp[i] not in positions:
                positions[temp[i]] = i
        res = []
        for num in nums:
            res.append(positions[num])
        return res
