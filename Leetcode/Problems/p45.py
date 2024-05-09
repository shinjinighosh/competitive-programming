class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        jumps = 0
        end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest,i + nums[i])
            if i == end: # we have reached the end of the range we can jump to currently
                end = farthest
                jumps += 1
                if end >= len(nums) - 1: # exit early
                    return jumps
        return jumps

        
