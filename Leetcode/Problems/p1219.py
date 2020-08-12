# 1219. Path with Maximum Gold

'''
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def DFS(grid, current_gold, visited, r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                for i, j in visited:
                    current_gold += grid[i][j]
                return current_gold

            _max = 0
            visited.add((r, c))
            for new_r, new_c in [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]:
                _max = max(_max, DFS(grid, current_gold, visited, new_r, new_c))
            visited.remove((r, c))
            return _max
        if not grid:
            return 0
        max_gold = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # maybe paths instead of gold
                current_gold = DFS(grid, 0, set(), r, c)
                max_gold = max(max_gold, current_gold)

        return max_gold
