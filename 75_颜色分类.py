# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
class Solution:
    def sortColors(self, nums):
        m = len(nums)
        for i in range(m - 1, 0, -1):
            maxposition = 0
            for j in range(1, i + 1):
                if nums[j] >= nums[maxposition]:
                    maxposition = j
            nums[i], nums[maxposition] = nums[maxposition], nums[i]
        return nums


class Solution2:
    def sortColors(self, nums):
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return nums
aa = Solution2().sortColors([2,0,2,1,1,0])
print(aa)
