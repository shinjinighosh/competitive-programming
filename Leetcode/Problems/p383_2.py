from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_ctr = Counter(magazine)
        note_ctr = Counter(ransomNote)
        for letter, num in note_ctr.items():
            if letter not in mag_ctr:
                return False
            mag_num = mag_ctr[letter]
            if mag_num < num:
                return False
        return True
        
