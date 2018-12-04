# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums):
      res = []
      def dfs(curr, stack):
        if not curr:
          res.append(stack)
          return
        else:
          for i in range(len(curr)):
            dfs(curr[: i] + curr[i + 1:], stack + [curr[i]])
      dfs(nums, [])
      return res
aa = Solution().permute([1, 2, 3])
print(aa)