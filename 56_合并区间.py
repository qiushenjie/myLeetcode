# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 定义一个区间
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        alist = []
        for item in intervals:
            alist.append([item.start, item.end]) #可排序
        alist.sort()
        if alist == []:
            return []
        res = []
        curr = Interval(alist[0][0], alist[0][1])
        for i in range(1, len(alist)):
            if alist[i][0] > curr.end:
                res.append([curr.start, curr.end])
                curr.start = alist[i][0]
                curr.end = alist[i][1]
            else:
                if alist[i][1] <= curr.end:
                    continue
                else:
                    curr.end = alist[i][1]
        res.append([curr.start, curr.end])
        return res

class Solution2:
    def merge(self, intervals):
        alist = []
        intervals.sort()
        if intervals == []:
            return []
        res = []
        curr = Interval(intervals[0][0], intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] > curr.end:
                res.append([curr.start, curr.end])
                curr.start = intervals[i][0]
                curr.end = intervals[i][1]
            else:
                if intervals[i][1] <= curr.end:
                    continue
                else:
                    curr.end = intervals[i][1]
        res.append([curr.start, curr.end])
        return res
aa = Solution2().merge([[1,4],[4,5]])
print(aa)
