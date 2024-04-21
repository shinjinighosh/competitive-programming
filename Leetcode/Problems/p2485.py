import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(int(n * (n+1) / 2))
        if abs(x - int(x)) <= 0.000000001:
            return int(x)
        return -1
        
