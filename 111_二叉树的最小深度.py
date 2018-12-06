# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# 分析： 
# 空树，最小深度为0 
# 左右子树都为空，最小深度为1 
# 左右子树不都为空，左右子树中有空树的情况，最小深度一定是在非空树中产生，
# 因为最小深度定义为到最近叶子节点的深度。一旦左右子树有空的情况，
# 这边的深度就可以置为正无穷，表示最小深度不可能再这里产生。
# 然后分别计算左右子树的最小深度，使用递归策略。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1