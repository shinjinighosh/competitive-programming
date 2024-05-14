class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, curr_gold):
            if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] == 0 or visited[x][y]:
                return curr_gold
            # mark cell as visited
            visited[x][y] = True
            curr_gold += grid[x][y]
            max_gold = 0 # for this path

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy, curr_gold))
            # mark cell as unvisited before the next exploration
            visited[x][y] = False
            return max_gold
        
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0: # start from cell with gold
                    res = max(res, dfs(i, j, 0))

        return res
