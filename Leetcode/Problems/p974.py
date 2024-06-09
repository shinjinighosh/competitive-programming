class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:
                mod += k
            
            if mod in count:
                res += count[mod]
            
            if mod in count: 
                count[mod] += 1
            else:
                count[mod] = 1
        
        return res
