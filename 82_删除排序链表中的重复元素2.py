# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

# 示例 1:

# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:

# 输入: 1->1->1->2->3
# 输出: 2->3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy = ln = ListNode(0)
        dummy.next = head
        occur = False
        while head and head.next:
            if head.val != head.next.val and not occur:
                ln.next = head
                ln = ln.next
                head = head.next
            elif head.val == head.next.val:
                head = head.next
                occur = True
            else: #说明出现过了
                head = head.next
                occur = False
        if occur == False: #最后一个
            ln.next = head
        else:
            ln.next = head.next

        return dummy.next
aa = ListNode(1)
aa.next = ListNode(2)
aa.next.next = ListNode(3)
aa.next.next.next = ListNode(3)
aa.next.next.next.next = ListNode(4)
aa.next.next.next.next.next = ListNode(4)
aa.next.next.next.next.next.next = ListNode(5)

aaa = Solution().deleteDuplicates(aa)



            