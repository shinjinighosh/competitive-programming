# 695. Max Area of Island

'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Understand
- Given 2d array of 0's and 1's, output the maximum number of 1's in a cluster, where a cluster is composed by neighboring elements that are the same

Match
- Traversal problem
- DFS

Plan
Main
Initialize visited as 2d array of False
Loop through each element in the 2d array
- if the element == 1 and not visited
  - perform dfs from this element
  - record the size of the cluster and check for the maximum

DFS plan
- take in i, j as coordinate in the 2d array
- mark visited[i][j] as True
- initialize return value as 1
- for each of the 4 neighboring coordinates
  - if neighboring coordinate is valid and neighboring element == 1 and not visited[neighboring]
    - return value += dfs(neighboring coordinate)
- return the return value
'''


def maxAreaOfIsland(grid):

    def dfs(i, j):
        visited[i][j] = True
        max_cluster = 1
        for x_new, y_new in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x_new < rows and 0 <= y_new < cols and grid[x_new][y_new] and not visited[(x_new, y_new)]:
                max_cluster += dfs(x_new, y_new)
        return max_cluster

    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = {(i, j): False for j in range(cols) for i in range(rows)}
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] and not visited[(i, j)]:
                island_size = dfs(i, j)
                if island_size > res:
                    res = island_size
    return res
