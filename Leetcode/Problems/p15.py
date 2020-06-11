# 15. 3Sum

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''


class Solution:
    def threeSum(self, nums):
        def twoSum(nums, target):
            res = set()
            mapping = {}
            for i in range(len(nums)):
                if (target - nums[i]) in mapping:
                    res.add((nums[i], target - nums[i],))
                else:
                    mapping[nums[i]] = i
            return res

        res = set()
        for i in range(len(nums)):
            old = nums[i]
            k = twoSum(nums[i + 1:], -1 * old)
            if k:
                for other_2 in k:
                    a, b = other_2[0], other_2[1]
                    res.add(tuple(sorted([old, a, b])))
        return list(list(i) for i in res)


t = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(t.threeSum(nums))
