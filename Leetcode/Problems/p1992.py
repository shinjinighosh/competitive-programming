# includes commented out TLE solution

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        res = []

        # seen = set()

        # def within_bounds(x, y):
        #     return 0 <= x < m and 0 <= y < n

        # def get_corner(x, y):
        #     # get the bottom right corner of the farmland that starts at (x, y)
        #     agenda = deque([(x, y)])
        #     while agenda:
        #         x, y = agenda.popleft()
        #         seen.add((x, y))
        #         if within_bounds(x+1, y) and land[x+1][y] and (x+1, y) not in seen:
        #             agenda.append((x+1, y))
        #         if within_bounds(x, y+1) and land[x][y+1] and (x, y+1) not in seen:
        #             agenda.append((x, y+1))
        #     return [x, y] # neither its bottom nor right cell are farmland and the agenda has been exhausted, so this is the corner

        # def get_corner(x, y):
        #     # get the bottom right corner of the farmland that starts at (x, y)
        #     stack = deque([(x, y)])
        #     while stack:
        #         x, y = stack.popleft()  # Use popleft() to pop from the beginning of the deque
        #         land[x][y] = 0  # Mark cell as visited
        #         if x + 1 < m and land[x + 1][y]:
        #             stack.append((x + 1, y))
        #         if y + 1 < n and land[x][y + 1]:
        #             stack.append((x, y + 1))
        #     return [x, y]  # Neither its bottom nor right cell are farmland, so this is the corner

        # for i in range(m):
        #     for j in range(n):
        #         if land[i][j] and (i, j) not in seen:
        #             # part of new farmland
        #             left_corner = [i, j]
        #             right_corner = get_corner(i, j)
        #             res.append(left_corner + right_corner)

        # return res

        visited = set()
        groups = []

        def is_farmland(x, y):
            return 0 <= x < m and 0 <= y < n and land[x][y] == 1

        def dfs(r1, c1):
            r2, c2 = r1, c1
            stack = [(r1, c1)]
            visited.add((r1, c1))
            while stack:
                x, y = stack.pop()
                r2, c2 = max(r2, x), max(c2, y)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if is_farmland(nx, ny) and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
            groups.append([r1, c1, r2, c2])

        for i in range(m):
            for j in range(n):
                if is_farmland(i, j) and (i, j) not in visited:
                    dfs(i, j)

        return groups

        
