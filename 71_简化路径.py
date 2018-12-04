# 给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

# 例如，
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

# 边界情况:

# 你是否考虑了 路径 = "/../" 的情况？
# 在这种情况下，你需返回 "/" 。
# 此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
# 在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 
class Solution:
    def simplifyPath(self, path):
        stack = []
        path = path.split('/') #直接去除'//'和'/'
        for item in path:
            if not item or item == '.':
                continue
            elif item == '..' and stack:
                stack.pop() 
            elif item == '..' and not stack:
                continue
            else:
                stack.append(item)
        return '/' + '/'.join(stack)
aa = Solution().simplifyPath("/home//foo/")
print(aa)
