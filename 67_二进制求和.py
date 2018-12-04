# 给定两个二进制字符串，返回他们的和（用二进制表示）。

# 输入为非空字符串且只包含数字 1 和 0。

# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"
class Solution:
    def addBinary(self, a, b):
        def binaryToTen(num):
            strnum = str(num)
            l = len(strnum)
            count = 0
            for item in strnum:
                count += int(item) * 2 ** (l - 1)
                l -= 1
            return count
        def tenToBinaryTo(num):
            res = []
            res.append(str(num % 2))
            while num // 2 != 0:
                num = num // 2
                res.append(str(num % 2))
            res.reverse()
            res = ''.join(res)
            return res
        tena = binaryToTen(a)
        tenb = binaryToTen(b)
        sums = tena + tenb
        result = tenToBinaryTo(sums)
        return result
aa = Solution().addBinary("1010", "1011")
print(aa)


