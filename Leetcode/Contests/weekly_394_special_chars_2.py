class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        special_chars = set()
        seen = set()
        ctr = 0
        wordset = set(word)
        memo = {} # maps letter: [idx of occurrence]
        
        for idx, letter in enumerate(word):
            if letter in memo:
                memo[letter].append(idx)
            else:
                memo[letter] = [idx]
                
        for idx, letter in enumerate(word):
            if letter.islower() and letter not in seen and letter.upper() in wordset: # candidate
                seen.add(letter)
                all_lower_occurrences = memo[letter]
                all_upper_occurrences = memo[letter.upper()]
                
                if all_lower_occurrences[-1] < all_upper_occurrences[0]:
                    ctr += 1
        return ctr
