class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle.reverse()
        for idx, row in enumerate(triangle):
            if idx == 0:
                continue
            for i, elt in enumerate(row):
                triangle[idx][i] += min(triangle[idx-1][i], triangle[idx-1][i+1])

        return triangle[-1][0]
        
