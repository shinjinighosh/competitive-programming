# Rotting Oranges

'''
Given a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 '''

  class Solution:

       def countOne(self, grid):
            res = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        res += 1
            return res

        def getCandidates(self, grid, r, c):
            cand = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            rows = len(grid)
            cols = len(grid[0])
            for a, b in cand:
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1:
                    res.append((a, b))
            return res

        def orangesRotting(self, grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])
            original_fresh = self.countOne(grid)
            old_fresh = self.countOne(grid)
            new_fresh = 0
            if not old_fresh:
                return 0
            # print(old_fresh)
            mins = 0
            while new_fresh != old_fresh and self.countOne(grid):
                to_change = []
                for r in range(rows):
                    for c in range(cols):
                        if grid[r][c] == 2:
                            cands = self.getCandidates(grid, r, c)
                            to_change.extend(cands)
                # print(to_change)
                for new_r, new_c in to_change:
                    grid[new_r][new_c] = 2
                old_fresh = new_fresh
                new_fresh = self.countOne(grid)
                mins += 1
            if self.countOne(grid):  # some always stay fresh
                return -1
            return mins
