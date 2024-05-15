class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for digit in digits[::-1]:
            curr_total = digit + carry
            new_digit = curr_total % 10
            carry = curr_total // 10
            res.append(new_digit)
        if carry != 0:
            res.append(carry)
        return [int(i) for i in res[::-1]]

