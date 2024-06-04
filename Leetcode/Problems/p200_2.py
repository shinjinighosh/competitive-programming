class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(x, y, visited):
            if not (0 <= x < m) or not(0 <= y < n) or (x, y) in visited or grid[x][y] == "0":
                return
            visited.add((x, y))
            dfs(x+1, y, visited)
            dfs(x-1, y, visited)
            dfs(x, y+1, visited)
            dfs(x, y-1, visited)

        res = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i, j, visited)
        return res
