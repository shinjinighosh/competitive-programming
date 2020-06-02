# implement atoi
import re


def myAtoi(str: str) -> int:
    # str = str.strip()
    pattern = "^\s*([-\+]?\d+)"
    match = re.search(pattern, str)
    if not match:
        return 0
    try:
        res = int(match.group(1))
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
