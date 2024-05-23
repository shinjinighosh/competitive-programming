from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited= set()
        curr_path = set()

        def dfs(course):
            if course in curr_path: # we have a cycle
                return False
            if course in visited:
                return True
            visited.add(course)
            curr_path.add(course)

            for adj_node in graph[course]:
                if not dfs(adj_node):
                    return False
            
            curr_path.remove(course)
            return True

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        return True
