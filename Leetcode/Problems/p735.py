# 735. Asteroid Collision

'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # result = []
        for roid in asteroids:
            # print(roid, stack)
            if roid > 0 or not stack:
                stack.append(roid)
            elif stack:
                # do stuff
                last = 0
                while stack and stack[-1] < abs(roid) and stack[-1] > 0:
                    # last going right
                    last = stack.pop()
                # roid is destroyed if a) is equal size as last or b) stack[-1] > roid
                if stack and stack[-1] == abs(roid):
                    stack.pop()
                    continue
                elif stack and stack[-1] > abs(roid):
                    continue
                else:
                    stack.append(roid)
            # print("stack at end", stack)
        return stack


# testcases
# [5,10,-5]
# [8, -8]
# [10, 2, -5]
# [-2, -1, 1, 2]
# [-2,1,1,-1]

# answers
# [5,10]
# []
# [10]
# [-2,-1,1,2]
# [-2,1]
