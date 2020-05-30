class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def square_of_dist_to_origin(point):
            x = point[0]
            y = point[1]
            return (x*x + y*y)
        return sorted(points, key = square_of_dist_to_origin)[:K]
            
        
