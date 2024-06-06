class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        
        def dfs(start, visited):
            for y in range(n):
                if isConnected[start][y] and y not in visited:
                    visited.add(y)
                    dfs(y, visited)
            return visited

        res = 0
        visited = set()
        for x in range(n):
            for y in range(n):
                if x not in visited:
                    res += 1
                    visited.add(x)
                    visited = dfs(x, visited)
                if not isConnected[x][y] and y not in visited:
                    res += 1
                    visited.add(y)
                    visited = dfs(y, visited)
        return res
            

