class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        if not heights:
            return res
        m, n = len(heights), len(heights[0])
            

        visited_pac = set()
        
        # top row
        for j in range(n):
            visited_pac.add((0, j))
        # left col
        for i in range(m):
            visited_pac.add((i, 0))
        
        visited_atl = set()
        # bottom row
        for j in range(n):
            visited_atl.add((m-1, j))
        # right column
        for i in range(m):
            visited_atl.add((i, n-1))

        def bfs(visited):
            agenda = deque(list(visited)) # start from all the relevant edges
            while agenda:
                r, c = agenda.popleft()
                visited.add((r, c))
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dirs:
                    if 0 <= r + dr < m and 0 <= c + dc < n and heights[r][c] <= heights[r + dr][c + dc]:
                        if (r + dr, c + dc) not in visited:
                            agenda.append((r + dr, c + dc))
            return visited

        visited_pac = bfs(visited_pac)
        visited_atl = bfs(visited_atl)

        unordered_res = visited_pac.intersection(visited_atl)
        
        for i in range(m):
            for j in range(n):
                if (i, j) in unordered_res:
                    res.append([i, j])
        
        return res
