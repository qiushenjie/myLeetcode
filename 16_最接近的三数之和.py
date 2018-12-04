# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return []
        #先进行排序
        nums.sort()
        res = []
        mins = 100000000
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i + 1, len(nums) - 1
            #针对只有唯一解
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target)  <  abs(mins - target):
                    mins = s
                #找其他可能
                if s == target:
                    return target
                elif s > target:
                    r -= 1
                else:
                    l += 1
                    
        return mins

a = Solution()
aaa = a.threeSumClosest([-4,-2,-2,-2,0,3,4,4,6,6], 7)
print(aaa)