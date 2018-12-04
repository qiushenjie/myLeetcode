# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for i in range(len(s)):
            if (stack == [] and s[i] not in right) or s[i] in left:
                stack.append(s[i])
            elif stack == [] and s[i] in right:
                return False
            elif s[i]  == ')' and i > 0 and stack[-1] == '(':
                stack.pop(-1)
            elif s[i]  == '}' and i > 0 and stack[-1] == '{':
                stack.pop(-1)
            elif s[i]  == ']' and i > 0 and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False
        if stack == []:
            return True
        else:
            return False
inpu = "([)]"
aa = Solution()
print(aa.isValid(inpu))
        