class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        def dfs(start, path):
            # we reached the end of the string and the path is valid
            if start == len(s):
                res.append(path)
                return

            # every possible partition
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    dfs(end, path + [s[start:end]])

        res = []
        dfs(0, [])
        return res
