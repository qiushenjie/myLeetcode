# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

# 实现一个将字符串进行指定行数变换的函数:

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:

# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I
class Solution:
	#自上而下，自下而上
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            lis = [""] * numRows
            index, step = 0, 1
            for x in s:
                lis[index] += x
                if index == numRows - 1:
                    step = -1
                elif index == 0:
                    step = 1
                index += step
        return ''.join(lis)

aa = Solution()
print(aa.convert("PAYPALISHIRING", 4))