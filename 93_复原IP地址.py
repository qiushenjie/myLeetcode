# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 示例:

# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
class Solution:
    def restoreIpAddresses(self, s):
    	if not s:
    		return []
    	res = []
    	self.helper(s, 0, res, [])
    	return res

    def helper(self, currentS, k, res, stack):
    	if not currentS:
    		if k == 4:
    			res.append('.'.join(stack)) # 以.分隔作为字符串返回
    		return
    	if k == 4: # 分了4段，结束
    		return
    	# 取一位
    	self.helper(currentS[1:], k + 1, res, stack + [currentS[:1]])
        # 若要取2位及以上，要确保目前的第一位不能为0
    	if currentS[0] != '0':
    		if len(currentS) >= 2:
    			self.helper(currentS[2:], k + 1, res, stack + [currentS[:2]])
    		if len(currentS) >= 3 and int(currentS[:3]) <= 255: # 若要取3位，则要保证小于255
    			self.helper(currentS[3:], k + 1, res, stack + [currentS[:3]])

aa = Solution().restoreIpAddresses("25525511135")
print(aa)
