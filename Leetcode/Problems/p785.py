# 785. Is Graph Bipartite?

'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
'''


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorings = [False] * (len(graph) + 1)
        visited = set()

        def dfs(source):
            visited.add(source)
            for node in graph[source]:
                if node not in visited:
                    colorings[node] = not colorings[source]  # alternate colors
                    if not dfs(node):
                        return False
                # has already been assigned same col
                elif node in visited and colorings[source] == colorings[node]:
                    return False
            return True

        for node in range(len(graph)):
            if node not in visited and not dfs(node):
                return False

        return True
