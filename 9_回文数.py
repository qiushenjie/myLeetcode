# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:

# 你能不将整数转为字符串来解决这个问题吗？

class Solution:
    def isPalindrome(self, x):
        sig = 1
        if x < 0:
            sig = -1
        xre = str(abs(x))
        xre = xre[::-1]
        if sig == -1:
            xre += '-'
        if xre == str(x):
            return True
        else:
            return False

class Solution2:
    def isPalindrome(self, x):
        sig = 1
        lis = []
        res = 0
        if x >= 0:
            xab = x
            #数字颠倒
            while(xab > 0):
                res = res*10 + (xab%10)
                xab = int(xab / 10)
        if x < 0:
            xab = abs(x)
            while(xab > 0):
                sig = -1
                res = res*10 + (xab%10)
                xab = int(xab / 10)
        if sig == 1 and x == res:
            return True
        elif sig == -1 and abs(x) == res:
            return False
        else:
            return False
        


aa = Solution2()
print(aa.isPalindrome(121))
