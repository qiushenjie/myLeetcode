# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:

# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:

# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
        	return []
        res = []
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while up < down and left < right:
        	res.extend([matrix[up][col] for col in range(left, right)])
        	res.extend([matrix[row][right] for row in range(up, down)])
        	res.extend([matrix[down][col] for col in range(right, left, -1)])
        	res.extend([matrix[row][left] for row in range(down, up, -1)])
        	up += 1
        	down -= 1
        	left += 1
        	right -= 1
        if left == right:
        	res.extend([matrix[row][left] for row in range(up, down + 1)])
        elif up == down:
        	res.extend([matrix[up][col] for col in range(left, right + 1)])
        return res
    
a =[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
aa = Solution().spiralOrder(a)
print(aa)
            
