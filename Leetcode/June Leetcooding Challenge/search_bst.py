# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        # print(root.val, root.left, root.right)
        if not root.left and not root.right:
            return None
        elif not root.right:
            if root.left.val == val:
                return root.left
            else:
                return self.searchBST(root.left, val)
        elif not root.left:  # only right side exists
            if root.right.val == val:
                return root.right
            else:
                return self.searchBST(root.right, val)
        else:  # choose a side
            # print("val is", val, "and left val is ", root.left.val, "and right val is", root.right.val)
            if val > root.val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    # import sys
    # import io
    #
    # def readlines():
    #     for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
    #         yield line.strip('\n')
    #
    # lines = readlines()
    trees = ['[4, 2, 7, 1, 3]']
    vals = [2]
    # while True:
    for i in range(len(trees)):
        try:
            # line = next(lines)
            line = trees[i]
            root = stringToTreeNode(line)
            # line = next(lines)
            # val = int(line)
            val = vals[i]

            print(treeNodeToString(root))
            ret = Solution().searchBST(root, val)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
