# 383. Ransom Note

'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return set(ransomNote).intersection(set(magazine)) == set(ransomNote)
        tested = set()
        for c in ransomNote:
            if c not in tested:
                if magazine.count(c) < ransomNote.count(c):
                    return False
                tested.add(c)
        return True
