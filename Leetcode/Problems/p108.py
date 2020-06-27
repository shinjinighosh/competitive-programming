class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [-10,-3,0,5,9]


class Solution:
    def sortedArrayToBST(self, arr) -> TreeNode:
        if not arr:
            return None
        pivot_point = len(arr) // 2
        new_pivot = arr[pivot_point]
        return self.convertToBSTHelper(TreeNode(new_pivot), arr[:pivot_point], arr[pivot_point + 1:])

    def convertToBSTHelper(self, root: TreeNode, left_arr, right_arr) -> TreeNode:
        if not root:
            return root
        if len(left_arr) == 1:
            root.left = TreeNode(left_arr[0])
        elif left_arr:
            pivot_point = len(left_arr) // 2
            new_pivot = left_arr[pivot_point]
            left_BST = self.convertToBSTHelper(
                TreeNode(new_pivot), left_arr[:pivot_point], left_arr[pivot_point + 1:])
            root.left = left_BST

        if len(right_arr) == 1:
            root.right = TreeNode(right_arr[0])
        elif right_arr:
            pivot_point = len(right_arr) // 2
            new_pivot = right_arr[pivot_point]
            right_BST = self.convertToBSTHelper(
                TreeNode(new_pivot), right_arr[:pivot_point], right_arr[pivot_point + 1:])
            root.right = right_BST

        return root

# alternate shorter solution


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        mid_idx = len(nums) // 2
        mid_num = nums[mid_idx]
        left_root = self.sortedArrayToBST(nums[:mid_idx])
        right_root = self.sortedArrayToBST(nums[mid_idx + 1:])
        root_node = TreeNode(mid_num, left_root, right_root)
        return root_node
