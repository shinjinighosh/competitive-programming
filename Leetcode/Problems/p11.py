# TLE Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        total_max = 0
        for idx, ht in enumerate(height[:-1]):
            # one pointer is idx, what's the max area we can make with idx as left side?
            for j in range(idx + 1, len(height)):
                area = (j - idx) * min(ht, height[j])
                if area > total_max:
                    total_max = area
        return total_max
