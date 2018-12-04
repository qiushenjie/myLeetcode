# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 示例 1:

# 给定 nums = [3,2,2,3], val = 3,

# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:

# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,

# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

# 注意这五个元素可为任意顺序。

# 你不需要考虑数组中超出新长度后面的元素。
# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

#错误答案，仅供参考，但会报错，因为顺序被改了,不知道为什么不能通过
class Solution1:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        maxval = max(nums)
        if val not in nums:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = maxval
        # nums = sorted(nums) #用这句会报错
        nums.sort() #sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表
        stop = 0
        for i in range(len(nums)):
            if nums[i] != maxval:
                stop += 1
            else:
                break
        if val == maxval:
            return stop
        else:
            return stop + 1


class Solution2:
    def removeElement(self, nums, val):
        # for ele in nums: #报错
        '''
        您需要获取列表的副本并首先迭代它，否则迭代将失败，结果可能是意外结果。

        例如（取决于列表的类型）：

        for tup in somelist[:]:
            etc....
        一个例子：

        >>> somelist = range(10)
        >>> for x in somelist:
        ...     somelist.remove(x)
        >>> somelist
        [1, 3, 5, 7, 9]

        >>> somelist = range(10)
        >>> for x in somelist[:]:
        ...     somelist.remove(x)
        >>> somelist
        []          
        '''
        for ele in nums[:]: #相当于做了个副本，而且只能用[:]才能做，单纯复制给另一个变量也不行
            if ele == val:
                nums.remove(val)
        return len(nums)

class Solution3:
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start

