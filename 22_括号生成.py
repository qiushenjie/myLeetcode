# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        def dfs(left, right, ans, string):
            if left > right:#剩余的左括号比右括号多时，不添加
                return
            if not left and not right:
                ans.append(string)
            if left:
                dfs(left - 1, right, ans, string + '(')
            if right:
                dfs(left, right - 1, ans, string + ')')
        dfs(left, right, ans, "")
        return ans
