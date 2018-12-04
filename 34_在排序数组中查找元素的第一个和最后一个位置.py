# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        #先用二分法找到某个target元素
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target: 
                break
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                left = mid + 1
        if left > right: return [-1, -1] #如果找不到target元素，返回[-1,1]

        left = 0
        right = mid - 1 #更新left为vector的头部索引，right为med-1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] != target and nums[mid + 1] == target: #满足这个退出条件，nums[med]就是我们要的元素
                break
            if nums[mid] < target: #不满足退出条件，且当前nums[med]小于target，那么更新left，继续循环
                left = mid + 1
            elif nums[mid] == target: #不满足退出条件，且nums[med]是target，那么更新right，继续循环
                right = mid - 1
        if left > right: #如果找不到我们想要的元素，left大于right了，那么med才是target元素的起始位置
            resleft = mid
        else: #如果找得到我们想要的元素，那么med+1才是target元素的起始位置
            resleft = mid + 1


        left = mid + 1
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] != target and nums[mid - 1] == target: #满足这个退出条件，nums[med]就是我们要的元素
                break
            if nums[mid] > target: #不满足退出条件，且当前nums[med]大于target，那么更新right，继续循环
                right = mid - 1
            elif nums[mid] == target: #不满足退出条件，且nums[med]是target，那么更新left，继续循环
                left = mid + 1
        if left > right: #如果找不到我们想要的元素，那么med才是target元素的结束位置
            return [resleft, mid]
        else: #如果找得到，那么med-1才是target元素的结束位置
            return [resleft, mid - 1]

a= Solution().searchRange([5,7,7,8,8,10], 7)
print(a)









