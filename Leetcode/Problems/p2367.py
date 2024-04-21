class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ctr = 0
        numset = set(nums)
        for i in nums[1:]:
            if i-diff in numset and i+diff in numset:
                ctr += 1
        return ctr
