# return indices which add up to target


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        # faster one-pass hash array solution
        mapping = {}
        for i in range(len(nums)):
            if (target - nums[i]) in mapping:
                return [i, mapping[target - nums[i]]]
            else:
                mapping[nums[i]] = i
