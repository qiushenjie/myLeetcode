# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
class Solution:
    def combinationSum2(self, candidates, target):
      res = []
      candidates.sort()
      def dfs(remain, ele, candidat):
        if not remain and ele not in res:
          res.append(ele)
          return
        else:
          for i in range(len(candidat)):
            if candidat[i] > remain:
              break
            elif not ele or candidat[i] >= ele[-1]:
              dfs(remain - candidat[i], ele + [candidat[i]], candidat[i + 1:]) #与上一题不同的是从当前点的之后位置开始再遍历
      candidat = candidates[:]
      dfs(target, [], candidat)
      return res
aa = Solution().combinationSum2([10,1,2,7,6,1,5] , 8)
print(aa)
