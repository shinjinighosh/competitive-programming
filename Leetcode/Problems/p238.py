class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = []
        curr = 1
        for idx, num in enumerate(nums):
            left_prods.append(curr)
            curr *= num
        right_prods = []
        curr = 1
        for idx in range(len(nums) - 1, -1, -1):
            right_prods.append(curr)
            curr *= nums[idx]
        right_prods = right_prods[::-1]
        res = []
        for idx in range(len(nums)):
            res.append(left_prods[idx] * right_prods[idx])
        return res
        
