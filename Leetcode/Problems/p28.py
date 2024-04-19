class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, letter in enumerate(haystack):
            if letter != needle[0]:
                continue
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1
