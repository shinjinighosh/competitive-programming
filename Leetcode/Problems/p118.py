class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(2, numRows+1):
            old_row = result [-1]
            new_row = [old_row[0]]
            for idx in range(len(old_row)-1):
                new_row.append(old_row[idx] + old_row[idx+1])
            new_row.append(old_row[-1])
            result.append(new_row)
        return result
        
