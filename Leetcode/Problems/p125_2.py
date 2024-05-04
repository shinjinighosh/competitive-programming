class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if not(char.isdigit() or char.isalpha()):
                continue
            if char.isalpha():
                res.append(char.lower())
            else:
                res.append(char)
        return res == res[::-1]
        
