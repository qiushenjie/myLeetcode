# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# # 示例 1:
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# [1, 2, 7, 6, 5, 4, 3] → [1, 3, 2, 4, 5, 6, 7]
class Solution:
    def nextPermutation(self, nums):
        nidx = len(nums) - 1      
        
        def reverse(nums, l, r=nidx):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        for i in range(nidx, 0, -1):
            # find longest weakly decreasing (l -> r) suffix
            if nums[i - 1] >= nums[i]: continue
            l, r = i - 1, nidx
            while nums[r] <= nums[l]:
                r -= 1
            # there must be at least 1 successor by defn
            nums[l], nums[r] = nums[r], nums[l]
            reverse(nums, i)
            return
        nums.reverse() #上面for循环一直continue时，说明数组是降序，直接输出其升序即可
a = Solution()
a.nextPermutation(nums)
print(nums)