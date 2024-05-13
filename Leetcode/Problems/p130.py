class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        
        def dfs(x, y):
            if not (0 <= x < m) or not (0 <= y < n) or board[x][y] != "O":
                return
            board[x][y] = "S"
            for dx in [-1, 1]:
                dfs(x + dx, y)
            for dy in [-1, 1]:
                dfs(x, y + dy)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # flip all O to X and all S back to O
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "O":
                    board[i][j] = "X"
                elif cell == "S":
                    board[i][j] = "O"
                    
