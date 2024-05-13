class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        curr_max = 0
        for n in nums:
            if n-1 not in numset:
                curr_seq = 1
                while n+1 in numset:
                    curr_seq += 1
                    n += 1
                if curr_seq > curr_max:
                    curr_max = curr_seq
        return curr_max
