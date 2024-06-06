# This TLEs

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return mat
        m, n = len(mat), len(mat[0])
        res = [[0 for i in range(n)] for j in range(m)]

        def bfs(r, c, visited=None):
            if visited is None:
                visited = set()

            agenda = deque([(r, c, 0)])
            while agenda:
                curr_row, curr_col, curr_path = agenda.popleft()
                visited.add((curr_row, curr_col))
                if mat[curr_row][curr_col] == 0:
                    return curr_path
                neighbors = [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]
                for new_r, new_c in neighbors:
                    if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited:
                        agenda.append((new_r, new_c, curr_path + 1))


        for r in range(m):
            for c in range(n):
                min_dist = bfs(r, c)
                res[r][c] = min_dist

        return res

