# 5483. Make The String Great

'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
'''

# TO FINISH


class Solution:
    def isGood(self, s):
        i = 0
        while i <= len(s) - 2:
            if s[i].islower() and s[i + 1].isupper() and s[i + 1].lower() == s[i]:
                return False
            elif s[i + 1].islower() and s[i].isupper() and s[i].lower() == s[i + 1]:
                return False
            i += 1
        return True

    def makeGood(self, s: str) -> str:
        while not self.isGood(s):
            for i in range(len(s) - 2):
                if (s[i].islower() and s[i + 1].isupper() and s[i + 1].lower() == s[i]) or (s[i + 1].islower() and s[i].isupper() and s[i].lower() == s[i + 1]):
                    if i < len(s) - 2:
                        s = s[:i] + s[i].lower() + s[i + 2:]
                    else:
                        s = s[:i] + s[i].lower()
        return s
