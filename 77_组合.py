# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution:
    #耗时太长
    def combine1(self, n, k):
        res = []
        nums = []
        for i in range(n):
            nums.append(i + 1)
        self.helper1(res, [], k, nums)
        return res

    def helper1(self, res, stack, k, curr):
        if len(stack) == k:
            res.append(stack)
            return
        for i in range(len(curr)):
            self.helper1(res, stack + [curr[i]], k, curr[i + 1:])

    #正确做法，当原数组中剩余的元素少于需要的元素的个数时，不再递归
    def combine(self, n, k):
        res = []
        nums = []
        for i in range(n):
            nums.append(i + 1)
        self.helper(nums, k, 0, [], res)
        return res
    def helper(self, nums, k, used, stack, res):
        if len(stack) == k:
            res.append(stack)
            return
        while len(nums) - used >= k - len(stack): #看原数组中剩余的元素数量还够不够组合 不够直接跳过
            nextstack = stack + [nums[used]] #不能用 stack += [nums[used]]，因为stack在本次递归中还要在while中比较
            used += 1
            self.helper(nums, k, used, nextstack, res)

aa = Solution().combine(10, 5)
print(aa)