from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if n == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize thief positons to 0
        dist = [[float("inf")] * n for _ in range(n)]
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0

        # BFS to find min distance to each thief
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float("inf"):
                    dist[nr][nc] = dist[r][c] + 1 # it is one unit away from the previous location
                    queue.append((nr, nc))

        # Priority queue to maximize the min distance path
        # Negative because heapq is a min-heap
        pq = [(-dist[0][0], 0, 0)]
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]

        while pq:
            safeness_factor, r, c = heapq.heappop(pq)
            safeness_factor = -safeness_factor # convert back to positive
            if r == n-1 and c == n-1: # we have reached the end
                return safeness_factor
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safeness = min(safeness_factor, dist[nr][nc]) # this is now the new safeness value
                    if new_safeness > safeness[nr][nc]: # this path has a new least safe cell
                        safeness[nr][nc] = new_safeness
                        heapq.heappush(pq, (-new_safeness, nr, nc))

        return safeness[n-1][n-1]

