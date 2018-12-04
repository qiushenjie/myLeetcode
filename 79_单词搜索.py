# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
class Solution:
    def exist(self, board, word):
        if not word:
            return True
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.helper(board, word, row, col):
                        return True
        return False

    def helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]: #当所有单词都匹配上后返回ture, 并用于下面找四个近邻的if判断语句
                return True
            tmp = board[i][j]
            board[i][j] = '#' #表示使用过
            if i > 0 and self.helper(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and self.helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and self.helper(board, word[1:], i, j + 1):
                return True
            board[i][j] = tmp #当在当前元素的基础上搜索没找时，将原始的值返还给它
            return False
        else:
            return False