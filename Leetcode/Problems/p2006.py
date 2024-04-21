class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        memo = {} # maps number : [idx]
        ctr = 0

        for idx, num in enumerate(nums):
            if num in memo:
                memo[num].append(idx)
            else:
                memo[num] = [idx]

        for idx, num in enumerate(nums):
            if num-k in memo:
                for idx_j in memo[num-k]:
                    if idx_j > idx:
                        ctr += 1
            if num+k in memo:
                for idx_j in memo[num+k]:
                    if idx_j > idx:
                        ctr += 1

        return ctr
