class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(items): # takes in a list
            items = [i for i in items if i != "."]
            seen = set()
            for item in items:
                if int(item) > 9 or int(item) < 1:
                    return False
                if int(item) in seen:
                    return False
                seen.add(int(item))
            return True
        
        for row in board:
            if not isValid(row):
                return False
        
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            if not isValid(col):
                return False

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                sub_sq = []
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        sub_sq.append(board[i][j])
                if not isValid(sub_sq):
                    return False

        return True


        
