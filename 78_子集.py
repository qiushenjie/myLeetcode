# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#原理和77题组合一样
class Solution:
    def subsets(self, nums):
        length = len(nums)
        res = []

        for i in range(0,length + 1):
            self.helper(nums, i, 0, [], res)
        return res
    def helper(self, nums, k, used, stack, res):
        if len(stack) == k:
            res.append(stack)
            return
        while len(nums) - used >= k - len(stack):
            if nums[used] not in stack:
                nextstack = stack + [nums[used]]
                used += 1
            else:
                nextstack = stack
                used += 1
            self.helper(nums, k, used, nextstack, res)


aa = Solution().subsets([1,2,3])
print(aa)