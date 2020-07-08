# 49. Group Anagrams

'''
Given an array of strings, group anagrams together.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # def isAnagram(word1, word2):
        #     freq = {}
        #     for c in word1:
        #         if c not in freq:
        #             freq[c] = 1
        #         else:
        #             freq[c] += 1
        #     freq2 = {}
        #     for c in word2:
        #         if c not in freq2:
        #             freq2[c] = 1
        #         else:
        #             freq2[c] += 1
        #     for char, count in freq.items():
        #         if char not in freq2 or freq2[char] != count:
        #             return False
        #     for char, count in freq2.items():
        #         if char not in freq or freq[char] != count:
        #             return False
        #     return True

        groups = {}  # tuple to list of strings
        for s in strs:
            letters = tuple(sorted(s))

            # for key, val in groups.items():
            #     if isAnagram(s, key):
            #         val.append(s)
            #         break
            # else:
            #     groups[s] = [s]

            if letters not in groups:
                groups[letters] = [s]
            else:
                groups[letters].append(s)

        return groups.values()
