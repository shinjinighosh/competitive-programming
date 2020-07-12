# 5461. Number of Substrings With Only 1s

'''
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.
'''


class Solution:
    def numSub(self, s: str) -> int:
        tail = s.find("1")
        if not s or tail == -1:
            return 0
        if len(s) == 1:
            if s[0] == 1:
                return 1
            else:
                return 0
        head = tail + 1
        temp = 0
        count = 0
        while head <= len(s):
            # print(s[tail:head], "1"*(head-tail), "head", head, "tail", tail)
            if s[tail:head] == "1" * (head - tail):
                temp += 1
                head += 1
            else:
                # print("temp", temp)
                count += (temp * (temp + 1)) // 2
                count %= (10**9 + 7)
                temp = 0
                tail = head
                head = tail + 1
        if temp:
            count += (temp * (temp + 1)) // 2
            count %= (10**9 + 7)
        return count
