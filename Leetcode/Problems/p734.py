class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        time_dict = {(u, v): w for u, v, w in times}
        visited = {}

        def bfs(start):
            agenda = deque([(start, 0)])
            while agenda:
                curr_node, curr_time = agenda.popleft()
                if curr_node in visited:
                    visited[curr_node] = min(visited[curr_node], curr_time)
                else:
                    visited[curr_node] = curr_time
                for node in range(1, n+1):
                    if node != curr_node and (curr_node, node) in time_dict:
                        if node in visited and visited[node] > curr_time + time_dict[(curr_node, node)]:
                            agenda.append((node, curr_time + time_dict[(curr_node, node)]))
                        elif node not in visited:
                            agenda.append((node, curr_time + time_dict[(curr_node, node)]))
        
        bfs(k)
        if len(visited) < n:
            return -1
        return max(visited.values())
