# Valid Palindrome

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for char in s:
            if char.isnumeric() or char.isalpha():
                r += char.lower()
        return r == r[::-1]
