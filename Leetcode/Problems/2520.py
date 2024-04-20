class Solution:
    def countDigits(self, num: int) -> int:
        return sum([num%int(i)==0 for i in str(num)])
