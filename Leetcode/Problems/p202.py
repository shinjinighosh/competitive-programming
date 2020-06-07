# 202. Happy Number


class Solution:
    def isHappy(self, n: int) -> bool:
        # if I ever return to the same number, it's a cycle
        seen = set()

        while n != 1:
            l = [int(i) for i in list(str(n))]
            n = sum([i * i for i in l])
            if n in seen:
                return False
            else:
                seen.add(n)

        return True


test_obj = Solution()
print(test_obj.isHappy(19))
