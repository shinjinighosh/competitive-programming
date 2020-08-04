# 46. Permutations

'''
Given a collection of distinct integers, return all possible permutations.
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(seen, cur, res):
            if len(seen) == len(nums):
                res.append(cur)
                return
            for num in nums:
                if num in seen:
                    continue
                nex = copy.deepcopy(cur)
                nex.append(num)
                new_seen = {num}
                new_seen = new_seen.union(seen)
                helper(new_seen, nex, res)
        helper(set(), [], res)
        return res
