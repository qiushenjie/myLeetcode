'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            el1 = nums[i]
            if (el1 in dic):
                return [dic[el1], i]
            else:
                dic[target - el1] = i


a = Solution()
aaa = a.twoSum([-2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],0)
print(aaa)
