class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if not nums:
            return True
        curr_parity = nums[0] % 2
        for num in nums[1:]:
            num_par = num % 2
            if num_par == curr_parity:
                return False
            curr_parity = num_par
        return True
        
