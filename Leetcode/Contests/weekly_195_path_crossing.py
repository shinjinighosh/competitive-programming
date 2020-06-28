# 5448. Path Crossing

'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.
'''


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        traj = [(0, 0,)]
        visited.add(traj[0])
        for direction in path:
            old_pos = traj[-1]
            old_x, old_y = old_pos
            if direction == 'N':
                new_x = old_x
                new_y = old_y + 1
            elif direction == 'E':
                new_x = old_x + 1
                new_y = old_y
            elif direction == 'S':
                new_x = old_x
                new_y = old_y - 1
            else:
                new_x = old_x - 1
                new_y = old_y
            if (new_x, new_y,) in visited:
                return True
            traj.append((new_x, new_y,)
            visited.append((new_x, new_y,))
        return False
