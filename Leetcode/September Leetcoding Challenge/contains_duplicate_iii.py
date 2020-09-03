# Contains Duplicate III

'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

'''

from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, min(i+k+1, len(nums))):
        #         # print(nums[i], nums[j])
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        # return False
        SList = SortedList()
        for i in range(len(nums)):
            if i > k:
                SList.remove(nums[i - k - 1])
            pos1 = bisect_left(SList, nums[i] - t)
            pos2 = bisect_right(SList, nums[i] + t)

            if pos1 != pos2 and pos1 != len(SList):
                return True

            SList.add(nums[i])

        return False
