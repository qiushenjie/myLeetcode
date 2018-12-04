# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

# 示例 1:

# 输入: 3
# 输出: "III"
# 示例 2:

# 输入: 4
# 输出: "IV"
# 示例 3:

# 输入: 9
# 输出: "IX"
# 示例 4:

# 输入: 58
# 输出: "LVIII"
# 解释: C = 100, L = 50, XXX = 30, III = 3.
# 示例 5:

# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.

class Solution:
    def intToRoman(self, num):
        if num > 3999 or num < 0:
            return False
        st = []
        add = 0
        i = 0
        while(num > 0):
            current = (num % 10)
            num = ((num - current)//10)
            resnum = current * 10 ** i
            i += 1
            st.append(resnum)
        resstr = []
        for nu in st[::-1]:
            if nu >= 1000 and nu <= 3000:
                resstr.append('M' * int(nu / 1000))
            elif nu == 900:
                resstr.append('CM')
            elif nu == 400:
                resstr.append('CD')
            elif nu >= 100 and nu < 400:
                resstr.append('C' * int(nu / 100))
            elif nu == 500:
                resstr.append('D')
            elif nu > 400 and nu < 900:
                resstr.append('D' + 'C' * int(nu / 100 - 5))
            elif nu == 90:
                resstr.append('XC')
            elif nu == 40:
                resstr.append('XL')
            elif nu >= 10 and nu < 40:
                resstr.append('X' * int(nu / 10))
            elif nu == 50:
                resstr.append('L')
            elif nu > 40 and nu < 90:
                resstr.append('L' + 'X' * int(nu / 10 - 5))
            elif nu == 9:
                resstr.append('IX')
            elif nu == 4:
                resstr.append('IV')
            elif nu >= 1 and nu < 4:
                resstr.append('I' * int(nu))
            elif nu == 5:
                resstr.append('V')
            elif nu > 4 and nu < 9:
                resstr.append('V' + 'I' * int(nu - 5))
        res = ''.join(resstr)
        return res

class Solution2:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        M = ["", "M", "MM", "MMM"]
        
        #123 // 10 = 12; 123 / 10 = 12.3
        return M[(num // 1000) % 10] + C[(num // 100) % 10] + X[(num // 10) % 10] + I[num % 10]

aa = Solution()
print(aa.intToRoman(58))