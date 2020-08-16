# 128. Longest Consecutive Sequence

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        input_set = set(nums)
        longest_seq = 0
        local_seq = 1

        for n in nums:

            while (n + 1) in input_set:
                local_seq += 1
                n += 1

            longest_seq = max(longest_seq, local_seq)
            local_seq = 1

        return longest_seq
