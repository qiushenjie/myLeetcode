# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:

# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:

# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    #计算深度
    def height(self, root):
        if not root:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        return max(leftheight, rightheight) + 1

class Solution2:
    def isBalanced(self, root):
        self.isTrue = True
        self.height(root)
        return self.isTrue

    def height(self, root):
        if not root:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if abs(leftheight - rightheight) > 1:
            self.isTrue = False

        return max(leftheight, rightheight) + 1




