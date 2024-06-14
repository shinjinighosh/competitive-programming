class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        target = []
        res = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                target.append(num)
                continue
            if num > target[idx - 1]:
                target.append(num)
            else:
                target.append(target[idx - 1] + 1)
                res += target[idx - 1] + 1 - num

        # print(target)
        return res
