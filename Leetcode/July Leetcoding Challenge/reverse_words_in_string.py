# Reverse Words in a String

'''
Given an input string, reverse the string word by word.

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])
