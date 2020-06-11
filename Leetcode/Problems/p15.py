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
                    # return [nums[i], target - nums[i]]
                    # return [i, mapping[target - nums[i]]]
                else:
                    mapping[nums[i]] = i
            return res

        res = set()
        for i in range(len(nums)):
            temp = [nums[i]]
            old = nums[i]
            # print(f"temp is {temp} and passing to twoSum {nums[i+1:]} and {-1 * nums[i]}")
            k = twoSum(nums[i + 1:], -1 * nums[i])
            if k:
                print(f"k is {k} and old is {old}")
                for other_2 in k:
                    a, b = other_2[0], other_2[1]
                    # print(f"three candidates are {old, a, b}")
                    res.add(tuple(sorted([old, a, b])))
                    # res.add(frozenset([old] + list(other_2)))
                    # temp.add(nums[a])
                    # temp.add(nums[b])
                    # temp.extend([a, b])
                    # temp.extend([nums[a], nums[b]])
                    # res.add(frozenset(temp))
                    # res.append(temp)
                print(f"res is {res}")
        return list(list(i) for i in res)


t = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(t.threeSum(nums))
