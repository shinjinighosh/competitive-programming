# Course Schedule II

'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
'''

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # make graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        topological_sorted_order = []

        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
