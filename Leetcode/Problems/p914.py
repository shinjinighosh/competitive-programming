# 914. X of a Kind in a Deck of Cards

'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
'''


class Solution:
    def gcd(self, a, b):
        if a > b:
            a, b = b, a
        if b % a == 0:
            return a
        return gcd(b % a, a)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = {}
        for i in deck:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        vals = list(set(freq.values()))
        vals.sort()
        if not vals or vals[0] == 1:
            return False
        if len(vals) == 1:
            return True
        min_elt = vals[0]
        # print(vals)
        gcds = []
        for i in range(1, len(vals)):
            # print("gcd is", self.gcd(vals[i],min_elt))
            k = self.gcd(vals[i], min_elt)
            if k == 1:
                return False
            gcds.append(k)
        # print(gcds)
        reduced_gcd = gcds[0]
        for i in range(1, len(gcds)):
            reduced_gcd = self.gcd(gcds[i], reduced_gcd)
        if reduced_gcd == 1:
            return False
        # if len(set(gcds)) != 1:
        #     return False
        return True
