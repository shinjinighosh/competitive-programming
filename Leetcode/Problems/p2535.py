class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elt_sum = lambda lis: sum(lis)
        digit_sum_num = lambda num: sum([int(i) for i in str(num)])
        digit_sum = lambda lis: sum([digit_sum_num(num) for num in lis])
        return abs(digit_sum(nums) - elt_sum(nums))
