# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''
当我们加上一个正数时，和会增加；当我们加上一个负数时，和会减少。如果当前得到的和是个负数，那
么这个和在接下来的累加中应该抛弃并重新清零，不然的话这个负数将会减少接下来的和
'''
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        maxsum = currsum = nums[0]
        currarr = []
        arr = []
        for num in nums[1:]:
            currsum = max(num, currsum + num)
            maxsum = max(currsum, maxsum)
        return maxsum
'''
动态规划，如果前一个元素（不断与计算好的前一个元素相加）大于0，则当前元素等于当前元素加上前一个元素。
如果前一个元素小于或等于零，则忽略它，当前元素保持不变。
'''
    def maxSubArray2(self, nums):
        for i in range(len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
aa = Solution().maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
print(aa)