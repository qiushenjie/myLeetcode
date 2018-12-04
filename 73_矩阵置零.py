# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 示例 1:
# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:
# 输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


'''
题目建议最好使用常数空间，那么我们先扫描第一行，记录下第一行是否含有0。接着从第二
行开始扫描，当扫描到0时，就将“该列出现0”的信息记录到第一行中，而不是新生成一个大
小为 n 的boolean数组
'''
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        row0has0 = False
        for row in range(m):
            if matrix[row][0] == 0:
                row0has0 = True
                break

        col0has0 = False
        for col in range(n):
            if matrix[0][col] == 0:
                col0has0 = True
                break

        # 将“该列出现0”的信息记录到第一行和第一列中
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # 将非0行0列的元素置零
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0
        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0

        #将0列置零
        if col0has0:
            for col in range(n):
                matrix[0][col] = 0
        #将0行置零
        if row0has0:
            for row in range(m):
                matrix[row][0] = 0
        return matrix




    	
