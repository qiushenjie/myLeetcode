# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
# 示例 1:
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 示例 2:
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 进阶:
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

'''
只需要举出能够最坏情况的数据是 [1,1,1,1... 1] 里有一个0即可。
在这种情况下是无法使用二分法的，复杂度是O(n)
所以解法是消重，要使得nums[l]严格大于nums[r],这样就可以继续判断区间的单调性，从而二分
'''
class Solution:
    def search(self, nums, target):
    	l, r = 0, len(nums) - 1
    	while l <= r:
    		while l < r and nums[l] == nums[r]:
    			l += 1
    		mid = l + (r - l) // 2
    		if nums[mid] == target:
    			return True
    		if nums[l] <= nums[mid]:
    			if nums[l] <= target <= nums[mid]:
    				r = mid - 1
    			else:
    				l = mid + 1
    		else:
    			if nums[mid] <= target <= nums[r]:
    				l = mid + 1
    			else:
    				r = mid - 1
    	return False
aa = Solution().search([1,2,5,6,6,0,1,1], 6)
print(aa)
