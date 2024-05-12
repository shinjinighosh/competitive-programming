class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'(': ')', '{': '}', '[': ']'}
        opening = matches.keys()
        closing = matches.values()

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if not stack: # unmatched
                    return False
                last_open = stack.pop()
                if matches[last_open] != bracket:
                    return False
        return not stack
