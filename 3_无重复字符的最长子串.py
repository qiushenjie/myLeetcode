# 给定一个字符串，找出不含有重复字符的最长子串的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 无重复字符的最长子串是 "abc"，其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 无重复字符的最长子串是 "b"，其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 无重复字符的最长子串是 "wke"，其长度为 3。
#      请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        start = 0
        leng = 0
        maxl = 0
        for i in range(n):
            #start为本次无重复字符串开始位置的位置，因此s[i]不能和第一个字符比较
            if i != start:
                if s[i] in s[start:i]:
                    #若出现重复，start位置移至本次字符串与s[i]重复的位置的下一个位置
                    start = s[start:i].index(s[i]) + start+1
            #记录无重复字符串的长度
            leng = i - start + 1
            if leng >= maxl:
                maxl = leng
        return maxl
