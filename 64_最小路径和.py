# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:

# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

#动态规划，维护当前位置的最小路径和
class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for col in range(1, n):
            grid[0][col] = grid[0][col] + grid[0][col - 1]
        for row in range(1, m):
            grid[row][0] = grid[row][0] + grid[row - 1][0]
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]

a =[[1,2,5],[3,2,1]]
aa = Solution().minPathSum(a)
print(aa)