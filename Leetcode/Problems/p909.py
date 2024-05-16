class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = len(board)

        def get_coords(pos):
            row = (pos - 1) // self.n
            col = (pos - 1) % self.n
            if row % 2 != 0:
                col = self.n - 1 - col  # Reverse column order on odd rows
            return self.n - 1 - row, col  # Transform row to start from the bottom

          
        def bfs(board):           
            agenda = [(1, 0)]
            seen = set([1])
            while agenda:
                curr_pos, curr_path = agenda.pop(0)

                if curr_pos >= self.n * self.n:
                    return curr_path


                for next_pos in range(curr_pos + 1, 1 + min(curr_pos + 6, self.n * self.n)):
                    r, c = get_coords(next_pos)
                    if board[r][c] != -1: # if this is a snake or ladder
                        next_pos = board[r][c]
                    if next_pos not in seen:
                        seen.add(next_pos)
                        agenda.append((next_pos, curr_path + 1))

            return -1

        return bfs(board)

                

        
