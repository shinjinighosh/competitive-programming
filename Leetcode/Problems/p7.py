# Given a 32-bit signed integer, reverse digits of an integer.


def reverse(x: int) -> int:
    min_int = -2**31
    max_int = 2**31 - 1
    negative = True if x < 0 else False
    if not negative:
        result = int(str(x)[::-1])
    else:
        result = -1 * int(str(-x)[::-1])
    if min_int <= result <= max_int:
        return result
    else:
        return 0

    # result = 0
    # min_int = -2**31
    # max_int = 2**31 - 1
    # while x != 0:
    #     last_digit = x % 10
    #     x //= 10
    #     if result > max_int // 10 or (result == max_int // 10 and last_digit > 7):
    #         print("gets to a, result is", result)
    #         return 0
    #     if result < min_int // 10 or (result == min_int // 10 and last_digit < -8):
    #         print("gets to b, result is", result)
    #         return 0
    #     result = result * 10 + last_digit
    # print("result is", result)
    #
    # if min_int <= result <= max_int:
    #     return result
    # else:
    #     return 0
    # return result


testcases = [1, 123, 0, 321, -123, 120, 1534236469]
true_answers = [1, 321, 0, 123, -321, 21, 0]

assert len(testcases) == len(true_answers)

for i in range(len(testcases)):
    true = true_answers[i]
    obtained = reverse(testcases[i])
    if true != obtained:
        print(f"Should be {true} but was {obtained}")
