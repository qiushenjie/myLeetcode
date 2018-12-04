# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

# 示例:

# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    def generateMatrix(self, n):
    	if n == 0:
    		return []
    	matrix = [[0 for i in range(n)] for j in range(n)]
    	left, right, up, down = 0, n - 1, 0, n - 1
    	num = n ** 2
    	nums = []
    	for i in range(num, 0, -1):
    		nums.append(i)
    	print(nums)
    	while left < right and up < down:
    		for col in range(left, right):
    			matrix[up][col] = nums.pop()
    		for row in range(up, down):
    			matrix[row][right] = nums.pop()
    		for col in range(right, left, -1):
    			matrix[down][col] = nums.pop()
    		for row in range(down, up, -1):
    			matrix[row][left] = nums.pop()
    		left += 1
    		right -= 1
    		up += 1
    		down -= 1
    	if left == right:
    		for row in range(up, down + 1):
    			matrix[row][left] = nums.pop()
    	elif up == down:
    		for col in range(left, right + 1):
    			matrix[up][col] = nums.pop()
    	return matrix
aa = Solution().generateMatrix(3)
print(aa)