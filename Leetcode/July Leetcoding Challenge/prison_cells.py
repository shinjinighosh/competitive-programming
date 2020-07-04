#   Prison Cells After N Days

'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
'''


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # 14 day loop
        # N -= max(N - 1, 0) / 14 * 14
        # for i in range(int(N)):
        #     cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        # return cells
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells
