# 242. Valid Anagram

'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
