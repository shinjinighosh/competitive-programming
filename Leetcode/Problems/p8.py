# implement atoi


def myAtoi(str: str) -> int:
    str = str.strip()
    negative = False
    if not str or ((str.count("+") + str.count("-")) > 1):
        print("count more for str", str)
        return 0
    if str[0] == "-":
        negative = True
    str = str.strip("+-")
    stripped_string = ""
    for char in str:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stripped_string += char
        else:
            break
    try:
        # print(stripped_string)
        if negative:
            res = -1 * int(stripped_string)
        else:
            res = int(stripped_string)
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return res
    except:
        return 0


testcases = ["123", "-321", "    123", "734982940932840983249",
             "", "words and 987", "2143 with words", "-5-", "+12", "+-2"]
correct_ans = [123, -321, 123, 2**31 - 1, 0, 0, 2143, -5, 12, 0]

for i in range(len(testcases)):
    actual = correct_ans[i]
    ans = myAtoi(testcases[i])
    if actual != ans:
        print(f"Should be {actual} but got {ans}")
