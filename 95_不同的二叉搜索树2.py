'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
      if n == 0:
        return []
      return self.helper(1, n + 1)
    def helper(self, left, right):
      if left == right:
        return None
      result = []
      for i in range(left, right):
        for l in self.helper(left, i) or [None]:
          for r in self.helper(i + 1, right) or [None]:
            root = TreeNode(i)
            root.left = l
            root.right = r
            result.append(root)
      return result
aa= Solution().generateTrees(3)
print(aa)

