# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # the thief can rob all the houses on a level but not two adjacent levels
        # level_sums = defaultdict(int)
        
        # def get_level_sums(root, level_sums):
        #     agenda = deque([(root, 0)])
        #     visited = set()
        #     while agenda:
        #         root, level = agenda.popleft()
        #         if not root:
        #             continue
        #         visited.add(root)
        #         level_sums[level] += root.val
        #         if root.left and root.left not in visited:
        #             agenda.append((root.left, level + 1))
        #         if root.right and root.right not in visited:
        #             agenda.append((root.right, level + 1))
        #     return level_sums

        # level_sums = get_level_sums(root, level_sums)
        # arr = [level_sums[key] for key in sorted(level_sums.keys())]
        # print(arr)
        # dp = [0 for _ in range(len(arr))] # dp[i] represents the max you can get by looting upto this level
        # if not dp:
        #     return 0
        # if len(dp) <= 2:
        #     return max(arr)
        # dp[0] = arr[0]
        # dp[1] = max(arr[0], arr[1])
        # for i in range(2, len(arr)):
        #     dp[i] = max([dp[i-1], dp[i-2] + arr[i]])
        # return dp[-1]

        # but this would not work 

        def dfs(node):
            if not node:
                return (0, 0) # whether you rob or not
            
            left = dfs(node.left)
            right = dfs(node.right)

            rob_current = node.val + left[1] + right [1] # cannot rob children
            not_rob_current = max(left[0], left[1]) + max(right[0], right[1])

            return (rob_current, not_rob_current)

        res = dfs(root)
        return max(res[0], res[1])

