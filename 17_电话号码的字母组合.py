# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 示例:

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution:
    def letterCombinations(self, digits):
    	num2char = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    	if '1' in str(digits) or '0' in str(digits) or digits == '':
    		return []
    	else:
    		digits = str(digits)
    		res = ['']
    		for digit in digits:
    			res_curr = []
    			for alp in num2char[digit]:
	    			res_curr.extend([ele + alp for ele in res])
	    		res = res_curr
	    	return res




aa = Solution()
print(aa.letterCombinations(29))
