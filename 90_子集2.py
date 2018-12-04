# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        for i in range(0, len(nums) + 1):
            self.helper(nums, i, [], 0, res)
        return res
    def helper(self, nums, k, stack, used, res):
        if len(stack) == k:
            stack.sort()
            if stack not in res:
                res.append(stack)
                return
        else:
            while len(nums) - used >= k - len(stack):
                nextstack = stack + [nums[used]]
                used += 1
                self.helper(nums, k, nextstack, used, res)

a = Solution().subsetsWithDup([1,2,2])
print(a)