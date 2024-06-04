class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not click:
            return board
        r, c = click[0], click[1]
        m, n = len(board), len(board[0])
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0 or not (0 <= r + dr < m) or not (0 <= c + dc < n):
                    continue
                neighbors.append((r + dr, c + dc))
        # flag = False # change to True if it has adjacent mines
        count = 0 # count of adjacent mines
        for new_r, new_c in neighbors:
            if board[new_r][new_c] == "M":
                count += 1
        if count > 0:
            board[r][c] = str(count)
        else:
            board[r][c] = "B"
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == "E":
                    board = self.updateBoard(board, [neighbor[0], neighbor[1]])
        return board
