# 1389. Create Target Array in the Given Order

'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
'''


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # mapping  = {}
        # for i in range(len(nums)):
        #     mapping[index[i]] = nums[i]
        # index.sort()
        # res = []
        # for idx in index:
        #     res.append(mapping[idx])
        # return res
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res
