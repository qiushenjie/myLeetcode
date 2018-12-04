# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 示例 1:
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)
class Solution:
	#类似于梯子的问题，不同的是需要考虑'0'这个情况，'01'不能解码
    def numDecodings(self, s):
    	if s == '' or s[0] == '0':
    		return 0
    	l = len(s)
    	dp = [0] * (l + 1)
    	dp[0] = 1
    	for i in range(1, l + 1):
    		if s[i - 1] != '0':
    			dp[i] += dp[i - 1]
    		if len(s[i - 2: i]) == 2 and s[i - 2: i] >= '10' and s[i - 2: i] <= '26':
    			dp[i] += dp[i - 2] 
    	return dp[l]
aa= Solution().numDecodings('12')
print(aa)
