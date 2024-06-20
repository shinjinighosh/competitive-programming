class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def canPlaceBalls(minDist):
            ct = 1 
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= minDist:
                    ct += 1
                    last_pos = position[i]
                    if ct == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
