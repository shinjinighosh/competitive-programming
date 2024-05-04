class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        memo = {}
        seen = set()
        if len(pattern) != len(str.split()):
            return False
        for letter, word in zip(pattern, str.split()):
            if letter in memo:
                if word != memo[letter]:
                    return False
            else:
                # so we have not mapped this pattern letter to a word before
                # but if we have seen this word before that's not okay either
                if word in seen:
                    return False
                # all clear
                memo[letter] = word
                seen.add(word)
        return True
            
        
