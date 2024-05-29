class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows == 1:
            return s
        numCols = len(s) + 1
        res = [[0 for i in range(numCols)] for j in range(numRows)]
        curr_row = 0
        curr_col = 0
        direction = 1 # 1 for down, 2 for right

        # go down, then zigzag up, then down
        for idx, letter in enumerate(s):
            res[curr_row][curr_col] = letter
            if direction == 1:
                if curr_row == numRows - 1:
                    # move zigzag right
                    curr_row -= 1
                    curr_col += 1
                    direction = 2
                else:
                    # move down
                    curr_row += 1
            else: # currently zigzagging
                if curr_row == 0:
                    # go down again
                    curr_row += 1
                    direction = 1
                else:
                    # continue zigzagging
                    curr_row -= 1
                    curr_col += 1
        res_str = []
        for row in res:
            for cell in row:
                if cell != 0:
                    res_str.append(cell)
        return "".join(res_str)
