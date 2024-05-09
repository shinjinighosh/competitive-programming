class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            if curr_area > max_area:
                max_area = curr_area

            # Move the pointer that points to the shorter line inward,
            # as this might increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
