# 342. Power of Four

'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # while num >= 0:
        #     num = num << 1
        # return num == 0
        if num <= 0:
            return False
        x = math.log(num, 4)
        return 4**x == 4**int(x)
