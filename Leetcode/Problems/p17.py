# 17. Letter Combinations of a Phone Number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution:
    mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": [
        'm', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        return [i for i in self.yieldCombos(digits)]

    def yieldCombos(self, digits):
        if not digits:
            return
        elif len(digits) == 1:
            yield from Solution.mapping[digits[0]]
        else:
            for option in Solution.mapping[digits[0]]:
                for rest in self.yieldCombos(digits[1:]):
                    yield option + rest
