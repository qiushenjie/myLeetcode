# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

class Solution:
    #题目要求时间复杂度为O(logn)
    def search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2 #取中间值
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]: #此时begin和mid肯定处在同一个递增数组上
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1 #在此递增数组上继续二分查找
                else:
                    l = mid + 1
            else: #此时mid处于第二个递增数组 begin处于第一个递增数组 自然的mid和end肯定处于第二个递增数组上
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1 #在此递增数组上继续二分查找
                else:
                    r = mid - 1 
        return -1

nums = [4,5,6,7,0,1,2]
a = Solution().search(nums, target = 0)
print(a)

