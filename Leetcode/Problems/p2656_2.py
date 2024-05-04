class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return sum(max(nums) + i for i in range(k))

