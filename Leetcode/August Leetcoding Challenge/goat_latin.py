# Goat Latin

'''
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.
'''


class Solution:
    def toGoatLatin(self, S: str) -> str:
        def isVowel(l):
            return l in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        words = S.split()
        idx = 0
        res = []
        while idx < len(words):
            temp = words[idx]
            if not temp:
                res.append(temp)
            elif isVowel(temp[0]):
                res.append(temp + "ma" + "a" * (idx + 1))
            else:
                res.append(temp[1:] + temp[0] + "ma" + "a" * (idx + 1))
            idx += 1
        return " ".join(res)
