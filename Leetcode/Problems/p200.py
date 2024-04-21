# includes commented out TLE solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # seen = set()
        # m = len(grid)
        # n = len(grid[0])
        # counter = 0

        # def within_bounds(x, y):
        #     return 0 <= x <= m-1 and 0 <= y <= n-1

        # def get_island(x, y): 
        #     # process the island that contains (x, y) and mark as seen
        #     # assumes grid[x][y] == 1
        #     agenda = [(x, y)]
        #     while agenda:
        #         # print("Agenda is", agenda)
        #         x, y = agenda.pop(0)
        #         # if (x, y) in seen:
        #             # continue
        #         seen.add((x, y))
        #         candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        #         valid_candidates = []
        #         for x_new, y_new in candidates:
        #             if within_bounds(x_new, y_new) and grid[x_new][y_new] == "1" and (x_new, y_new) not in seen:
        #                 valid_candidates.append((x_new, y_new))
        #         agenda.extend(valid_candidates)

        # def get_island(x, y): 
        #     # process the island that contains (x, y) and mark as seen
        #     # assumes grid[x][y] == 1
        #     agenda = deque([(x, y)])
        #     while agenda:
        #         x, y = agenda.popleft()
        #         grid[x][y] = "0"  # Mark cell as visited
        #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             nx, ny = x + dx, y + dy
        #             if within_bounds(nx, ny) and grid[nx][ny] == "1":
        #                 agenda.append((nx, ny))

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1" and (i, j) not in seen:
        #             counter += 1 # new island spotted
        #             get_island(i, j)

        # return counter    

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                return
            grid[x][y] = "0"  # Mark current cell as visited
            # Explore adjacent cells in all directions
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        m = len(grid)
        n = len(grid[0])
        island_count = 0

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1  # Found a new island
                    dfs(i, j)  # Explore the island and mark all connected land cells as visited
        
        return island_count
        
