# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:

# 所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs):
    	if not strs:
    		return ''
    	else:
	        l = len(strs)
	        minl = 10000000000
	        #获得所有字符串中的最小长度
	        for st in strs:
	            if minl >= len(st):
	                minl = len(st)
	        #随机初始最长的前缀字符
	        res = strs[0][:minl]
	        result = ''
	        for j in range(minl):
		        count = 0
	        	for i in range(l):
	        		#与初始的前缀比较，若相同则加一
	        		if res[j] == strs[i][j]:
	        			count += 1
	        	#个数为字符串个数时，写入result
	        	if count == l:
	        		result  += res[j]
	        	else:
	        		break
	        return result

aa = Solution()  
print(aa.longestCommonPrefix(["flower","flow","flight"]))