from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        dicts = [Counter(s) for s in A]
        for letter, count in dicts[0].items():
            curr_min_count = count
            for dic in dicts[1:]:
                if letter not in dic:
                    curr_min_count = 0
                    break
                else:
                    curr_min_count = min(curr_min_count, dic[letter])

            if curr_min_count:
                res.extend(letter * curr_min_count)

        return res
