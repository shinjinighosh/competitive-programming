# 5211. Path with Maximum Probability

'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
'''


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        # doesn't find all paths
        # q = [[start, 1]]
        # probs = []
        # visited = set()
        # while q:
        #     node, prob = q.pop()
        #     # print(node, prob)
        #     if node == end:
        #         probs.append(prob)
        #     if node not in visited:
        #         for i, edge in enumerate(edges):
        #             # print(i, edge)
        #             if edge[0] == node:
        #                 q.append([edge[1], prob * succProb[i]])
        #             elif edge[1] == node:
        #                 q.append([edge[0], prob * succProb[i]])
        #     visited.add(node)
        # if not probs:
        #     return 0

        visited = [False] * n
        path = []
        all_paths = []
        # paths = [i for i in self.yieldAllPathsUtil(start, end, visited, path, edges, all_paths)]
        self.yieldAllPathsUtil(start, end, visited, path, edges, all_paths)
        paths = all_paths
        # print(paths)
        prob_dict = {}
        for i, edge in enumerate(edges):
            prob_dict[(edge[0], edge[1])] = succProb[i]
            prob_dict[(edge[1], edge[0])] = succProb[i]
        probs = []
        if not paths:
            return 0
        for path in paths:
            prob = 1
            for i in range(len(path) - 1):
                prob *= prob_dict[(path[i], path[i + 1])]
            probs.append(prob)
        return max(probs)

    def yieldAllPathsUtil(self, u, d, visited, path, edges, all_paths):
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        if u == d:
            # print("got here")
            k = [n for n in path]
            all_paths.append(k)
            return
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for idx, edge in enumerate(edges):
                # print(u, d, edge)
                if edge[0] == u:
                    # print("edge found")
                    if not visited[edge[1]]:
                        self.yieldAllPathsUtil(edge[1], d, visited, path, edges, all_paths)
                elif edge[1] == u:
                    # print("edge found 2")
                    if not visited[edge[0]]:
                        self.yieldAllPathsUtil(edge[0], d, visited, path, edges, all_paths)
            # for i in self.graph[u]:
            #     if visited[i]==False:
            #         self.yieldAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False


'''
testcases
3
[[0,1],[1,2],[0,2]]
[0.5,0.5,0.2]
0
2
3
[[0,1],[1,2],[0,2]]
[0.5,0.5,0.3]
0
2
3
[[0,1]]
[0.5]
0
2
5
[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
[0.37,0.17,0.93,0.23,0.39,0.04]
3
4
'''
