class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = 0

        for left in range(len(arr)):
            curr = 0
            for right in range(left, len(arr)):
                curr += arr[right]
                if (right - left) % 2 == 0:
                    res += curr
        
        return res

