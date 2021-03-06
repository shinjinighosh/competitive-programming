# 297. Serialize and Deserialize Binary Tree

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X"
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return str(root.val) + "," + l + "," + r

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(inp):
            node = inp.pop(0)
            if node == "X":
                return None
            tree = TreeNode(int(node))
            tree.left = build_tree(inp)
            tree.right = build_tree(inp)
            return tree

        return build_tree(data.split(","))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
