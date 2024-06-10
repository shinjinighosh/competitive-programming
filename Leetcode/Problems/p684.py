from collections import defaultdict

class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     res = []
    #     if not edges:
    #         return res
        
    #     graph = defaultdict(list)
    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)

    #     def dfs(start, parent):
    #         visited.add(start)
    #         for neighbor in graph[start]:
    #             if neighbor == parent:
    #                 continue
    #             if neighbor in visited: # found a cycle
    #                 return (start, neighbor)
    #             else:
    #                 result = dfs(neighbor, start)
    #                 if result:
    #                     return result
    #         return None

    #     visited = set()
    #     cycle_edge = None
    #     for node in graph:
    #         if node not in visited:
    #             cycle_edge = dfs(node, None)
    #             if cycle_edge:
    #                 break

    #     for u, v in reversed(edges):
    #         if (u, v) == cycle_edge or (v, u) == cycle_edge:
    #             return [u, v]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            visited = set()
            
            # Before adding the edge, try to see if u and v are already connected.
            if self.dfs(graph, u, v, visited):
                return [u, v]  # If they are connected, this edge is redundant.
            
            # Add the edge to the graph.
            graph[u].append(v)
            graph[v].append(u)

    def dfs(self, graph, start, target, visited):
        if start == target:
            return True
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited and self.dfs(graph, neighbor, target, visited):
                return True
        return False
