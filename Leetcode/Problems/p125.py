class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for char in s:
            if char.isnumeric() or char.isalpha():
                r+= char.lower()
        return r == r[::-1]
        
