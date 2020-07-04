#   Ugly Number II

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # uglies = [2, 3, 4, 5]
        # L2 = [2*i for i in uglies]
        # L2.remove(4)
        # L3 = [3*i for i in uglies]
        # L5 = [5*i for i in uglies]
        uglies = [1]
        uglies_set = set([1])
        L2 = [2]
        L3 = [3]
        L5 = [5]
        # if n <= 4:
        # return uglies[n]
        while len(uglies) < n:
            # print("uglies are ", uglies)
            # print(L2, L3, L5)
            if L2[0] <= L3[0] and L2[0] <= L5[0]:
                k = L2.pop(0)
                if k in uglies_set:
                    continue
                uglies_set.add(k)
                uglies.append(k)
                L2.append(2 * k)
                L3.append(3 * k)
                L5.append(5 * k)
            elif L3[0] <= L2[0] and L3[0] <= L5[0]:
                k = L3.pop(0)
                if k in uglies_set:
                    continue
                uglies_set.add(k)
                uglies.append(k)
                L2.append(2 * k)
                L3.append(3 * k)
                L5.append(5 * k)
            else:
                k = L5.pop(0)
                if k in uglies_set:
                    continue
                uglies_set.add(k)
                uglies.append(k)
                L2.append(2 * k)
                L3.append(3 * k)
                L5.append(5 * k)
            # L2.append()
        return uglies[-1]
