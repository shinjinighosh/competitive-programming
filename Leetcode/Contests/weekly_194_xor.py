# 5440. XOR Operation in an Array

'''
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
'''


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if not n:
            return 0
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num
        return res
