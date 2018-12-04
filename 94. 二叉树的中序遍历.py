# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归解法
class Solution1:
    def inorderTraversal(self, root):
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

#迭代解法
#先把迭代到最左边的叶子节点，把所有途中的root放进stack，当左边走不通了，开始往res里面存数，并往右边走
class Solution:
    def inorderTraversal(self, root):
    	res, stack = [], []
    	while stack or root:
    		if root:
    			stack.append(root)
    			root = root.left
    		else:
    			node = stack.pop() 
    			res.append(node.val)
    			root = node.right
    	return res

