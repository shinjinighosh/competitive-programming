# 15. 3Sum

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''


class Solution:
    def threeSum(self, nums):
        def twoSum(nums, target):
            mapping = {}
            for i in range(len(nums)):
                if (target - nums[i]) in mapping:
                    return [i, mapping[target - nums[i]]]
                else:
                    mapping[nums[i]] = i
            return None
        res = set()
        for i in range(len(nums)):
            temp = [nums[i]]
            k = twoSum(nums[i + 1:], -1 * nums[i])
            if k:
                a, b = k
                # temp.add(nums[a])
                # temp.add(nums[b])
                temp.extend([nums[a], nums[b]])
                res.add(tuple(temp))
                # res.append(temp)
        return list(list(i) for i in res)


t = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(t.threeSum(nums))
