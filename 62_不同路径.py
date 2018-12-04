# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
class Solution:
    def uniquePaths(self, m, n):
        grid = [[0] * n for i in range(m)]
        for row in range(m): #第一列上每个位置的路径走法只有一种
            grid[row][0] = 1
        for col in range(n): #第一行上每个位置的路径走法只有一种
            grid[0][col] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1] #之后每一个的走法为当前位置上边一个和左边一个的走法的总和          
        return grid[-1][-1]
    #超出时间限制
    def uniquePaths1(self, m, n):
        count = []
        def lu(currm, currn, stack):
            if currm == m - 1 and currn == n - 1:
                count.append(stack)
                return
            elif currm == m - 1 and currn != n - 1:
                lu(currm, currn + 1, stack + 'd')
            elif currm != m - 1 and currn == n - 1:
                lu(currm + 1, currn, stack + 'r')
            else:
                lu(currm, currn + 1, stack + 'd')
                lu(currm + 1, currn, stack + 'r')
        lu(0, 0, '')
        return len(count)
a = Solution().uniquePaths(23, 12)
print(a)
