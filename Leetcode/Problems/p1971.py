# includes TLE solution commented out at the top

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        visited = set()

        # def dfs(edges, node, visited):
        #     # print("Starting dfs with", node, visited)
        #     if node == destination:
        #         return True
        #     if node not in visited:
        #         visited.add(node)
        #         for edge in edges:
        #             if edge[0] == node and edge[1] not in visited:
        #                 if dfs(edges, edge[1], visited):
        #                     return True
        #             elif edge[1] == node and edge[0] not in visited:
        #                 if dfs(edges, edge[0], visited):
        #                     return True
        #     return False

        # for node_a, node_b in edges:
        #     if node_a == source:
        #         if dfs(edges, node_a, visited):
        #             return True
        #     elif node_b == source:
        #         if dfs(edges, node_b, visited):
        #             return True

        # Convert edges to adjacency list for faster access
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        def dfs(node):
            # Check if the current node is the destination
            if node == destination:
                return True
            
            # Mark the current node as visited
            visited.add(node)
            
            # # Explore neighbors
            # for edge in edges:
            #     if node in edge:
            #         # Find the neighbor node
            #         neighbor = edge[0] if edge[1] == node else edge[1]
            #         # If the neighbor is not visited, recursively call dfs
            #         if neighbor not in visited:
            #             if dfs(neighbor):
            #                 return True

            # Explore neighbors
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

        return dfs(source)
        # return False        
