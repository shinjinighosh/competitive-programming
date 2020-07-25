# All Paths From Source to Target

'''
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(formed):
            if formed[-1] == n - 1:
                sol.append(formed)
                return
            for child in graph[formed[-1]]:
                dfs(formed + [child])

        sol, n = [], len(graph)
        dfs([0])
        return sol
