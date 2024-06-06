class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        m, n = len(image), len(image[0])

        def bfs(sr, sc):
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited = set()
            agenda = deque([(sr, sc)])
            start_col = image[sr][sc]
            while agenda:
                r, c = agenda.popleft()
                visited.add((r, c))
                image[r][c] = color
                for dr, dc in dirs:
                    if 0 <= r + dr < m and 0 <= c + dc < n and image[r+dr][c+dc] == start_col and (r+dr, c+dc) not in visited:
                        agenda.append((r + dr, c + dc))
        
            return
        
        bfs(sr, sc)
        return image
