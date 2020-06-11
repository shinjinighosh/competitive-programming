# 451. Sort chars by frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        l = list(s)
        l.sort(reverse=True, key=lambda x: freq[x])
        temp = []
        for i in l:
            if i not in temp:
                temp.append(i)
        res = ""
        joined = "".join(temp)
        for char in joined:
            res += char * freq[char]
        return res
        # return "".join(l)
