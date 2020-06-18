# 605. Can Place Flowers

'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        stack = []
        for idx, pos in enumerate(flowerbed):
            # print("stack at start", stack)
            if pos:  # already a flower here
                stack.append(pos)
            else:  # empty place
                if (not stack or stack and not stack[-1]) and (idx == len(flowerbed) - 1 or flowerbed[idx + 1] == 0):
                    # either (we are just starting or last place was empty) and nextplace (if existent) is empty
                    stack.append(1)
                    n -= 1
                    if n == 0:
                        return True
                else:
                    stack.append(0)
            # print("stack at end", stack)
        return False
