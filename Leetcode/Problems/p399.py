from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1 / val

        res = []

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1
            elif src == dst:
                return 1
            queue = deque([(src, 1)])
            visited = set([src])

            while queue:
                curr_node, curr_prod = queue.popleft()
                if curr_node == dst:
                    return curr_prod
                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_prod * graph[curr_node][neighbor]))

            return -1


        res = []
        for x, y in queries:
            res.append(bfs(x, y))
        return res
