# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 说明：m 和 n 的值均不超过 100。
# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0] * n for i in range(m)]
        for col in range(n):
            if obstacleGrid[0][col] != 1:
                grid[0][col] = 1
            else:
                break
        for row in range(m):
            if obstacleGrid[row][0] != 1:
                grid[row][0] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
        return grid[-1][-1]
a = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
aa = Solution().uniquePathsWithObstacles(a)
print(aa)






