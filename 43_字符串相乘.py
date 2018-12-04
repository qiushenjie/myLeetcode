# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：

# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

class Solution:
    def multiply(self, num1, num2):
      numDic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
      strDic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
      l1 = len(num1)
      l2 = len(num2)
      res1 = 0
      res2 = 0
      for i in range(l1):
        res1 += numDic[num1[i]] * (10 ** (l1 - i - 1))
      for i in range(l2):
        res2 += numDic[num2[i]] * (10 ** (l2 - i - 1))
      ans = res1 * res2
      if ans == 0:
        return '0'
      a = []
      while ans // 10 != 0 or ans % 10 != 0:
        a.append(strDic[ans % 10])
        ans = ans // 10
      fina = ''
      for i in a[::-1]:
        fina += i
      return fina
aa= Solution().multiply('123', '456')
print(aa)