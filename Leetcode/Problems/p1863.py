class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        subset_ct = 1 << len(nums)

        for i in range(subset_ct):
            curr_xor = 0
            for j in range(len(nums)):
                # check if the jth elt is in the ith subset
                if i & (1 << j):
                    curr_xor ^= nums[j]
            res += curr_xor

        return res

        return res
