# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:

        def getNodeDirs(head, target, res):
            if head == target:
                res.append(1)  # signals we have found it
                return res
            if not head.right and not head.left:
                return None  # not found here
            elif not head.right:
                return getNodeDirs(head.left, target, res + ["L"])
            elif not head.left:
                return getNodeDirs(head.right, target, res + ["R"])
            else:
                # both left and right exist
                left_dir = getNodeDirs(head.left, target, res + ["L"])
                if left_dir:  # found it
                    return left_dir
                else:
                    return getNodeDirs(head.right, target, res + ["R"])

        directions = getNodeDirs(original, target, [])

        while directions:
            next_move = directions.pop(0)
            if next_move == 1:
                return cloned
            elif next_move == "L":
                cloned = cloned.left
            else:
                cloned = cloned.right

