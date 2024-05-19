# TLE Solution

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        is_sp = [False] * len(nums) # holds parity difference between two adj elements
        is_sp[-1] = True
        if not nums:
            return [True] * len(queries)
        # curr_par = nums[0] % 2
        # for i in range(1, len(nums)):
        #     # print(idx, num)
        #     num_par = nums[i] % 2
        #     if curr_par == num_par:
        #         is_sp[i] = False
        #         for j in range(i+1, len(nums)):
        #             is_sp[j] = False
        #             break
        #     is_sp[i] = is_sp[i-1] # once it's False, it remains False
        #     curr_par = num_par
        # print(is_sp)
        for i in range(1, len(nums)):
            is_sp[i-1] = (nums[i-1] % 2 != nums[i] % 2)
        res = []
        for from_idx, to_idx in queries:
            if from_idx == to_idx:
                res.append(True)
                continue
            curr_sp = True
            for j in range(from_idx, to_idx):
                if not is_sp[j]:
                    curr_sp = False
                    break
            res.append(curr_sp)
        return res

