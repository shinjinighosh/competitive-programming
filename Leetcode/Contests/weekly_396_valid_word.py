class Solution:
    def isValid(self, word: str) -> bool:
       
        vowels = set("aeiou")
        consonants = set("qwrtypsdfghjklzxcvbnm")
       
        has_vowel = False
        has_consonant = False
       
        if len(word) < 3:
            return False
       
        for s in word:
            if not s.isalnum():
                return False
            if s.lower() in vowels:
                has_vowel = True
            elif s.lower() in consonants:
                has_consonant = True
       
        if not has_vowel or not has_consonant:
            return False
        return True

