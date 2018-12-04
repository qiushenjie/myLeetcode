# 给定一个 32 位有符号整数，将整数中的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321
# 示例 3:

# 输入: 120
# 输出: 21
# 注意:

# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
class Solution:
    def reverse(self, x):
        if x < 0:
            sig = -1
        else:
            sig = 1
        strx = str(abs(x))
        strx = strx[::-1]
        res = sig*int(strx)
        if res <= -1*2**31 or res >= 2**31:
            return 0
        return res
xx = Solution()
print(xx.reverse(1534236469))