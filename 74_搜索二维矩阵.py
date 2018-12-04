# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:

# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:

# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false

'''
二维数组当成一维数组来处理
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1 # m * n - 1和普通二分里面的 len(arr) - 1 相对应的数组最后一个数的下标 
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
aa = Solution().searchMatrix(matrix, 3)
print(aa)