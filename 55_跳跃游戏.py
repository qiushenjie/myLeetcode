# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个位置。

# 示例 1:

# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:

# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置

#贪心算法
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if n <= 1:
            return True
        farthest = 0 #当前位置能跳的最远的位置
        i = 0
        for i in range(n):
            if i > farthest:
                return False #说明上一个能跳最远的距离跳不到i这个位置
            '''
            这时候已经满足i<=farthest,即上一次的最大跳跃距离已经能到达或者
            超过i这个位置，此时比较当前i位置基础上能跳到的最远距离即i+nums[i]
            和原始的能跳的最远距离,作为当前能跳跃的最远距离
            '''
            farthest = max(farthest, i + nums[i]) 
        return True
