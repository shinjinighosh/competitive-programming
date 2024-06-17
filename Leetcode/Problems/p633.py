class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # return c % 4 in [0,1,2]
        # if c % 4 == 3:
        #     return False
        # if c == 1 or c == 2:
        #     return True
        # squares = set([i*i for i in range(c//2 +1)])
        # for i in squares:
        #     if c-i in squares:
        #         return True
        # return False

        divisor = 2 

        while divisor  ** 2 <= c:
            if c % divisor == 0:
                exponent_count = 0
                while c % divisor == 0:
                    exponent_count += 1
                    c //= divisor
                if divisor % 4 == 3 and exponent_count % 2 == 1:
                    return False
            divisor += 1
        
        return c % 4 != 3
        
        
