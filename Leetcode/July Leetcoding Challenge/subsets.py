# Subsets

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(seq):
            if len(seq) <= 1:
                yield seq
                yield []
            else:
                for item in powerset(seq[1:]):
                    yield [seq[0]] + item
                    yield item
        return [i for i in powerset(nums)]
