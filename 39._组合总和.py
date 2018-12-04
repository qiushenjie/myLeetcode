# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:

# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
class Solution:
    def combinationSum(self, candidates, target):
      res = []
      candidates.sort()
      def dfs(remain, ele):
        if not remain: #当逐步相减至恰好为0的时候
          res.append(ele)
        else:
          for item in candidates: #每一次都对所有元素遍历，广度优先遍历
            if item > remain: #当前项大于剩余值时，循环停止
              break
            elif not ele or item >= ele[-1]:
              dfs(remain - item, ele + [item])
      dfs(target, [])
      return res
aa = Solution().combinationSum([2,3,6,7] , 7)
print(aa)