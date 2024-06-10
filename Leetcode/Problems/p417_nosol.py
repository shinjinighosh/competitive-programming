class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        if not heights:
            return res
        m, n = len(heights), len(heights[0])
        pac = [[False for j in range(n)] for i in range(m)]
        atl = [[False for j in range(n)] for i in range(m)]

        visited_pac = set()
        
        # top row
        for j in range(n):
            pac[0][j] = True
            visited_pac.add((0, j))
        # left col
        for i in range(m):
            pac[i][0] = True
            visited_pac.add((i, 0))
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if (i, j) not in visited:
        #             if heights[i][j] >= heights[i-1][j] and pac[i-1][j] == True:
        #                 pac[i][j] = True
        #                 continue
        #             if heights[i][j] >= heights[i][j-1] and pac[i][j-1] == True:
        #                 pac[i][j] = True
        #         visited.add((i, j))


        
        visited_atl = set()
        # bottom row
        for j in range(n):
            atl[m-1][j] = True
            visited_atl.add((m-1, j))
        # right column
        for i in range(m):
            atl[i][n-1] = True
            visited_atl.add((i, -1))
        # # bottom to top
        # for i in range(m-2, -1, -1):
        #     # right to left
        #     for j in range(n-2, -1, -1):
        #         if (i, j) not in visited:
        #             if heights[i][j] >= heights[i+1][j] and atl[i+1][j] == True:
        #                 atl[i][j] = True
        #                 continue
        #             if heights[i][j] >= heights[i][j+1] and atl[i][j+1] == True:
        #                 atl[i][j] = True
        #         visited.add((i, j))
        
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        
        return res
