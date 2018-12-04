# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        #先进行排序
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l - 1] == nums[l]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                #数组已排过序，因此当s小于0时，需要nums[l]向右移来增大s
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res

a = Solution()
aaa = a.threeSum([1, 0, 1, 2, -1, -1, -4])
print(aaa)