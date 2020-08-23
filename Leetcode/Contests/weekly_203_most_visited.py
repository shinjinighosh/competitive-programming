# 5495. Most Visited Sector in a Circular Track

'''
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).
'''


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited_count = [0 for _ in range(n)]
        for i in range(len(rounds) - 1):
            start = rounds[i]
            end = rounds[i + 1]
            sectors_visited = []
            if start <= end:
                sectors_visited = list(range(start + 1, end + 1))
            else:
                sectors_visited = list(range(start + 1, n + 1))
                sectors_visited.extend(list(range(1, end + 1)))
            # print("sectors", start, end, sectors_visited)
            for num in sectors_visited:
                visited_count[num - 1] += 1
        visited_count[rounds[0] - 1] += 1
        maxes = []
        max_count = 0
        # print(visited_count)
        for idx, i in enumerate(visited_count):
            if i > max_count:
                maxes = [idx + 1]
                max_count = i
            elif i == max_count:
                maxes.append(idx + 1)
        # visited_count.sort(reverse=True, key= lambda x: (x, visited_count.index(x)))
        return maxes
