class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ctr = 0
        wordset = set(word)
        seen = set()
        for letter in word:
            if letter.islower() and letter not in seen and letter.upper() in wordset:
                seen.add(letter)
                ctr += 1
        return ctr
