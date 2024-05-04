class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        curr = max(nums)
        res = 0
        for i in range(k):
            res += curr
            curr += 1
        return res 
