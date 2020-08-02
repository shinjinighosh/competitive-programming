# Detect Capital

'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        letters = list(word)
        if not word:
            return True
        if all([a.isupper() for a in letters]):
            return True
        elif all([a.islower() for a in letters]):
            return True
        elif letters[0].isupper() and all([a.islower() for a in letters[1:]]):
            return True
        return False
