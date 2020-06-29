# 310. Minimum Height Trees

'''
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n:
            return []
        if n == 1:
            return [0]
        adj = [set() for i in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = [v for v in range(n) if len(adj[v]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for u in leaves:
                v = adj[u].pop()
                adj[v].remove(u)
                if len(adj[v]) == 1:
                    new_leaves.append(v)
            leaves = new_leaves

        return leaves
