class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for a, b in edges:
            if a in seen:
                return a
            else:
                seen.add(a)
            if b in seen:
                return b
            else:
                seen.add(b)
        
