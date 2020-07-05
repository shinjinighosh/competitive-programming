# 394. Decode String

'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''


class Solution:
    def decodeString(self, s: str) -> str:
        # s = list(s)
        # res = ''
        # while s:
        #     num = int(s.pop(0))
        #     s.pop(0)
        #     temp = ''
        #     while s[0] != ']':
        #         temp += s.pop(0)
        #     s.pop(0)
        #     res += temp * num
        # return res
        # while '[' in s:
        #     s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        # return s
        stack = []
        current = []
        num = 0
        for c in s:
            if c.isalpha():
                current.append(c)
            elif c.isnumeric():
                num = 10 * num + int(c)
            elif c == '[':
                stack.append((num, current))
                num = 0
                current = []
            else:  # c == ']'
                count, old_cur = stack.pop()
                old_cur.append(count * ''.join(current))
                current = old_cur
        return ''.join(current)
