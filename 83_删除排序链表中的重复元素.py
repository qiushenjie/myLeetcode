# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:

# 输入: 1->1->2
# 输出: 1->2
# 示例 2:

# 输入: 1->1->2->3->3
# 输出: 1->2->3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy = ln = ListNode(0)
        dummy.next = head
        while head:
            if head.next == None: #直接处理最后一个节点
                ln.next = head
                break
            if head.val == head.next.val:
                head = head.next
            else:
                ln.next = head
                head = head.next
                ln = ln.next
        return dummy.next
                

