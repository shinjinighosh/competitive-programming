class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed_set = set(allowed)
        for word in words:
            for letter in word:
                if letter not in allowed_set:
                    break
            else:
                res += 1
        return res
