class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ctr = 0
        for num in nums:
            if num < k:
                ctr += 1
        return ctr
