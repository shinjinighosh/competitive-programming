class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def square_of_dist_to_origin(point):
            x = point[0]
            y = point[1]
            return (x * x + y * y)
        return sorted(points, key=square_of_dist_to_origin)[:K]

        # alternate heap solution, slightly slower than the sol above
        '''
        res = []
        for i in range(len(points)):
            x, y = points[i]
            res.append(((x*x+y*y), [x,y]))

        import heapq
        heapq.heapify(res)

        arr = []
        for i in range(K):
            arr.append(heapq.heappop(res)[1])

        return arr
        '''
